## Function 8: Eight-dimensional complex-system optimisation

Function 8 accepts eight continuous inputs and is the highest-dimensional
function in the project. It is presented as analogous to tuning a complex system
or an ML model with several interacting parameters.

The official initial dataset contains 40 observations. Although this is the
largest dataset in the project, it is still extremely sparse relative to an
eight-dimensional continuous search space.

## Actual observed result
Best observed input:
[0.056447411, 0.065955553, 0.022928678, 0.038786472,
 0.403935441, 0.801055329, 0.488307007, 0.893084977]

Best observed output:
9.598482002566342

## Function-specific interpretation
Function 8 has the highest dimensionality. Even 40 initial observations provide
limited coverage of an eight-dimensional domain. The predicted optimum is
therefore particularly sensitive to the kernel, candidate sample and random
seed. A proposed point should be treated as an informed recommendation, not a
verified optimum.
