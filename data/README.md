# Official BBO starter data

This folder contains the official initial observations supplied in Mini-lesson
12.8: Data and descriptions of functions for Bayesian optimisation competition.

The project includes eight synthetic black-box maximisation functions. Each
function folder contains:

- `initial_inputs.npy` — official initial evaluated input points
- `initial_outputs.npy` — corresponding observed outputs

## Dataset structure

| Function | Input shape | Output shape | Optimisation goal |
|---:|---:|---:|---|
| 1 | `(10, 2)` | `(10,)` | Maximise |
| 2 | `(10, 2)` | `(10,)` | Maximise |
| 3 | `(15, 3)` | `(15,)` | Maximise |
| 4 | `(30, 4)` | `(30,)` | Maximise |
| 5 | `(20, 4)` | `(20,)` | Maximise |
| 6 | `(20, 5)` | `(20,)` | Maximise |
| 7 | `(30, 6)` | `(30,)` | Maximise |
| 8 | `(40, 8)` | `(40,)` | Maximise |

The observed values in this folder are genuine course-provided data.
Model-generated query recommendations are stored separately under `results/`
and must not be interpreted as evaluated hidden-function outputs.

No peer query history or peer-generated data is included.
