# Wind triangle

Prerequisites: the course .venv from Module 0. Standard library only.
Run from the repository root:

```bash
.venv/bin/python examples/01-flight-language/wind-triangle/run.py
```

Expected ground speeds and tracks: calm 15.00 m/s and 0.00 degrees,
headwind 10.00 m/s and 0.00 degrees, crosswind 15.81 m/s and 18.43 degrees.
Embedded assertions also check eastward heading and zero ground speed
(where track is undefined). No files are written.

Exercise: change the crosswind's east component to -5 and predict the new
track before running again.

Limitations: horizontal vector arithmetic, zero sideslip, constant airspeed,
and specified wind. This is not a JSBSim aircraft model or control law.
Wind components describe where air travels toward, not weather-report
directions describing where wind comes from.

