names = ["Ahmed", "Salem", "Nasser"]

name = input("name: ")

if name in names:   # python will linear search the list for you
    print("Found")
else:
    print("Not found")
