# Mission Planning

Learn how to create and execute flight missions in JSBSim.

## What is a Mission?

A JSBSim mission is a sequence of events that define:

- **Time and position** of the aircraft
- **Control inputs** (throttle, elevator, aileron, rudder)
- **Atmospheric conditions** (wind, temperature, pressure)
- **Events** (waypoints, takeoff, landing)

## Mission Types

1. **Fixed-point missions** - Aircraft visits predefined locations
2. **Waypoint missions** - Follow a route with navigation
3. **Time-based missions** - Simulate flight over a duration
4. **Custom missions** - Any combination of the above

## Basic Mission Structure

```xml
<mission>
  <description>Simple flight test</description>
  
  <time>
    <unit>sec</unit>
    <value>3600</value>
  </time>
  
  <waypoints>
    <waypoint>
      <longitude>180.0</longitude>
      <latitude>40.0</latitude>
      <altitude>100.0</altitude>
      <time>0.0</time>
    </waypoint>
  </waypoints>
  
  <controls>
    <throttle>1.0</throttle>
    <elevator>0.0</elevator>
    <aileron>0.0</aileron>
    <rudder>0.0</rudder>
  </controls>
</mission>
```

## Running a Mission

```python
import jsbsim
from jsbsim import *

# Create aircraft
aircraft = Aircraft()
aircraft.set_model("Cessna172.xml")

# Create mission
mission = Mission()
mission.set_time(3600)  # 1 hour

# Run mission
mission.run(aircraft)

# Access results
for state in mission.states:
    print(f"t={state.time:.1f} h={state.h:.1f} alt={state.alt:.1f}")
```

## Mission Analysis

JSBSim provides tools to analyze mission results:

- **Flight path** - 3D trajectory
- **Performance** - Fuel consumption, speed, altitude
- **Control history** - Input vs response
- **Aerodynamics** - Coefficients over time

## Tips

- Start with simple, fixed-point missions
- Use `MissionTester` to validate mission files
- Monitor fuel and battery during long missions
- Use `logFile` for detailed output

## Next Steps

Proceed to [Data Analysis](../jsbsim/04-analysis.md).
