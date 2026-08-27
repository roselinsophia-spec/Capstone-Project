## Function 5: Four-dimensional chemical-yield analogy

Function 5 accepts four inputs and is presented as analogous to maximising the
yield of a chemical process. The course description suggests a typically
unimodal landscape.

The official initial dataset contains 20 observations. The output distribution
is strongly uneven, with one observed value substantially larger than much of
the remaining dataset.

## Actual observed result:
Best observed input:
[0.224189023, 0.846480490, 0.879484180, 0.878515684]

Best observed output:
1088.859618196271

## Function-specific interpretation
Function 5 is strongly right-skewed. The maximum observed response is much
larger than the median and mean. This point should not be deleted as an outlier,
because it may represent the high-yield region the optimisation is intended to
find. The large scale difference makes output standardisation particularly
important.
