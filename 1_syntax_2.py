############################
#### exceptions ####
############################
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")
            # pass
            # you can use pass instead of print to silently try again

x = get_int("x: ")

############################
#### Truncation ####
############################

# python is smart & doesn't truncate
x = int(input("x: "))  # 1
y = int(input("y: "))  # 3
z = x / y   # int / int
print(z)   # 0.33333333333  python get back with a float

############################
#### floating-point imprecision ####
############################

# python has a limitiation. you can use a library 
# that give you better precision for scientific purposes
x = int(input("x: "))  # 1
y = int(input("y: "))  # 3
z = x / y   # int / int
print(f"{z:.50f}")   # print float with 40 decimal points

############################
#### integer overflow ####
############################

# if u count to high in c you might overflow the capacity
# of int & end up going back to 0 or negative
# in Python this problem doesn't exist

