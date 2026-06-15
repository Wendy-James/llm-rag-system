.PHONY: eval test all

eval:
	PYTHONPATH=src python3 scripts/run_experiment.py

test:
	PYTHONPATH=src python3 -m pytest -q

all: eval test
