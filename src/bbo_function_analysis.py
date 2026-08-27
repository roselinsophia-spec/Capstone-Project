"""Original BBO analysis for the official Mini-lesson 12.8 starter data.

Run one function: python bbo_function_analysis.py --function 1
Run all functions: python bbo_function_analysis.py --all
Predictions and proposed queries are unevaluated model outputs.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm, qmc
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.preprocessing import StandardScaler

SEED = 42
N_CANDIDATES = 20_000
KAPPA = 2.0
XI = 0.01
ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "initial_data"
RESULTS_DIR = ROOT / "results"


def load_data(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    folder = DATA_DIR / f"function_{function_id}"
    X = np.load(folder / "initial_inputs.npy").astype(float)
    y = np.load(folder / "initial_outputs.npy").astype(float).reshape(-1)
    if X.ndim != 2 or y.ndim != 1 or len(X) != len(y):
        raise ValueError(f"Invalid shapes for Function {function_id}: {X.shape}, {y.shape}")
    if not np.isfinite(X).all() or not np.isfinite(y).all():
        raise ValueError(f"Non-finite data found for Function {function_id}")
    if np.any((X < 0) | (X > 1)):
        raise ValueError(f"Function {function_id} contains inputs outside [0, 1]")
    return X, y


def expected_improvement(mu, sigma, best, xi=XI):
    improvement = mu - best - xi
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.divide(improvement, sigma, out=np.zeros_like(mu), where=sigma > 0)
        result = improvement * norm.cdf(z) + sigma * norm.pdf(z)
    return np.where(sigma > 0, result, 0.0)


def probability_improvement(mu, sigma, best, xi=XI):
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.divide(mu - best - xi, sigma, out=np.zeros_like(mu), where=sigma > 0)
    return np.where(sigma > 0, norm.cdf(z), 0.0)


def fit_gp(X, y):
    x_scaler = StandardScaler().fit(X)
    y_scaler = StandardScaler().fit(y.reshape(-1, 1))
    Xs = x_scaler.transform(X)
    ys = y_scaler.transform(y.reshape(-1, 1)).ravel()
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(X.shape[1]), length_scale_bounds=(1e-2, 1e2), nu=2.5
    ) + WhiteKernel(noise_level=1e-5, noise_level_bounds=(1e-10, 1e0))
    gp = GaussianProcessRegressor(kernel=kernel, normalize_y=False,
                                  n_restarts_optimizer=5, random_state=SEED)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        gp.fit(Xs, ys)
    return gp, x_scaler, y_scaler


def analyse(function_id: int) -> pd.DataFrame:
    X, y = load_data(function_id)
    gp, x_scaler, y_scaler = fit_gp(X, y)
    candidates = qmc.LatinHypercube(d=X.shape[1], seed=SEED + function_id).random(N_CANDIDATES)
    # Prevent effectively duplicate recommendations.
    nearest = np.min(np.linalg.norm(candidates[:, None, :] - X[None, :, :], axis=2), axis=1)
    candidates = candidates[nearest > 1e-6]
    mu_s, sigma_s = gp.predict(x_scaler.transform(candidates), return_std=True)
    scale = float(y_scaler.scale_[0])
    mu = y_scaler.inverse_transform(mu_s.reshape(-1, 1)).ravel()
    sigma = sigma_s * scale
    best = float(np.max(y))
    scores = {
        "UCB": mu + KAPPA * sigma,
        "EI": expected_improvement(mu, sigma, best),
        "PI": probability_improvement(mu, sigma, best),
    }
    rows = []
    for method, score in scores.items():
        j = int(np.argmax(score))
        rows.append({
            "function": function_id,
            "method": method,
            "proposed_query": "-".join(f"{v:.6f}" for v in candidates[j]),
            "predicted_mean": mu[j],
            "predicted_std": sigma[j],
            "acquisition_score": score[j],
            "best_observed_output": best,
            "evaluated_by_hidden_function": False,
        })
    out = pd.DataFrame(rows)
    folder = RESULTS_DIR / f"function_{function_id}"
    folder.mkdir(parents=True, exist_ok=True)
    out.to_csv(folder / "acquisition_recommendations.csv", index=False)

    best_i = int(np.argmax(y))
    pd.DataFrame([{
        "function": function_id, "observations": len(y), "dimensions": X.shape[1],
        "best_observed_input": "-".join(f"{v:.6f}" for v in X[best_i]),
        "best_observed_output": y[best_i], "output_min": y.min(),
        "output_mean": y.mean(), "output_median": np.median(y), "output_std": y.std(),
    }]).to_csv(folder / "observed_summary.csv", index=False)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.hist(y, bins=min(10, len(y)), color="#315c9b", edgecolor="white")
    ax.axvline(best, color="#c43c35", linestyle="--", label="Best observed")
    ax.set(title=f"Function {function_id}: observed output distribution",
           xlabel="Observed output", ylabel="Frequency")
    ax.legend(); fig.tight_layout()
    fig.savefig(folder / "observed_output_distribution.png", dpi=180)
    plt.close(fig)

    if X.shape[1] == 2:
        fig, ax = plt.subplots(figsize=(6, 5))
        sc = ax.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=75, edgecolor="black")
        ax.scatter(X[best_i, 0], X[best_i, 1], marker="*", s=240, color="red", label="Best observed")
        ax.set(xlabel="x1", ylabel="x2", title=f"Function {function_id}: official observations",
               xlim=(0, 1), ylim=(0, 1))
        ax.legend(); fig.colorbar(sc, ax=ax, label="Observed output"); fig.tight_layout()
        fig.savefig(folder / "observed_input_space.png", dpi=180)
        plt.close(fig)
    print(f"\nFunction {function_id}: {len(y)} observations, {X.shape[1]} dimensions")
    print(f"Best observed: {'-'.join(f'{v:.6f}' for v in X[best_i])} -> {best:.12g}")
    print(out.to_string(index=False))
    return out


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--function", type=int, choices=range(1, 9))
    group.add_argument("--all", action="store_true")
    args = parser.parse_args()
    ids = range(1, 9) if args.all else [args.function]
    combined = pd.concat([analyse(i) for i in ids], ignore_index=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    combined.to_csv(RESULTS_DIR / "all_acquisition_recommendations.csv", index=False)


if __name__ == "__main__":
    main()
