## Function 1: Two-dimensional sparse-response optimisation

Function 1 accepts two continuous inputs and is presented as analogous to
detecting contamination sources in a two-dimensional area. A meaningful
response may occur only when a query is sufficiently close to a source. This
can create an extremely sparse and uneven output landscape.

The official initial dataset contains 10 observations. Because the inputs are
two-dimensional, the observed points and Gaussian Process acquisition surface
can be visualised directly. The optimisation objective is to maximise the
returned output.

## Actual observed Result:
Best observed input:
[0.731023631, 0.732999876]

Best observed output:
7.710875114502849e-16

## Function-specific interpretation
Function 1 has a highly sparse observed response. The current maximum is very
close to zero, while one observation is substantially negative relative to the
others. This makes modelling sensitive to output scaling and kernel assumptions.
Uncertainty is therefore particularly important when recommending another query.
