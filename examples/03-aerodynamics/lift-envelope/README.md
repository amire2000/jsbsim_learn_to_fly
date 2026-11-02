# Dynamic pressure and lift demand

Prerequisites: course `.venv` from Module 0 with the existing
`requirements-course.txt` installed (Matplotlib is already included).
Read Module 1 and the Part 2 force-balance recap in Module 3.

From the repository root:

```bash
.venv/bin/python examples/03-aerodynamics/lift-envelope/check.py
.venv/bin/python examples/03-aerodynamics/lift-envelope/run.py
```

Expected output: `Lift-demand checks passed`, then
`15 m/s, 0.36 kg: q=137.81 Pa, W=3.5316 N, required CL=0.1971`.
The demo saves `examples/03-aerodynamics/lift-envelope/lift-envelope.png`
(overwriting its previous generated plot). It needs no display and opens no window.
The left panel shows pressure increasing with speed squared; the right panel
shows required CL decreasing with speed and increasing with mass.

Exercise: predict the effect of doubling `AREA`, change it from 0.13 to 0.26,
and rerun the demo. Required CL halves, while pressure is unchanged. Restore
it before running checks, which verify the documented baseline.

Limitations: constant assumed density, illustrative area and masses, steady
straight level flight, no bank, and no vertical thrust contribution. The code
calculates lift demand, not achieved lift, stall speed, trim, drag, propulsion,
or a JSBSim trajectory. No measured PW75 coefficients are supplied. The 5–25 m/s
plot range is a calculation range, not a validated flight envelope. Zero speed
is rejected because required CL divides by dynamic pressure.
