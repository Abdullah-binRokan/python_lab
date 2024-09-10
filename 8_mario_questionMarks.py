def main():
    n = get_int("n: ")

    for _ in range(n):
        print("?", end="")
    
    print()


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()