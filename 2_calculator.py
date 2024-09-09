# without converition if x = 1, y = 2 it will print 12
x = input("x: ")  # input returns string by default
y = input("y: ")  

# convert to int to have addition instead of concatination of strs 
print(int(x) + int(y))