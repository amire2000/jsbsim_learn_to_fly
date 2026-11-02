# JSBSim Learn to Fly

## Domain model

This course teaches fixed-wing flight dynamics by building a simulation of a
small tailless plank aircraft, using the Flightory Mini Plank as the physical
reference airframe.

- **Airframe**: the physical aircraft geometry, mass, center of gravity,
  inertia, propulsion, control surfaces, and aerodynamic data.
- **Flight dynamics model (FDM)**: JSBSim's 6-DOF physics simulation. It is the
  authority for forces, moments, motion, and simulated aircraft state.
- **Aircraft model**: the JSBSim XML description of an airframe and its
  subsystems. It is not the same thing as the Godot visual mesh.
- **Flight-control system**: the mapping from pilot or controller commands to
  actuator commands, including elevon mixing on a tailless aircraft.
- **Simulation coordinator**: Python code that initializes JSBSim, advances its
  fixed time step, applies inputs, records state, and sends render state.
- **Renderer**: Godot 4. It displays state received from the coordinator and
  does not calculate the aircraft's flight physics.
- **Ground truth**: the ideal state produced by JSBSim, used to validate plots,
  sensor models, and estimates. It is not automatically the same as a real
  aircraft sensor measurement.
- **Reference airframe**: the Mini Plank data supplied by Flightory. Published
  dimensions and performance are initial assumptions to be measured,
  parameterized, and challenged during the course.
