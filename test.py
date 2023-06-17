import unittest
import components.board as board

class tests(unittest.TestCase):
    def test_fen_to_game(self):
        game = board.fen_to_game("rnbqkb1r/ppp2ppp/3p1n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
        board.display(game.board_pieces)


if __name__ == '__main__':
    unittest.main()