# Patterns from past queries and how they shaped this round
Across the first ten rounds, the clearest pattern has been that some functions respond well to local refinement, while others remain noisy or weakly structured and require broader exploration. In particular, when a function showed repeated stronger values from nearby queries, that became a signal that the region might contain a useful local basin. For those functions, my current choices were influenced by the pattern of stable local improvement, so I made smaller moves around those areas rather than jumping far away.
A second pattern was that some functions did not reward repeated fine-tuning in one place. In those cases, past rounds suggested that the apparent signal was either weak or unstable, so I used a more exploratory move this round. That means my choices were not uniform across all eight functions - they depended on whether the function had previously behaved like a stable region, a drifting region or a noisy region.

# Clusters or recurring regions in the search space
Yes, I do think some recurring regions have started to look like local clusters of promising behaviour. I am not claiming these are true global optima, but some functions now appear to have groups of nearby points with consistently better outputs than surrounding regions. Those clusters matter because they suggest that the search space may contain areas where local continuity is informative.
At the same time, not every function shows a clean cluster. For some, the query history still looks scattered, with no strong evidence that the higher-performing points form a stable group. In those cases, the absence of a clear cluster is itself informative: it suggests either high irregularity, sparse sampling or that I have not yet explored the right subspace.

# Less effective strategies and how I am adjusting
One less effective strategy has been over-refining weak local signals. In earlier rounds, if I saw a slightly better point, I sometimes treated that as a stronger indicator than it really was. With more rounds completed, I now see that not every local improvement deserves repeated exploitation. Another less effective tendency has been spreading attention too evenly across all directions in functions that now appear to have more important dimensions than others.
To adjust for this, I am becoming more selective. If a region has not shown stable follow-up improvement, I treat it more cautiously. If a function shows repeated local strength, I refine it. If it does not, I widen the search. So the adjustment is not simply “explore more” or “exploit more,” but to match the search style more carefully to the observed pattern.

# How this parallels clustering
My refinement process parallels clustering because I am effectively trying to separate meaningful local structure from noise. In clustering, the goal is often to identify groups of related points and avoid overreacting to isolated outliers. In this optimisation setting, I am doing something similar: nearby stronger points can be treated like a local cluster, while isolated good-looking points may be more like outliers until confirmed by neighbouring evidence.
Distance and similarity also matter in the same way they do in clustering. I am paying attention to whether high-performing points are close together in the search space, whether they suggest a local centroid or whether they sit on a boundary where the structure is still unclear. That clustering-style thinking helps me decide whether to tighten around a region or treat it as too uncertain.

# Expected visual patterns and how they guide next actions
If I plotted the query history and outputs, I would expect to see:
    - a few functions with tightening local groups around stronger outputs
    - some functions with scattered points and no obvious grouping
    - possible boundary regions where performance changes quickly over small distances
Those visual groupings would guide future action directly. Tight local clusters would support cautious exploitation and local refinement. Scattered patterns with no grouping would support broader exploration. Boundary-like transitions would suggest that sampling just around the edge of the current cluster may be more informative than sampling in its exact centre.

Overall, this clustering lens helped me become more disciplined: instead of reacting only to the best single point, I looked for groups, consistency and neighbourhood structure before deciding how to query next.
