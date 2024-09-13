import sys


def main():
    """
    Main function to validate arguments and filter words based on their length.
    """
    try:
        assert len(sys.argv) == 3
        assert not contains_special_characters(sys.argv[1])
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError()
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)

    filter_string = sys.argv[1].split(' ')
    filter_string = [
        word for word in filter_string
        if (lambda x: len(x) > number and x != '')(word)
    ]
    print(filter_string)


def contains_special_characters(string: str) -> bool:
    """
    Check if the string contains any special characters other than space.
    """
    for char in string:
        if not (char.isalnum() or char == ' '):
            return True
    return False


if __name__ == "__main__":
    main()
