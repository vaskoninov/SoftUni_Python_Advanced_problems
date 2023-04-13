import sys
from io import StringIO

test = "hello world"

sys.io = StringIO(test)

print(test)
