"""Run ten simulated seconds of the bundled Cessna takeoff script."""
import csv
import math
import tempfile
import time
from pathlib import Path

import jsbsim

DURATION_S = 10
HZ = 120


def main():
    """Run the baseline and record one telemetry sample per simulated second."""
    root = Path(jsbsim.get_default_root_dir())
    output = Path(tempfile.mkdtemp(prefix="jsbsim-module0-"))
    fdm = jsbsim.FGFDMExec(str(root))
    fdm.set_debug_level(0)
    fdm.set_output_path(str(output))
    if not fdm.load_script(str(root / "scripts/c1723.xml")):
        raise RuntimeError("Bundled Cessna script failed to load")
    fdm.set_dt(1 / HZ)
    if not fdm.run_ic():
        raise RuntimeError("Initial conditions failed")
    fdm.disable_output()
    properties = {
        "altitude_m": ("position/h-sl-ft", 0.3048),
        "airspeed_m_s": ("velocities/vtrue-fps", 0.3048),
        "roll_deg": ("attitude/phi-rad", 180 / math.pi),
        "pitch_deg": ("attitude/theta-rad", 180 / math.pi),
        "heading_deg": ("attitude/psi-rad", 180 / math.pi),
        "throttle_cmd": ("fcs/throttle-cmd-norm", 1),
        "elevator_cmd": ("fcs/elevator-cmd-norm", 1),
        "aileron_cmd": ("fcs/aileron-cmd-norm", 1),
    }
    start = time.perf_counter()
    with (output / "telemetry.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["time_s", *properties])
        for step in range(DURATION_S * HZ):
            if not fdm.run():
                raise RuntimeError(f"Simulation stopped at step {step}")
            values = [fdm[name] * scale for name, scale in properties.values()]
            assert all(math.isfinite(value) for value in values)
            if (step + 1) % HZ == 0:
                writer.writerow([fdm.get_sim_time(), *values])
    assert math.isclose(fdm.get_sim_time(), DURATION_S, abs_tol=1e-8)
    print(f"JSBSim {jsbsim.__version__}: {DURATION_S} simulated seconds")
    print(f"Wall-clock seconds: {time.perf_counter() - start:.3f}")
    print(f"CSV: {output / 'telemetry.csv'}")


if __name__ == "__main__":
    main()

