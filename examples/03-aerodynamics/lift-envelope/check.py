"""Check the level-flight calculation against known values and scaling laws."""
import math

from run import lift_requirement


def main():
    """Verify a worked value, independent parameter changes, and rejected inputs."""
    pressure, coefficient = lift_requirement(15, 0.36)
    assert math.isclose(pressure, 137.8125)
    assert math.isclose(coefficient, 3.5316 / (137.8125 * 0.13))
    fast_pressure, fast_coefficient = lift_requirement(30, 0.36)
    assert math.isclose(fast_pressure, 4 * pressure)
    assert math.isclose(fast_coefficient, coefficient / 4)
    assert math.isclose(lift_requirement(15, 0.72)[1], 2 * coefficient)
    assert math.isclose(lift_requirement(15, 0.36, area=0.26)[1], coefficient / 2)
    thin_pressure, thin_coefficient = lift_requirement(15, 0.36, density=0.6125)
    assert math.isclose(thin_pressure, pressure / 2)
    assert math.isclose(thin_coefficient, 2 * coefficient)
    for index in range(4):
        for invalid in (0, -1, math.nan, math.inf, -math.inf):
            values = [15, 0.36, 0.13, 1.225]
            values[index] = invalid
            try:
                lift_requirement(*values)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Accepted invalid input: {values}")
    print("Lift-demand checks passed")


if __name__ == "__main__":
    main()
