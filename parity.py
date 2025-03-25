def main():
    x = int(input("What is x? "))
    if isEven(x):
        print("Even Number")
    else:
        print("Odd Number")

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
        

main()
