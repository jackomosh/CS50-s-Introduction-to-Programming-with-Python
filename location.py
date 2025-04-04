import sys

def main():
    # tuples are immutable.. you cant change any value in the tuple

    # comparison between tupes and lists in terms of memory

    coordinates_list = [42.372, -71.115]
    coordinates = (42.372, -71.115)
    print(f"{sys.getsizeof(coordinates_list)}") # list takes more memory than a tuple
    print(f"{sys.getsizeof(coordinates)}") # tuples take less memory

    
    latitude, longitude = coordinates # assignining the tuples to a var

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

main()