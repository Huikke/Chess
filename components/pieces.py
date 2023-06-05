def rook(s_coord, e_coord):
    for i in range(8):
        s_coord_test1 = (i, s_coord[1])
        s_coord_test2 = (s_coord[0], i)

        if s_coord_test1 == e_coord or s_coord_test2 == e_coord:
            return True

    return False