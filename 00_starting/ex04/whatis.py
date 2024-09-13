import sys


def main():
    try:
        if len(sys.argv) < 2:
            return
        assert len(sys.argv) == 2, "more than one argument is provided"

        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if number % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
