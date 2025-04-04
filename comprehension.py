def main():
    counts = {}
    words = get_words("address.txt")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    save_count(counts)

def save_count():
    ...

def get_words(address):
    try:
        with open(address, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File not found at {address.txt}")
        return None

main()