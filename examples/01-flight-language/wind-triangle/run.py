"""Compare heading and track in a horizontal, zero-sideslip example."""
import math


def ground_motion(airspeed, heading_deg, wind_north, wind_east):
    """Return ground speed and track for wind components directed toward N/E."""
    if not all(math.isfinite(v) for v in
               (airspeed, heading_deg, wind_north, wind_east)) or airspeed < 0:
        raise ValueError("Inputs must be finite and airspeed nonnegative")
    heading = math.radians(heading_deg)
    north = airspeed * math.cos(heading) + wind_north
    east = airspeed * math.sin(heading) + wind_east
    speed = math.hypot(north, east)
    track = math.degrees(math.atan2(east, north)) % 360 if speed > 1e-12 else None
    return speed, track


def main():
    """Check known vectors and print three flight-language scenarios."""
    assert ground_motion(15, 0, 0, 0) == (15, 0)
    assert ground_motion(15, 0, -5, 0) == (10, 0)
    speed, track = ground_motion(15, 0, 0, 5)
    assert math.isclose(speed, math.sqrt(250))
    assert math.isclose(track, 18.43494882292201)
    assert ground_motion(15, 0, -15, 0) == (0, None)
    assert math.isclose(ground_motion(15, 90, 0, 0)[1], 90)
    for label, north, east in [("Calm", 0, 0), ("Headwind", -5, 0),
                                ("Crosswind", 0, 5)]:
        speed, track = ground_motion(15, 0, north, east)
        print(f"{label}: airspeed=15.00 m/s heading=0.00 deg "
              f"groundspeed={speed:.2f} m/s track={track:.2f} deg")


if __name__ == "__main__":
    main()

