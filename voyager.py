distances = {
    "Voyager 1": "163",
    "Voyager 2": "52",
    "Pioneer 101": "568 AU"
}

def main():

    spacecraft = input("Enter a Spacecraft? ")

    try:
        au = int(distances[spacecraft])
        m = convert(au)
        print(f"{spacecraft} distance in meters is: {m}")
    except ValueError:
        print(f"Cannot convert {distances[spacecraft]} to an int")
    except KeyError:
        print(f"{spacecraft} cannot be found")
        return

def convert(au):
    return au * 2

main()