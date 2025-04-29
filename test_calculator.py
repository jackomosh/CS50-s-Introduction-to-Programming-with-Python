from calculator import square

def test_calculator():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

if __name__ == "__main__":
    test_calculator()