import sys
from io import StringIO

test = "hello world"

sys.stdin = StringIO(test)

print(test)
