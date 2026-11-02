# Advanced Topics

Learn advanced JSBSim features and customization techniques.

## Custom Aerodynamics

Override default aerodynamic models with custom data:

```xml
<aerodynamics>
  <airfoils>
    <airfoil>
      <name>NACA0012</name>
      <chord>0.5</chord>
      <cL>
        <alpha>
          <deg>0</deg>
          <value>0.1</value>
        </alpha>
      </cL>
    </airfoil>
  </airfoils>
</aerodynamics>
```

## Custom Atmosphere

Define non-standard atmospheric profiles:

```python
import jsbsim
from jsbsim import *

# Create custom atmosphere
atmosphere = Atmosphere()
atmosphere.set_pressure(101325)  # Pa
atmosphere.set_temperature(288.15)  # K

# Use in mission
mission.set_atmosphere(atmosphere)
```

## Custom Control Surfaces

Modify control surface characteristics:

```xml
<flightControls>
  <surface>
    <name>Elevator</name>
    <max>0.1</max>  # Max deflection
    <min>-0.1</min>
  </surface>
</flightControls>
```

## Scripting Custom Logic

Use Python scripting for custom mission logic:

```python
import jsbsim
from jsbsim import *

def custom_control(t, aircraft):
    # Custom control logic based on time and state
    throttle = min(1.0, t / 3600)
    return {
        'throttle': throttle,
        'elevator': 0.0,
        'aileron': 0.0,
        'rudder': 0.0
    }

mission.set_control_callback(custom_control)
```

## Next Steps

Complete the course and [contribute](../jsbsim/06-contribute.md)!
