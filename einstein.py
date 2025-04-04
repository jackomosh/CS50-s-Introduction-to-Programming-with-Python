def main():
    # E = mc**2
    mass = int(input("What is the mass of given object? "))
    print(joules(mass))

def joules(n):
    return n * (300000000 * 300000000)

main()