# First JSBSim run

Prerequisites: Python 3.11+, uv, and an internet connection for installation.
Run from the repository root:

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements-course.txt
.venv/bin/python examples/00-orientation/first-flight/run.py
```

If the course environment already exists, skip the first command.

Expected: the bundled script may print engine-event notifications, followed by
the JSBSim version, 10 simulated seconds, elapsed time, and a CSV path.
The CSV contains a header and 10 samples with position/attitude/command units
in the column names. Each run uses a new system temporary directory to preserve
earlier results; copy the CSV elsewhere if you want to retain it permanently.

Limitations: this is a scripted Cessna ground/takeoff sequence, not a trimmed
Mini Plank flight. The first ten seconds may remain near the runway. Script
events control the aircraft, so this is not a manual-control demo.
The assertions check finite values and elapsed simulated time, not flight fidelity.

