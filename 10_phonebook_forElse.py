names = ["Ahmed", "Majed", "Saud"]

name = input("name: ")

for n in names:        # we can use if name in names
    if name == n:
        print("Found")
        break
else:
    print("Not Found")
