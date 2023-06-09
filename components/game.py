def game_turn(board, str_coord, dest_coord):
    str_row, str_col = str_coord
    dest_row, dest_col = dest_coord

    if board[str_row][str_col] != "o":
        move_check = board[str_row][str_col].movement(dest_coord, board)
        if move_check == True:
            board[dest_row][dest_col] = board[str_row][str_col]
            board[str_row][str_col] = "o"

            return True
    return False