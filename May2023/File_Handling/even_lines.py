import os

chars = {"-", ",", ".", "!", "?"}

## Finds the path to the file
file_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(file_path, "text.txt")

## Opens the text.txt file and gathers the lines removing the "\n" (new lines)
with open(file, "r") as text:
    text_lines = [line.strip("\n") for line in text]

new_lines = []

## Replaces all characters in chars with "@" and then append a list of the
## transformed line to a new collection
for i, line in enumerate(text_lines):
    for c in line:
        if c in chars:
            line = line.replace(c, "@")
    if i % 2 == 0:
        new_lines.append(line.split())

## Prints the Even Lines reversed
for new_line in new_lines:
    print(" ".join(new_line[::-1]))
