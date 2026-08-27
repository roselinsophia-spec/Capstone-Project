# Black-Box Optimisation Capstone Project

## Non-technical explanation

This project investigates how to make effective decisions when the internal rules of a system are hidden. I analysed observations from eight unknown functions and developed a Bayesian optimisation pipeline to identify promising inputs for future evaluation. The method builds an approximate model from the available evidence and balances exploring uncertain areas with refining regions expected to perform well. Three query-selection strategies were compared. The analysis reports the strongest course-provided observations and generates new candidate inputs. These candidates are recommendations rather than confirmed improvements because they have not been evaluated by the hidden functions. This approach reflects real applications such as hyperparameter tuning, engineering design and simulation-based optimisation.

## 1. Project overview

This repository documents my work on a **Black-Box Optimisation (BBO) capstone challenge**. Black-box optimisation is useful when the mathematical structure of an objective function is unavailable or too expensive to evaluate extensively.

The project contains eight synthetic hidden functions. For each function, the available information consists of:

- previously evaluated input points
- corresponding observed outputs
- the requirement to maximise the output
- the constraint that every input coordinate must remain between 0 and 1

The objective is to use the available observations efficiently and propose promising candidate points for future evaluation.

This project demonstrates skills in:

- exploratory data analysis
- Bayesian optimisation
- Gaussian Process modelling
- uncertainty-aware decision-making
- experiment organisation
- reproducible Python development
- technical and non-technical communication

## 2. Data

The project uses the official starter data supplied for the course Black-Box Optimisation challenge. The data contains observed inputs and corresponding outputs for eight synthetic hidden functions.

| Function | Observations | Input dimensions | Objective |
|---|---:|---:|---|
| Function 1 | 10 | 2 | Maximise |
| Function 2 | 10 | 2 | Maximise |
| Function 3 | 15 | 3 | Maximise |
| Function 4 | 30 | 4 | Maximise |
| Function 5 | 20 | 4 | Maximise |
| Function 6 | 20 | 5 | Maximise |
| Function 7 | 30 | 6 | Maximise |
| Function 8 | 40 | 8 | Maximise |

The files are stored under [`data/`](data/) in folders named `function_1` through `function_8`. Each function folder contains:

- `initial_inputs.npy` – evaluated input points
- `initial_outputs.npy` – corresponding observed outputs
- `README.md` – a function-specific explanation

The observations in the data folders are genuine course-provided data. Model-generated query recommendations are stored separately under [`results/`](results/) and have not been evaluated by the hidden functions.

Further information about the dataset, its composition, limitations and appropriate uses is provided in the [datasheet](docs/datasheet.md).

## 3. Inputs and outputs

For every function, an input is a point containing the required number of coordinates. Each coordinate must be between 0 and 1.

When preparing a query for submission, coordinates are formatted to six decimal places and separated by hyphens. For example, a two-dimensional query may be written as:

```text
0.123456-0.654321
```

The output is a single numerical value returned by the hidden function. All eight functions are treated as **maximisation problems**, meaning that a higher observed output is considered better.

For functions whose outputs are negative, the highest value is the one closest to zero. However, this does not imply that zero is necessarily the unknown global optimum.

## 4. Function contexts

The functions are synthetic, but the course provides illustrative applications showing how similar optimisation problems may occur in practice.

| Function | Illustrative context |
|---|---|
| Function 1 | Detecting a source in a two-dimensional area with sparse non-zero readings |
| Function 2 | Maximising a noisy log-likelihood surface containing local optima |
| Function 3 | Selecting three compound quantities while minimising transformed adverse effects |
| Function 4 | Tuning four parameters in a dynamic warehouse-placement system |
| Function 5 | Maximising the yield of a four-variable chemical process |
| Function 6 | Optimising five recipe inputs using a negative combined score |
| Function 7 | Tuning six machine-learning hyperparameters |
| Function 8 | Optimising a complex eight-dimensional system |

These contexts are explanatory analogies. The repository contains synthetic function observations rather than real medical, industrial or business data.

## 5. Technical approach

### Exploratory analysis

For each function, the program:

1. loads the official NumPy input and output arrays
2. validates their dimensions and numerical values
3. identifies the strongest observed result
4. summarises the observed output distribution
5. produces visualisations of the available observations

Two-dimensional input-space plots are produced for Functions 1 and 2. For higher-dimensional functions, output-distribution plots are used because a single two-dimensional plot cannot represent the complete response surface.

### Gaussian Process surrogate

A **Gaussian Process Regressor** is fitted separately to each function. The surrogate supplies a predicted mean output and an estimate of predictive uncertainty for each candidate input.

A Matérn kernel is used because it can represent response surfaces that are not perfectly smooth. Input and output scaling support numerical stability across functions with different output ranges.

### Candidate generation

Candidate input points are generated using **Latin Hypercube Sampling** within the valid interval `[0, 1]`. This gives structured coverage without requiring an exhaustive grid, which becomes impractical as dimensionality increases.

### Acquisition functions

The pipeline compares three Bayesian optimisation acquisition functions:

- **Upper Confidence Bound (UCB)** – combines predicted performance and uncertainty
- **Expected Improvement (EI)** – estimates expected improvement over the current best observation
- **Probability of Improvement (PI)** – estimates the probability that a candidate will improve on the current best observation

These methods balance:

- **exploration** – investigating uncertain or weakly sampled areas
- **exploitation** – refining areas predicted to perform strongly

The code generates one recommended candidate from each acquisition method. These recommendations are retained for comparison and are not presented as confirmed improvements.

## 6. Strategy development

My broader strategy developed from exploratory reasoning towards a systematic Bayesian optimisation workflow. During the capstone, I considered ideas including:

- local refinement around promising observations
- neighbourhood-based reasoning
- regression for estimating local trends
- threshold-based classification of stronger and weaker regions
- SVM-style boundary reasoning
- clustering-style identification of recurring regions
- uncertainty-aware Bayesian optimisation

Regression, classification, SVM, clustering and neural-network ideas influenced my interpretation of the challenge. However, the reproducible final pipeline uses a **Gaussian Process surrogate with UCB, EI and PI acquisition functions**. This distinction prevents conceptual methods considered during the course from being confused with models implemented in the final code.

## 7. Results

The analysis records the strongest observation in the official starter data for each function.

| Function | Best observed output |
|---|---:|
| Function 1 | `7.710875e-16` |
| Function 2 | `0.611205` |
| Function 3 | `-0.034835` |
| Function 4 | `-4.025542` |
| Function 5 | `1088.859618` |
| Function 6 | `-0.714265` |
| Function 7 | `1.364968` |
| Function 8 | `9.598482` |

The generated results include:

- an observed-data summary for every function
- observed-output distribution plots
- two-dimensional input-space plots for Functions 1 and 2
- candidate recommendations produced by UCB, EI and PI
- a combined recommendations file covering all eight functions

The combined recommendations are available in [`results/all_acquisition_recommendations.csv`](results/all_acquisition_recommendations.csv).

### Interpretation of results

The best observed values are genuine results from the course-provided data. In contrast, the acquisition recommendations are predictions from fitted surrogate models.

The recommendations cannot be described as improvements, successful queries or global optima unless they are submitted to the hidden functions and evaluated. Therefore:

- observed outputs are reported as evidence
- model predictions are reported as estimates
- recommended inputs are reported as unevaluated candidates
- no claim of finding a global optimum is made

## 8. Repository structure

```text
Capstone-Project/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   ├── function_1/
│   ├── function_2/
│   ├── function_3/
│   ├── function_4/
│   ├── function_5/
│   ├── function_6/
│   ├── function_7/
│   └── function_8/
├── docs/
│   ├── README.md
│   ├── datasheet.md
│   ├── model-card.md
│   └── module-22-strategy.md
├── notebooks/
│   ├── README.md
│   └── bbo_analysis.ipynb
├── results/
│   ├── all_acquisition_recommendations.csv
│   ├── function_1/
│   ├── function_2/
│   ├── function_3/
│   ├── function_4/
│   ├── function_5/
│   ├── function_6/
│   ├── function_7/
│   └── function_8/
└── src/
    └── bbo_function_analysis.py
```

## 9. Repository contents

- [`data/`](data/) – official course-provided observations for all eight functions
- [`data/README.md`](data/README.md) – data provenance and organisation
- [`src/bbo_function_analysis.py`](src/bbo_function_analysis.py) – reproducible Bayesian optimisation pipeline
- [`notebooks/bbo_analysis.ipynb`](notebooks/bbo_analysis.ipynb) – notebook-based analysis
- [`results/`](results/) – generated summaries, plots and candidate recommendations
- [`results/all_acquisition_recommendations.csv`](results/all_acquisition_recommendations.csv) – combined acquisition recommendations
- [`docs/datasheet.md`](docs/datasheet.md) – dataset documentation
- [`docs/model-card.md`](docs/model-card.md) – model documentation
- [`docs/module-22-strategy.md`](docs/module-22-strategy.md) – strategy reflection
- [`requirements.txt`](requirements.txt) – Python package requirements

## 10. Reproducing the analysis

The project requires Python 3 and the packages listed in `requirements.txt`.

Install the dependencies from the repository root:

```bash
pip install -r requirements.txt
```

Run the analysis for all eight functions:

```bash
python src/bbo_function_analysis.py --all
```

Run an individual function by providing its number, for example:

```bash
python src/bbo_function_analysis.py --function 3
```

Generated summaries, plots and recommendations are saved under `results/`.

The notebook can be opened using Jupyter Notebook, JupyterLab or Google Colab:

```bash
jupyter notebook notebooks/bbo_analysis.ipynb
```

All notebook cells should be run from beginning to end using the official data files.

## 11. Transparency, assumptions and limitations

The main assumptions of the implemented approach are:

- the observed data contains some learnable structure
- nearby inputs may sometimes produce related outputs
- Gaussian Process uncertainty is informative for candidate selection
- the observations are sufficient to fit a preliminary surrogate

Important limitations include:

- the number of observations is limited
- the hidden mathematical functions are unavailable
- some regions of the search spaces may be poorly represented
- higher-dimensional spaces are difficult to cover with limited observations
- the Gaussian Process may not accurately represent every hidden function
- acquisition-function recommendations remain unevaluated
- no guarantee of global optimality or convergence is provided

The [datasheet](docs/datasheet.md) documents data provenance, composition, intended uses and limitations. The [model card](docs/model-card.md) explains model design, intended use, assumptions, performance reporting and possible failure modes.

## 12. Ethical and responsible use

The dataset contains synthetic numerical observations and does not include personal or demographic information.

The real-world descriptions associated with the functions are illustrative. Generated recommendations must not be used directly for medical, industrial, educational or other high-stakes decisions.

The project is intended for educational demonstration of black-box optimisation, Bayesian reasoning and transparent machine-learning documentation.

## 13. Conclusion

This project demonstrates a complete workflow for analysing limited observations from eight hidden functions and producing evidence-based candidate queries.

The final approach combines:

- official observed data
- exploratory summaries and visualisations
- Gaussian Process surrogate modelling
- structured candidate generation
- comparison of three acquisition functions
- transparent separation of observations and predictions
- reproducible code and supporting documentation

The central lesson is that effective black-box optimisation requires both exploration and exploitation. A useful optimisation system must seek strong predicted outcomes while recognising uncertainty, limited evidence and the possibility that unexplored regions may contain better solutions.

