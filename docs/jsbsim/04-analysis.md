# Data Analysis

Learn how to extract and analyze flight data from JSBSim simulations.

## Output Files

JSBSim generates several output formats:

1. **Binary (.bin)** - High-resolution state data
2. **Text (.txt)** - Human-readable log files
3. **CSV (.csv)** - Spreadsheet-ready data
4. **Plot files** - For visualization tools

## Reading Binary Data

```python
import jsbsim
from jsbsim import *

# Open binary file
f = jsbsim.DataFile("flight.bin")

# Read state data
for state in f:
    print(f"t={state.time:.1f} h={state.h:.1f} alt={state.alt:.1f}")
```

## CSV Export

JSBSim can export to CSV format:

```python
import jsbsim
from jsbsim import *

# Export to CSV
f = jsbsim.DataFile("flight.csv")
for state in f:
    print(f"{state.time},{state.h},{state.alt},{state.vx},{state.vy}")
```

## Visualization

### Using Matplotlib

```python
import matplotlib.pyplot as plt
import pandas as pd

# Read CSV data
df = pd.read_csv("flight.csv")

# Plot altitude vs time
plt.plot(df.time, df.alt)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Flight Altitude')
plt.grid(True)
plt.show()
```

### Using Plotly

```python
import plotly.graph_objects as go
import pandas as pd

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.time, y=df.alt, mode='lines+markers'))
fig.show()
```

## Performance Analysis

Extract key performance metrics:

```python
import numpy as np

# Calculate fuel consumption
fuel = []
for state in f:
    fuel.append(state.fuel)

fuel_consumption = fuel[-1] - fuel[0]
print(f"Fuel used: {fuel_consumption} kg")
```

## Next Steps

Proceed to [Advanced Topics](../jsbsim/05-advanced.md).
