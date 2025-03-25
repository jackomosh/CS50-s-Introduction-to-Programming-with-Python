emoticon = "v.v"

def main():
    global emoticon
    emoticon = ":)"
    say("Hello there champ!")

def say(phrase):
    print(phrase + ' ' + emoticon)

main()