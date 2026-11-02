# Aircraft Modeling

Learn how to create and configure aircraft models for JSBSim.

## Model Files

JSBSim aircraft models are XML files that define:

- **Aircraft geometry**
- **Mass properties** (mass, center of gravity, moments of inertia)
- **Aerodynamics** (airfoil data, drag polars, lift curves)
- **Propulsion** (engine characteristics, propeller settings)
- **Flight control surfaces**

## Basic Structure

A minimal aircraft model includes:

```xml
<?xml version="1.0"?>
<aircraft>
  <name>MyAircraft</name>
  <weight>1000.0</weight>
  <length>10.0</length>
  <width>4.0</width>
  <height>3.0</height>
  
  <mass>
    <mass>1000.0</mass>
    <cgX>0.5</cgX>
    <cgY>0.0</cgY>
    <cgZ>0.0</cgZ>
    <inertia>
      <ix>100.0</ix>
      <iy>100.0</iy>
      <iz>100.0</iz>
    </inertia>
  </mass>
  
  <aerodynamics>
    <!-- Airfoil and drag definitions -->
  </aerodynamics>
  
  <propulsion>
    <!-- Engine and propeller settings -->
  </propulsion>
  
  <flightControls>
    <!-- Control surface definitions -->
  </flightControls>
</aircraft>
```

## Common Aircraft Types

JSBSim includes models for:

- **Small aircraft**: Cessna 172, Piper Cub, Homebuilt
- **Military**: F-16, F/A-18, B-52
- **Transport**: Boeing 737, Airbus A320
- **Unmanned**: DJI Phantom, custom UAVs

## Custom Models

To create a custom aircraft model:

1. **Define geometry** from technical drawings
2. **Determine mass properties** through calculations or wind tunnel data
3. **Obtain aerodynamic data** from wind tunnel tests or CFD
4. **Configure propulsion** based on engine and propeller specifications

## Example: Simple Plane

See `examples/` directory for sample models.

## Next Steps

Proceed to [Mission Planning](../jsbsim/03-missions.md).
