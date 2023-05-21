```python
def is_valid(n, m):
    if n in range(rows) and m in range(cols):
        return True
```

#######################################

```python
movements = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}
```

########################################

```python
movements_diagonals = {
    "u_l": (-1, -1),
    "l": (0, -1),
    "b_l": (1, -1),
    "u": (-1, 0),
    "b": (1, 0),
    "u_r": (-1, 1),
    "r": (0, 1),
    "b_r": (1, 1),
}
```

########################################

```python
flattened_matrix = [value for row in matrix for value in row]
```

########################################

```python
principal = 0
secondary = 0
n = len(matrix)
for i in range(n):
    principal += matrix[i][i]
    secondary += matrix[i][n - i - 1]
```

########################################

```python
chess_knight_movements = {
    "up_left": (-2, -1),
    "up_right": (-2, 1),
    "right_up": (-1, -2),
    "right_down": (1, -2),
    "left_up": (-1, 2),
    "left_down": (1, 2),
    "down_left": (2, -1),
    "down_right": (2, 1),
}
```