# Geometric Lib
The python library implements area and perimeter calculations for geometric shapes.

## Dependencies:
- math

## How to use

```bash
pip install geometric-lib
```

or

```python
import geometric_lib
```

## Modules
- **square.py** – functions for a **square** given side **a**
- **circle.py** – functions for a **circle** given radius **r**

## Functions with examples

### square.py

Takes the side length and returns the area of the square.

**Args:**

- a: float, side length

**Returns:**

- float: area of the square

```python
from square import area
area(3)
9
```

Takes the side length and returns the perimeter of the square.

**Args:**

- a: float, side length

**Returns:**

- float: perimeter of the square

```python
from square import perimeter
perimeter(3)
12
```

### circle.py

Takes the radius of a circle and returns its area.

**Args:**

- r: float, radius

**Returns:**

- float: area of the circle

```python
from circle import area
round(area(2), 3)
12.566
```

Takes the radius of a circle and returns its circumference

**Args:**

- r: float, radius

**Returns:**

- float: perimeter of the circle

```python
from circle import perimeter
round(perimeter(2), 3)
12.566
```

## History of changes

- 8ba9aeb — 2021-03-04 — L-03: Circle and square added
