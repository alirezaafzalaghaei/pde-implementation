
# Finite Difference Methods for Partial Differential Equations

This repo implements basic finite difference methods for solving Partial Differential Equations (PDEs). Examples are taken from this book:

> Smith, G.D., Smith, G.D. and Smith, G.D.S., 1985. Numerical solution of partial differential equations: finite difference methods. Oxford university press.

## Requirements

- Python
- Numpy
- Matplotlib
- Seaborn
- Tabulate

## Details
- Each notebook contains an example (or part of it) based on the book structure.
- Two different animated plots have been drawn for each example.
- Both simple and vectorized implementations are available for each example.

## Notebooks
- `Example 2.1`: Explicit discretization with various step sizes:
	- Case 1: `r = 0.1`
	- Case 2: `r = 0.5`
	- Case 3: `r = 1.0`
- `Example 2.2`: Crank-Nicolson implicit discretization.
- `Example 2.3`: Explicit discretization with Neumann boundary conditions (Central Difference).
- `Example 2.4`: Explicit discretization with Neumann boundary conditions (Forward Difference).
- `Example 2.5`: Crank-Nicolson discretization with Neumann boundary conditions.
