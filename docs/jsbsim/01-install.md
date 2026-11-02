# Installing JSBSim

This guide covers installation on common platforms.

## Prerequisites

- **CMake 3.16+**
- **Python 3.8+**
- **Git**

## Building from Source

### Linux

```bash
git clone https://github.com/JSBSim/jsbsim.git
cd jsbsim
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

### macOS

```bash
git clone https://github.com/JSBSim/jsbsim.git
cd jsbsim
mkdir build && cd build
cmake ..
make -j$(sysctl -n hw.ncpu)
sudo make install
```

### Windows

```cmd
git clone https://github.com/JSBSim/jsbsim.git
cd jsbsim
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

## Verification

Test the installation with a simple flight:

```python
import jsbsim
from jsbsim import *

# Create a simple aircraft
aircraft = Aircraft()
aircraft.set_model("Cessna172.xml")

# Run a simple mission
mission = Mission()
mission.duration = 3600  # 1 hour
mission.run()
```

## Troubleshooting

### CMake configuration errors

Ensure you have:
- `libxml2-dev` (Linux)
- `libxml2` (macOS)
- `libxml` (Windows)

### Missing symbols

On Linux, ensure you installed:
```bash
sudo apt-get install libboost-all-dev libeigen3-dev libxml2-dev
```

## Next Steps

After installation, proceed to [creating your first aircraft model](../jsbsim/02-modeling.md).
