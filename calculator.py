# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = (x / y)

# print(f"{z:.2f}")

def main():
    x = int(input("What is x? "))
    print("X Squared is: ", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()