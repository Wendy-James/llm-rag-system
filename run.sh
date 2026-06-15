#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src python3 scripts/run_experiment.py
PYTHONPATH=src python3 -m pytest -q
