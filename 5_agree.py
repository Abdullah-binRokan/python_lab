s = input("Do you agree? ")

if s in ["y", "yes", "Y", "Yes", "YES", "YeS"]:
    print("Agreed")
elif s in ["n", "No", "N", "NO"]:
    print("Not agreed")