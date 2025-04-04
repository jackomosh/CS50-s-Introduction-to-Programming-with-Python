def main():
    # print(letters("James", "Jack"))

    names = ["James", "Rehema", "Hike"]

    for name in names:
        print(letters(name, "Jack"))

def letters(Reciever, Sender):
    return f"""

    ~--------------------------~

    Dear {Reciever},

    Kindly note that the meeting is scheduled Monday 25th April 2025.

    Sincerely,
    {Sender}.

    ~---------------------------~

    """

main()