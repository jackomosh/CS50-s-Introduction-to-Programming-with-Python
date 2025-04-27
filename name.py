import sys

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

for arg in sys.argv[:-1]:
    print("Hello, my name is:", arg)