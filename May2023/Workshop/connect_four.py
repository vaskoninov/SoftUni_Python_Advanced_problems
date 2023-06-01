##### Connect Four
import operator
from collections import deque

from colorama import Fore


def print_board():
    print(*field, sep="\n")


def place_circle():
    row = 0

    while row != ROWS and field[row][player_col] == "0":
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
    if counter_for_draw == ROWS * COLS:
        print("Draw!")
        print_board()
        return
    return False


ROWS = 6
COLS = 7

counter_for_draw = 0

field = [["0"] * COLS for row in range(ROWS)]

player_one_symbol = "1"
player_two_symbol = "2"

players = deque([[Fore.BLUE + "Player One" + Fore.RESET, player_one_symbol],
                 [Fore.RED + "Player Two" + Fore.RESET, player_two_symbol]])
win = False

directions = (
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1),
)

while not win:
    print_board()
    player, player_symbol = players[0]

    try:
        player_col = int(input(f"{player} please choose a column: ")) - 1
    except ValueError:
        print(Fore.RED + f"You need to insert a valid integer in the range (1-{COLS})" + Fore.RESET)
        continue

    if not 0 <= player_col <= COLS:
        print(Fore.RED + f"You need to insert a valid integer in the range (1-{COLS})" + Fore.RESET)
        continue

    if field[0][player_col] != "0":
        print(Fore.RED + f"No empty space on that row. "
                         f"You need to insert a valid integer in the range (1-{COLS})" + Fore.RESET)
        continue

    row = place_circle()
    counter_for_draw += 1
    win = check_for_win(row, player_col)

    players.rotate()

print(f"{players[1][0]} wins")
