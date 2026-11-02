# Modules 0 and 1: orientation and flight vocabulary

Created: 2026-11-02

Status: Implemented and verified

Description: Introduce a Python-proficient aviation beginner to the simulation
boundary and the terms needed to read aircraft telemetry.

## Decisions

- Module 0 runs a bundled Cessna script, records a short finite state trace,
  and separates simulated time from elapsed execution time.
- Module 1 uses an analytic wind-vector exercise, with assertions, to separate
  airspeed, heading, ground speed, and track without assuming aircraft physics.
- Each module is one complete introductory lesson with five shared quizzes.
- Fix shared quiz feedback once and retain the existing lesson URLs as signposts.
- Use a course virtual environment with pinned dependencies for repeatable setup.

## Related material

- [Syllabus](../../docs/syllabus.md)
- [Module 0](../../docs/modules/00-orientation/index.md)
- [Module 1](../../docs/modules/01-flight-language/index.md)
- [Orientation demo](../../examples/00-orientation/first-flight/README.md)
- [Wind demo](../../examples/01-flight-language/wind-triangle/README.md)
