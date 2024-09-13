import sys


MORSE_CODE_DICT = {
    ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}


def contains_special_characters(string: str) -> bool:
    """
    Check if the string contains any special characters other than space.
    """
    for char in string:
        if not (char.isalnum() or char == ' '):
            return True
    return False


def main():
    """
    Main function to validate input and translate the input to Morse code.
    """
    try:
        assert len(sys.argv) == 2
        assert not contains_special_characters(sys.argv[1])
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)

    string = sys.argv[1].upper()
    morse_string = " ".join([MORSE_CODE_DICT.get(char) for char in string])
    print(morse_string)


if __name__ == "__main__":
    main()
