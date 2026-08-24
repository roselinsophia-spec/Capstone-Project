# Part 2: Model card for my BBO optimisation approach
# Model overview
        Model name: Iterative Heuristic BBO Strategy
        Version: Round 10 draft
        Type: sequential query-selection strategy for black-box optimisation
        Developer: [Roselin Sophia / roselinsophia-spec]

## Intended uses and limitations:

### This approach is intended for:
    - limited-query black-box optimisation
    - exploratory optimisation with incomplete knowledge
    - educational or prototype optimisation settings

### It should be avoided for:
    - high-confidence claims about global optimality
    - fully automated high-stakes optimisation without monitoring
    - settings that require exhaustive search or guaranteed convergence

### Inputs and outputs:
    Input: accumulated query history and returned outputs for each of the eight functions
    Output: the next proposed query point for each function

### Strategy details:
    - Across the ten rounds, the strategy evolved from broad exploration toward more selective local refinement.
    - Early rounds prioritised diversity and avoiding crowded regions.
    - Later rounds gave more weight to repeated strong outputs, local stability and uncertainty.
  
### Techniques considered include:
   - local or linear regression for trend estimation
   - threshold-based logistic reasoning for “good vs bad” regions
   - SVM-style boundary thinking for promising vs weak areas
   - possible future Bayesian optimisation reasoning

## Performance
Because the true optima are unknown, performance is summarised using:
    - best observed value per function so far
    - whether a given round improved on the previous best
    - search efficiency and consistency
    - qualitative stability across functions

## Assumptions, constraints and failure modes  
### Key assumptions:
    - local structure provides at least some useful signal
    - nearby strong points may justify refinement
    - unexplored regions may still matter

### Key constraints:
    - limited number of queries
    - delayed feedback
    - unknown function structure
    - uneven coverage of the search space
    
### Potential failure modes:
    - overfitting to local patterns
    - missing global structure
    - reinforcing early sampling bias
    - underestimating unexplored regions

## Ethical considerations and transparency:
### Transparency supports reproducibility because it allows others to see:
    - what data was used
    - how decisions were made
    - what assumptions shaped the search
    - where the approach may fail
This also supports adaptation in real-world settings, where optimisation methods should be documented clearly enough to critique, reuse and improve.

## Reflection:
    Creating both the datasheet and model card improved the clarity of my capstone project. 
    The datasheet helps explain what the dataset is, why it exists, how it was collected and where its gaps are. 
    The model card explains how the optimisation approach works, where it is useful, how it changed over rounds and what its limitations are. 
    Together, they make the project more transparent, reproducible and professionally presented.
