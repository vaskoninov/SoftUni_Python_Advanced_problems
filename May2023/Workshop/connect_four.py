##### Connect Four
import operator
from collections import deque


def place_circle():
    row = 0

    while row != ROWS and field[row][player_col] == 0:
        row += 1

    field[row - 1][player_col] = player_symbol
    return row - 1


def get_circles_count(row, col, dx, dy, operator_func):
    current_count = 0
    for i in range(1, 4):
        new_row = operator_func(row, dx * i)
        new_col = operator_func(col, dy * i)

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if field[new_row][new_col] != player_symbol:
            break

        current_count += 1

    return current_count


def check_for_win(row, col):
    for x, y in directions:
        counter = get_circles_count(row, col, x, y, operator.add) \
                  + get_circles_count(row, col, x, y, operator.sub) + 1

        if counter >= 4:
            return True
    return False


ROWS = 6
COLS = 7

field = [[0] * COLS for row in range(ROWS)]

players = deque([["Player One", "1"], ["Player Two", "2"]])
win = False

directions = (
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1),
)

while not win:
    print(*field, sep="\n")
    player, player_symbol = players[0]

    try:
        player_col = int(input(f"{player} please choose a column: ")) - 1
    except ValueError:
        print(f"You need to insert a valid integer in the range (1-{COLS})")
        continue

    if not 0 <= player_col <= COLS:
        print(f"You need to insert a valid integer in the range (1-{COLS})")
        continue

    if field[0][player_col] != 0:
        print(f"No empty space on that row. "
              f"You need to insert a valid integer in the range (1-{COLS})")
        continue

    row = place_circle()
    win = check_for_win(row, player_col)

    players.rotate()

print(f"{players[1][0]} wins")
