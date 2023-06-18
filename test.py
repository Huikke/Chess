import unittest
import components.board as board
from components.game import Chess
import components.pieces as pieces

class tests(unittest.TestCase):
    def test_fen(self):
        # FEN to board works
        fen_game = board.fen_to_game("4n1k1/8/3R4/7K/8/8/8/8 w - - 4 30")
        # Set up Chess state manually
        board_state = [pieces.Knight("b", (0, 4)), pieces.King("b", (0, 6)), pieces.Rook("w", (2, 3)), pieces.King("w", (3, 7))]
        game = Chess(board_state, "w", "-", "-", 4, 30)
        # Compare objects
        self.assertEqual(fen_game.board_pieces[0].letter, game.board_pieces[0].letter)
        self.assertEqual(fen_game.board_pieces[1].position, game.board_pieces[1].position)
        self.assertEqual(fen_game.board_pieces[2].color, game.board_pieces[2].color)
        self.assertEqual(fen_game.board_pieces[3].letter, "K")
        self.assertEqual(fen_game.turn, "w")
        self.assertEqual(fen_game.en_passant, game.en_passant)
        self.assertEqual(fen_game.fullmove_number, 30)

        # New board returns correct FEN
        self.assertEqual(board.game_to_fen(Chess()), "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


if __name__ == '__main__':
    unittest.main()