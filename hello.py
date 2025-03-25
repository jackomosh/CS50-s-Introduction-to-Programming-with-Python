# name = input("What is your name? ")

# """
# hello there

# """

# name = name.strip()
# name = name.title() #capitalize more than one word in a sentence

# first, middle, last = name.split()

# print(f"Hello {last}")

def main():
    name = input("What is your name? ")
    name = name.capitalize()
    hello(name)

def hello(to):
    print("Hello", to)

main()