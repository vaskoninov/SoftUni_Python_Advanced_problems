import os
import string

punctuation = string.punctuation

## Finds the path to the file
file_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(file_path, "text.txt")
output_file = os.path.join(file_path, "output.txt")

## Opens the text.txt file and gathers the lines removing the "\n" (new lines)
with open(file, "r") as text:
    text_lines = [line.strip("\n") for line in text]

with open(output_file, "a") as out:
    for i, line in enumerate(text_lines, 1):
        letters = 0
        punct = 0
        for char in line:
            if char.isalpha():
                letters += 1
            if char in punctuation:
                punct += 1
        out.write(f"Line {i}: {line} ({letters})({punct})\n")
