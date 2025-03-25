shows = [
    " Avatar: the last airbender",
    "Ben 10",
    "johnny bravo",
    "Power puff girls ",
    " Spongebob Squarepants",
    "the proud family"
]

print("\n")
print(shows)
print("\n")

def main():
    cleaned_str = []
    for show in shows:
        cleaned_str.append(show.strip().title())
    print(', '.join(cleaned_str) + '\n')
    
main()