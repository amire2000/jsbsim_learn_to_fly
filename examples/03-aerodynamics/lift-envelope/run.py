"""Plot illustrative dynamic pressure and steady-level-flight lift demand."""
import math
from pathlib import Path

RHO = 1.225  # Assumed constant air density, kg/m³.
AREA = 0.13  # Assumed reference wing area, m², not a measured Mini Plank value.
GRAVITY = 9.81  # m/s²
MASSES = (0.30, 0.36, 0.40)  # kg


def lift_requirement(speed, mass, area=AREA, density=RHO):
    """Return dynamic pressure (Pa) and required CL for steady level flight in SI."""
    if not all(math.isfinite(value) and value > 0
               for value in (speed, mass, area, density)):
        raise ValueError("Speed, mass, area, and density must be finite and positive")
    pressure = 0.5 * density * speed**2
    coefficient = mass * GRAVITY / (pressure * area)
    return pressure, coefficient


def main():
    """Save two plots and print the reference calculation without opening a window."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    speeds = list(range(5, 26))
    figure, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    axes[0].plot(speeds, [lift_requirement(v, MASSES[0])[0] for v in speeds])
    axes[0].set(ylabel="Dynamic pressure q (Pa)", title="Same airflow for every mass")
    for mass in MASSES:
        coefficients = [lift_requirement(v, mass)[1] for v in speeds]
        axes[1].plot(speeds, coefficients, label=f"{mass:.2f} kg")
    axes[1].set(ylabel="Required lift coefficient CL (dimensionless)",
                title="Demand only: achievable CL is unknown")
    axes[1].legend()
    for axis in axes:
        axis.set_xlabel("True airspeed (m/s)")
        axis.grid(True, alpha=0.3)
    figure.suptitle(f"Illustrative level flight: density {RHO} kg/m³, area {AREA} m²")
    output = Path(__file__).with_name("lift-envelope.png")
    figure.savefig(output, dpi=150)
    plt.close(figure)
    pressure, coefficient = lift_requirement(15, 0.36)
    print(f"15 m/s, 0.36 kg: q={pressure:.2f} Pa, W={0.36 * GRAVITY:.4f} N, "
          f"required CL={coefficient:.4f}")
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
