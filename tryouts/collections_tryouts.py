# name = "Barbara"
# c = Counter(name.lower())
# print(c)
from collections import deque

dd = deque(["George", "Peter", "Michael", "William", "Thomas"])
n = 10

while len(dd) > 1:
    dd.rotate(-n + 1)
    print(f"Removed {dd.popleft()}")

print(f"Last is {dd[0]}")
