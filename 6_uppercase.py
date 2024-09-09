before = input("Before: ")
print("Afer:   ", end="")  # added the named parameters to alter default behavior
for c in before:
    print(c.upper(), end="")  # end="" will alter the default new line behaivor
print()