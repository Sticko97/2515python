def check_plate(plate):
    """
    This function checks if a given string is a valid license plate number.
    The correct format is: NN-LL-NN, where:
    - N is a number from 1 to 9
    - L is an uppercase letter (from A to Z)
    """
    if len(plate) != 7:
        return False
    if not plate[0:2].isdigit() or not plate[5:7].isdigit():
        return False
    if not plate[2:5].isalpha() or not plate[2:5].isupper():
        return False
    if plate[0] == "0" or plate[5] == "0":
        return False
    return True


def find_next_plate(plate, num_plates=1):
    """
    This function generates the next 'num_plates' license plate numbers
    coming after a given license plate number.
    """
    if not check_plate(plate):
        return False

    prefix, middle, suffix = plate[0:2], plate[2:5], plate[5:7]
    for i in range(num_plates):
        suffix = str(int(suffix) + 1)
        if suffix == "10":
            middle = chr(ord(middle[1]) + 1) + "A"
            suffix = "1"
        elif suffix == "00":
            middle = chr(ord(middle[0]) + 1) + "A"
            suffix = "1"
        if middle == "AA":
            prefix = str(int(prefix) + 1)
            middle = "AA"
            suffix = "1"
        if int(prefix) > 99:
            raise OverflowError("No more license plates available")
    return prefix + "-" + middle + "-" + suffix
