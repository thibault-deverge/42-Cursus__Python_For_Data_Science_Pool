import sys


def main():
    """
    This program analyze the provided string as Command-line argument and
    display the sum of the differents types of character in it.
    """
    try:
        if len(sys.argv) < 2 or sys.argv[1] == "":
            input_str = ask_user_input()
        else:
            assert len(sys.argv) == 2, "Too many arguments provided."
            input_str = sys.argv[1]
    except AssertionError as error:
        print(f"AssertionError: {error}")
        exit(1)

    analyse_string(input_str)


def analyse_string(string: str) -> dict:
    """
    Analyzes the given string and prints the counts of various character types.
    """
    punctuation_set = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    nums_characters = len(string)
    nums_upper = sum([1 for char in string if char.isupper()])
    nums_lower = sum([1 for char in string if char.islower()])
    nums_punctuations = sum([1 for char in string if char in punctuation_set])
    nums_spaces = sum([1 for char in string if char.isspace()])
    nums_digits = sum([1 for char in string if char.isdigit()])

    print(f"The text contains {nums_characters} characters:")
    print(f"\t{nums_upper} upper letters")
    print(f"\t{nums_lower} lower letters")
    print(f"\t{nums_punctuations} punctuation marks")
    print(f"\t{nums_spaces} spaces")
    print(f"\t{nums_digits} digits")


def ask_user_input() -> str:
    """
    Prompts the user for input and return it if no
    command-line argument is provided.
    """
    user_input = ""
    try:
        while (not user_input):
            user_input = input("What is the text to count?\n")
            user_input += '\n'
        return user_input
    except EOFError:
        print("Input terminated unexpectedly. Exiting program.")
        sys.exit(1)


if __name__ == '__main__':
    main()
