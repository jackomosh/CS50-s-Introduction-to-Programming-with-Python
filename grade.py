score = int(input("What was your Score? "))

if score >= 90 and score <= 100:
    print(score, "is Grade A")
elif score >= 80 and score <= 89:
    print(score, "is Grade B")
elif score >= 70 and score <= 79:
    print(score, "is Grade C")
elif score >= 60 and score <= 69:
    print(score, "is Grade D")
else:
    print(score, "not yet, work harder, Grade E")