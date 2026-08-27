## Function 2: Noisy two-dimensional optimisation

Function 2 accepts two inputs and is presented as analogous to maximising a
noisy machine-learning log-likelihood. The course description indicates that
the response may contain multiple local optima, meaning that local exploitation
alone may miss a stronger region.

The official initial dataset contains 10 observations. Its two-dimensional
structure allows direct visual comparison of observed values, predicted mean,
uncertainty and acquisition scores.

## Actual Observed Result:
Best observed input:
[0.702636557, 0.926564198]

Best observed output:
0.6112052157614438

## Function-specific interpretation:
Function 2 has a broader and more regular observed output range than Function 1.
The current best observation lies toward the upper part of the sampled domain.
However, only 10 observations are available, so the apparent regional pattern
should not be interpreted as proof of a global maximum.
