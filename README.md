# Black-Box Optimisation Capstone Project
## 1. Project overview
  This project documents my work on a black-box optimisation (BBO) capstone challenge. In this challenge, I must propose new query points for multiple unknown functions, receive evaluated outputs, and then refine my strategy over several rounds as more data becomes available.

  The overall goal of the BBO capstone project is to learn how to make better optimisation decisions under uncertainty. This is highly relevant in real-world machine learning because many important tasks behave like black-box problems. Examples include hyperparameter tuning, simulation-based optimisation, engineering design, and other settings where the objective function is unknown, expensive to evaluate, or too complex to model directly. The high-level idea is to use limited observations to decide where to sample next so that performance improves over time.

  This capstone project supports my current and future career goals by helping me strengthen skills in iterative modelling, optimisation, experiment tracking, uncertainty-aware decision making, and technical communication. It also reflects the type of thinking required in practical data science work, where complete information is rarely available at the start.

## 2. Inputs and outputs
For each unknown function, the input is a query point submitted in the required challenge format:
                x1-x2-x3-...-xn
Each coordinate:
    - starts with 0
    - is written to six decimal places
    - represents one dimension of the function input space

Example for a 2D function:
    0.123456-0.654321

The dimensionality varies by function, but the exact mathematical structure of each function is unknown. One new query point must be submitted for each function in every round. The output is the response value returned after the query is evaluated. This value acts as the performance signal that guides future decisions. Over time, the available dataset grows by one evaluated point per function in each module.

## 3. Challenge objectives
The objective of the challenge is to identify increasingly better query points for each of the unknown functions. In practical terms, the aim is to improve performance iteratively while learning about the hidden response surfaces.

The challenge includes several key constraints:
    - the true form of the functions is unknown
    - the number of queries is limited
    - only one new point per function can be submitted in each round
    - feedback is delayed until the next round
    - decisions must be made using incomplete and evolving information

The project is therefore not just about chasing the current best value. It is about building a strategy that uses each limited query as effectively as possible.

## 4. Technical approach
My strategy across the first three query rounds has gradually evolved from broad exploration toward a more balanced and evidence-based approach.

In the first round, I relied mainly on:
    - sample diversity
    - avoiding already crowded regions
    - cautious exploratory moves because very little was known

In the second round, I began using the observed outputs more directly by looking for:
    - locally promising regions
    - repeated stronger values
    - signs of smoother versus unstable behaviour

By the third round, my approach became more selective and informed by the growing dataset. I still use heuristics, but they are now increasingly guided by prior results rather than broad intuition alone.

A central part of my strategy is balancing exploration and exploitation:
    - exploration means sampling uncertain or weakly explored regions
    - exploitation means querying near regions that already appear promising
If nearby points show relatively strong and consistent outputs, I lean toward exploitation. If the evidence is sparse, noisy, or contradictory, I prioritise exploration so that I can learn more before committing too strongly.

At this stage, I am not relying on one fixed formal model for all functions, but I am considering how different methods could support decision-making:
    - linear or local regression for rough trend estimation in smoother regions
    - logistic regression or threshold-based classification to separate stronger and weaker regions
    - SVMs, especially soft-margin and kernel SVMs, to classify promising versus weak regions when boundaries may be non-linear

later, potentially more advanced surrogate-style approaches such as Bayesian optimisation reasoning

What makes my approach thoughtful is that I treat the challenge as both an optimisation problem and a learning problem. I am not only trying to improve the next query result, but also trying to make each query informative enough to improve future rounds. This README is intended to be a living document that I will continue updating as my strategy evolves throughout the capstone project.

## 5. Transparency and documentation
This repository also includes supporting documentation to improve transparency, reproducibility, and interpretability:
    - [Datasheet](docs/datasheet.md) - documents the query history and function evaluation dataset, including motivation, composition, collection process, intended uses, distribution, and maintenance.
    - [Model Card](docs/model-card.md) - documents the optimisation approach, intended uses, assumptions, limitations, strategy evolution, and transparency considerations.

