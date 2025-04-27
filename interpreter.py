def main():

    expression = input("Expression: ")

    sign = expression.split()
    print(sign)

    x = int(sign[0])
    y = sign[1]
    z = int(sign[2])

    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "/":
        print(float(x / z))
    else:
        print(float(x * z))

main()