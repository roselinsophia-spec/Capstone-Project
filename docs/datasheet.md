#Part 1: Datasheet for the BBO capstone dataset

## Motivation:
        This dataset was created to support my black-box optimisation (BBO) capstone project. Its main purpose is to record the history of submitted query points and the corresponding returned function evaluations across eight unknown functions. The dataset supports an iterative optimisation task in which I refine my search strategy over multiple rounds under limited feedback. It fills a practical need in the project by giving me a traceable record of what I queried, what outputs I received and how my decisions evolved over time. The dataset was created and maintained by me as part of my coursework and capstone development.

## Composition:
The dataset contains:
    - function identifiers for the eight unknown functions
    - query points submitted each round
    - returned response values from the challenge system
    - round information and strategy notes where relevant
    
The dataset grows by one evaluated point per function in each round, so its size increases over time. Each instance is structured numeric data, where the query is stored in the challenge input format and linked to a returned function value. It is not a complete sample of the search space, but rather a strategic sample shaped by my optimisation choices. This means there are gaps: some regions are explored more heavily than others, and unexplored regions may still contain important behaviour.

## Collection process:
        The data was collected iteratively through the BBO capstone portal over successive modules. Queries were generated using an evolving optimisation strategy. Early rounds relied more on broad exploration and diversity. Later rounds used more local refinement and model-informed reasoning. The sampling process was therefore deterministic but strategy-dependent, not random. The collection timeframe is the duration of the capstone challenge. No human subjects are involved, so informed consent and demographic risks do not apply in the usual sense.

## Pre-processing / cleaning / labelling:
The raw returned values are preserved, and I may also maintain processed summaries such as:
    - grouping by function
    - tracking best-so-far values
    - recording round-by-round changes
    - annotating regions as promising, uncertain or weak
These transformations are intended to support interpretation, not to replace the raw records. No class labels are inherent in the original data, although threshold-based “good vs bad” labels may be created for analysis.

## Uses:
The intended uses are:
    - analysing optimisation behaviour across rounds
    - supporting reproducibility of query decisions
    - comparing heuristic or model-based search strategies
    - documenting the capstone process

## Inappropriate uses would include:
    - treating the data as a full representation of the true unknown functions
    - making strong claims about global optima from limited and biased samples
    - using threshold labels as if they were ground-truth classes rather than analysis tools

## Distribution
The dataset is distributed through my public GitHub repository for educational and documentation purposes. It is shared as part of the capstone project record. Any reuse should acknowledge that it was created in a limited-query black-box setting and may reflect sampling bias.

Maintenance
The dataset is maintained by me. Updates occur each round as new queries and returned outputs are added. Version control is handled through GitHub. The dataset may continue to be expanded until the capstone ends.
