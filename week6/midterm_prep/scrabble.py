# def scrabble_score(word: str) -> int:
#     """Calculates how many Scrabble points a word is worth"""
    
#     LETTER_SCORES = {
#         "a": 1,
#         "b": 3,
#         "c": 3,
#         "d": 2,
#         "e": 1,
#         "f": 4,
#         "g": 2,
#         "h": 4,
#         "i": 1,
#         "j": 8,
#         "k": 5,
#         "l": 1,
#         "m": 3,
#         "n": 1,
#         "o": 1,
#         "p": 3,
#         "q": 10,
#         "r": 1,
#         "s": 1,
#         "t": 1,
#         "u": 1,
#         "v": 4,
#         "w": 4,
#         "x": 8,
#         "y": 4,
#         "z": 10,
#     }

# if __name__ == "__main__":
#     word = input("Enter a word: ")
#     score = scrabble_score(word)
#     print(word, "is worth", score, "Scrabble points")
import string
import getpass

def has_uppercase(password: str) -> bool:
    """checks if password has an upper case character

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains an uppercase character otherwise False
    """
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password: str) -> bool:
    """checks if password contains an lower case character

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a lowercase character otherwise False
    """
    for char in password:
        if char.islower():
            return True
    return False


def has_number(password: str) -> bool:
    """checks if password contains a number

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a number otherwise False
    """
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password: str) -> bool:
    """checks if password contains one of ~!@#$%^&*_+-=")

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a special character otherwise False
    """
    special_chars = "~!@#$%^&*_+-=\""
    for char in password:
        if char in special_chars:
            return True
    return False

def has_length(password: str, min_length: int = 10) -> bool:
    """checks if password length is at least min_length
    
    Args:
        password (str): password to be validated
        min_length (int): minimum required password length
        
    Returns:
        bool: True if password has at least the required length otherwise False
    """
    return len(password) >= min_length

def strong_password(password: str) -> bool:
    """Verifies password is at least 10 chars and contains an uppercase, lowercase, special, number

    Args:
        password (str): password to check

    Returns:
        bool: True if a "strong" password otherwise False
    """
    if (
        has_lowercase(password)
        and has_uppercase(password)
        and has_number(password)
        and has_special(password)
        and has_length(password)
    ):
        return True
    else:
        return False


def main():
    """prompts user for and validates users password indicating if it is strong enough
    This function asks the user for their password without displaying it
    and
    """
    password = getpass.getpass("Please enter your password: ")
    if strong_password(password):
        print("Strong Password")
    else:
        print("Weak Password")


if __name__ == "__main__":
    main()
