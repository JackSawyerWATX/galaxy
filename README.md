# Galaxy Visualization

A 3D spiral galaxy visualization created with Python, NumPy, and PyVista.

## What It Is

This project renders an interactive 3D visualization of a spiral galaxy with:
- **3,000 white particles** arranged in a logarithmic spiral pattern
- **A yellow sphere** at the center (representing a central mass/black hole)
- **Black background** for contrast
- **Fully interactive 3D view** (rotate, zoom, pan with mouse)

## How It Works

The visualization generates a spiral galaxy using mathematical principles:

1. **Theta Generation**: Creates 3,000 random angles from 0 to 4π radians
2. **Radial Distance**: Calculates radius proportional to theta (`r = theta * 0.2`) to form a logarithmic spiral
3. **Cartesian Coordinates**: Converts polar coordinates to 3D:
   - `x = r * cos(theta)` 
   - `y = r * sin(theta)`
   - `z = random` (adds vertical scatter)
4. **Rendering**: Uses PyVista to create an interactive 3D plot with particle mesh and central sphere

## Requirements

- Python 3.8+
- NumPy
- PyVista

## Installation

Install dependencies:

```powershell
pip install numpy pyvista
```

## Running

Execute from the console:

```powershell
py galaxy.py
```

Or:

```powershell
python galaxy.py
```

An interactive 3D window will open displaying the spiral galaxy. You can:
- **Rotate**: Click and drag with mouse
- **Zoom**: Scroll wheel
- **Pan**: Right-click and drag

Close the window to exit the program.

## Files

- `galaxy.py` - Main visualization script
- `README.md` - This file
