# Run Commands

## Run experiment

```bash
make test
```

or run the experiment script directly:

```bash
python scripts/run_experiment.py
```

## Tests

```bash
pytest -q
```

## Important outputs

- `experiments/retrieval_metrics.csv`
- `experiments/chunk_size_ablation.csv`
- `badcases/error_analysis.csv`
- `experiments/baseline/metrics.csv`
- `experiments/baseline/metrics.json`
