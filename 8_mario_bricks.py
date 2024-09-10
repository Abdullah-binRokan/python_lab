from cs50 import get_int

while True:
    n = get_int("n: ")
    if n > 0:
        break

for _ in range(n):
    print("#")