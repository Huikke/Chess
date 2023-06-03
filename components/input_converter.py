# Converts an input to a form python understands
def input_converter(move: str) -> int:
    # Converts latter part of coord
    col = ord(move[0].upper()) - 65
    # Converts number part of coord
    row = int(move[1]) - 1
    row = abs(row - 7)

    return row, col