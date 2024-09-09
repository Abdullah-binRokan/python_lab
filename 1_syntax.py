#### printing and importing Library ####

# hello world
print("hello, world")

# Library
import cs50

# for specific function in library
from cs50 import get_string

# another way to access function on Library 
# (helpful if there is another function with the same name)
import cs50
x = cs50.get_int("x: ")

# 1- getting input name with cs50 Lib then print it with hello
name = get_string("what's your name? ")
print("hello, " + name)

# 2- getting input name then print it using comma with hello
name = input("what's your name? ")
print("hello,", name)

# 3- print using format string (f string)
name = input("what's your name? ")
print(f"hello, {name}")

############################
#### Types ####
############################
bool, float, int, str
range, list, tuple, dict, set

############################
#### Conditionals ####
############################ 
if x < y:
    print("x is less than y")

# if else
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

# if elif else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


