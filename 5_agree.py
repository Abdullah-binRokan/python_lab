s = input("Do you agree? ")

# a better design to use str method (lower)
s = s.lower()

if s in ["y", "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Not agreed")