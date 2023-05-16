### Mathematical operators

```python
    func_mapper = {
    "/": lambda x, a: abs(x / a) if a > 0 else 0,
    "+": lambda x, a: abs(x + a),
    "*": lambda x, a: abs(x * a),
    "-": lambda x, a: abs(x - a),
}
```

##########################

### Reduce Sequences Operators

```python
from functools import reduce

operators = {
    "/": lambda x: reduce(lambda a, b: a // b, x),
    "+": lambda x: reduce(lambda a, b: a + b, x),
    "-": lambda x: reduce(lambda a, b: a - b, x),
    "*": lambda x: reduce(lambda a, b: a * b, x),
}
```