# Converts an input to a form python understands
def input_converter(move):
    # String length is less than 2 causes an error
    if len(move) < 2:
        return ValueError

    # Converts latter part of coord
    col = ord(move[0].upper()) - 65
    if col < 65 and col > 72:
        return ValueError

    # Converts number part of coord
    if not move[1].isdigit() or int(move[1]) < 1 or int(move[1]) > 8:
        return ValueError
    row = int(move[1]) - 1
    row = abs(row - 7)

    return row, col