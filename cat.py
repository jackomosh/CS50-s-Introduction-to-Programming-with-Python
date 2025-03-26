# while True:
#     x = int(input("What is x? "))
#     if x > 0:
#         break

# for _ in range(x):
#     print("Meow")


# while True:
#     n = int(input("What is n? "))
#     if n < 0:
#         print("Give a positive number")
#     else:
#         break


# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        x = int(input("What is x? "))
        if x < 0:
            print("Enter a number greater than 0")
        else:
            break
    return x

def meow(n):
    for _ in range(n):
        print("meow")

main()