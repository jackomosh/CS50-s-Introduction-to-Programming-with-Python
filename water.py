from soil import sample

def main():
    moisture = sample()
    print(f"Moisture is: {moisture}%")

    while moisture < 18:
        moisture = sample()
        print(f"Moisture is: {moisture}%")
    print("Time to water")

main()