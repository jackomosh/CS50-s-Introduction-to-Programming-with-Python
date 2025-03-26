def main():
    column(5)

def column(h):
    for _ in range(h):
        print("#")

main()

# print rows

def main():
    row(4)

def row(w):
    print("?" * w)

main()

def main():
    square(3)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()