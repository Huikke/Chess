def rook(s_coord, e_coord):
    if s_coord[0] == e_coord[0] or s_coord[1] == e_coord[1]:
        return True
    return False