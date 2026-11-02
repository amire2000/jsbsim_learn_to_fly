# JSBSim Introduction

Start the implemented course with [Module 0 — Orientation](../00-orientation/index.md)
and [Module 1 — Fixed-wing language](../01-flight-language/index.md).
The introduction below is legacy reference material.

This course teaches you how to use **JSBSim**, a full physics-based flight dynamics and atmospheric simulation tool used in research, development, and education.

## What is JSBSim?

JSBSim is a C++ physics library that simulates the dynamics of aircraft in flight. It provides:

- **Aircraft model definitions** in XML format
- **Flight dynamics calculations** (lift, drag, thrust, moments)
- **Atmospheric modeling** (Standard Atmosphere, ISA variations)
- **Mission planning and simulation**
- **Interface with flight simulators** and other tools

## Getting Started

Before you begin, ensure you have:

1. **CMake 3.16+** - Build system
2. **Python 3.8+** - For scripting and analysis
3. **Git** - For version control

Clone the JSBSim repository:

```bash
git clone --branch v1.3.3 https://github.com/JSBSim-Team/jsbsim.git
cd jsbsim
cmake -S . -B build \
  -DCMAKE_INSTALL_PREFIX=/usr/local \
  -DBUILD_SHARED_LIBS=ON
cmake --build build -j
sudo cmake --install build
sudo ldconfig
```


You can also run an included simulation:
```bash
./build/src/JSBSim \
  --root=./ \
  --script=scripts/c1721.xml
```

## Course Structure

This course covers:

1. **Basics** - Installation and first flight
2. **Aircraft Modeling** - Creating your own aircraft models
3. **Mission Planning** - Designing flight scenarios
4. **Data Analysis** - Extracting and visualizing results
5. **Advanced Topics** - Customization and integration

Welcome to Learn to Fly!
