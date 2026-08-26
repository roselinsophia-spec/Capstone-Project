# Black-Box Optimisation Capstone Project

## Non-technical explanation

This project explores how to make better decisions when working with a system whose internal rules are hidden. Over multiple rounds, I submitted candidate inputs to eight unknown functions and used the returned outputs to gradually learn which regions of the search space were more promising. My goal was to improve performance step by step by balancing exploration of uncertain areas with refinement of stronger regions. This reflects many real-world machine learning problems, such as hyperparameter tuning and simulation-based optimisation, where you cannot inspect the full mechanism directly and must rely on evidence from previous trials to guide the next decision.

## 1. Project overview

This repository documents my work on a **black-box optimisation (BBO) capstone challenge**. In this challenge, I propose new query points for multiple unknown functions, receive evaluated outputs, and refine my strategy over repeated rounds as more data becomes available.

The overall goal of the BBO capstone project is to learn how to make **better optimisation decisions under uncertainty**. This is highly relevant in real-world machine learning because many important tasks behave like black-box problems. Examples include:
- hyperparameter tuning
- simulation-based optimisation
- engineering design
- expensive evaluation problems where the true objective function is unknown or too complex to model directly

This capstone project supports my professional development by helping me strengthen skills in:
- iterative modelling
- optimisation
- experiment tracking
- uncertainty-aware decision making
- technical communication

## Data

This project uses the **query history and returned function evaluations** from the course Black-Box Optimisation (BBO) capstone challenge. The challenge is based on the **NeurIPS 2020 Black-Box Optimisation competition context**, where participants iteratively propose query points for several unknown functions and receive only the resulting outputs.

In this capstone, I worked with **eight unknown functions**, each with a fixed input dimensionality, and the dataset grew over time as one new evaluated point per function was added in each round.

The data consists of:
- submitted query points for each function
- returned response values from the challenge system
- round-by-round optimisation history

Because this is an iterative challenge rather than a standard static dataset, the core data is generated through the optimisation process itself. Any large supporting files should be linked externally rather than stored directly in the repository.

## 2. Inputs and outputs

For each unknown function, the input is a **query point** submitted in the required challenge format:

`x1-x2-x3-...-xn`

Each coordinate:
- starts with `0`
- is written to **six decimal places**
- represents one dimension of the function input space

Example for a 2D function:

`0.123456-0.654321`

The dimensionality varies by function, but the exact mathematical structure of each function is unknown.

The output is the **response value** returned after the query is evaluated. This value acts as the performance signal that guides future decisions. Over time, the available dataset grows by one evaluated point per function in each module.

## 3. Challenge objectives

The objective of the challenge is to identify **increasingly better query points** for each of the unknown functions. In practical terms, the aim is to improve performance iteratively while learning about the hidden response surfaces.

The challenge includes several key constraints:
- the true form of the functions is unknown
- the number of queries is limited
- only one new point per function can be submitted in each round
- feedback is delayed until the next round
- decisions must be made using incomplete and evolving information

The project is therefore not just about chasing the current best value. It is about building a strategy that uses each limited query as effectively as possible.

## Model

This project does not rely on a single fixed predictive model. Instead, it uses an **iterative black-box optimisation strategy** to choose new query points for eight unknown functions.

Over the course of the capstone, I mainly used:
- evidence-based local refinement
- exploratory search heuristics
- ideas from surrogate modelling such as:
  - local or linear regression
  - threshold-based classification
  - SVM-style boundary thinking

The goal was not to fully reconstruct the hidden functions, but to use the available evaluations to identify increasingly promising regions of the search space.

## Hyperparameter Optimisation

A central part of the project was deciding how strongly to favour **exploration** versus **exploitation**.

In practice, the main hyperparameters of my strategy were the rules that controlled:
- how widely I explored uncertain regions
- how aggressively I refined locally promising areas
- how much trust I placed in neighbourhood patterns versus isolated strong points

Early rounds favoured broader exploration because the search space was poorly understood. Later rounds became more selective, with greater emphasis on stable local structure and repeated strong performance. This made the optimisation process more evidence-based and reduced the risk of overcommitting too early to misleading patterns.

## 4. Technical approach

My strategy across the capstone evolved from **broad exploration** toward a more balanced and evidence-based approach.

In the first round, I relied mainly on:
- sample diversity
- avoiding already crowded regions
- cautious exploratory moves because very little was known

In later rounds, I began using the observed outputs more directly by looking for:
- locally promising regions
- repeated stronger values
- signs of smoother versus unstable behaviour
- neighbourhood patterns rather than isolated strong points

A central part of my strategy is balancing **exploration** and **exploitation**:
- **exploration** means sampling uncertain or weakly explored regions
- **exploitation** means querying near regions that already appear promising

If nearby points show relatively strong and consistent outputs, I lean toward exploitation. If the evidence is sparse, noisy or contradictory, I prioritise exploration so that I can learn more before committing too strongly.

At different stages, I considered how the following methods could support decision-making:
- linear or local regression for rough trend estimation in smoother regions
- logistic regression or threshold-based classification to separate stronger and weaker regions
- SVMs, especially soft-margin and kernel SVMs, to classify promising versus weak regions when boundaries may be non-linear
- more advanced surrogate-style approaches such as Bayesian optimisation reasoning

What makes this approach useful is that I treat the challenge as both an **optimisation problem** and a **learning problem**. I am not only trying to improve the next query result, but also trying to make each query informative enough to improve future rounds.

## Results

The main result of the project was an increasingly refined **query strategy** across multiple rounds of black-box optimisation.

Over time, I identified that:
- some functions responded well to **local refinement**
- others required more persistent **exploration**
- the strongest decisions usually came from **clusters of nearby strong points**, not isolated outliers

The most important lessons from the results were:
- neighbourhood structure often matters more than one strong point
- repeated local evidence is more reliable than isolated success
- optimisation under uncertainty benefits from balancing exploration and exploitation carefully
- adapting the strategy as more evidence becomes available is more effective than using one fixed rule throughout

## Repository contents

- `docs/datasheet.md` - dataset documentation
- `docs/model-card.md` - model documentation
- `docs/README.md` - documentation overview
- `notebooks/` or `src/` - analysis code, experiments, or helper scripts
- `results/` - summaries, observations, and supporting materials where applicable

## 5. Transparency and documentation

This repository includes supporting documentation to improve transparency, reproducibility and interpretability:

- [Datasheet](docs/datasheet.md) - documents the query history and function evaluation dataset, including motivation, composition, collection process, intended uses, distribution and maintenance
- [Model Card](docs/model-card.md) - documents the optimisation approach, intended uses, assumptions, limitations, strategy evolution and transparency considerations

This README is intended to be a living document and may continue to be updated to reflect further refinements, insights and supporting materials.
