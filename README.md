# MCP Student Sandbox

This repository contains small Python exercises focused on debugging, refactoring, and basic security awareness.

## mystery_module.py Overview

The file [mystery_module.py](mystery_module.py) currently defines a single function:

- `fn_x(a, b, c)`

### What It Does

`fn_x(a, b, c)` solves a quadratic equation in the form:

$$
ax^2 + bx + c = 0
$$

It calculates the discriminant:

$$
d = b^2 - 4ac
$$

Then:

- If `d < 0`, it returns `None` (no real roots).
- If `d >= 0`, it returns a tuple with two real roots:
  - `(-b + sqrt(d)) / (2a)`
  - `(-b - sqrt(d)) / (2a)`

### Function Signature

```python
def fn_x(a, b, c):
```

### Return Behavior

- `tuple[float, float]` when real roots exist
- `None` when the equation has no real roots

### Example

```python
from mystery_module import fn_x

print(fn_x(1, -3, 2))  # (2.0, 1.0)
print(fn_x(1, 0, 1))   # None (no real roots)
```

## Notes

- The current implementation assumes `a != 0`.
- If `a == 0`, division by zero may occur because the formula divides by `2 * a`.
- Function naming (`fn_x`) is not descriptive; a clearer name (for example, `solve_quadratic`) would improve readability.
