x = int(input("What is x? "))
y = int(input("What is y? "))

# this is recursion and the code works

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# conditional statements, if, elif, else

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# conditionals or and not equal

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
