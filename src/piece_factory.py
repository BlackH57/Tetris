import random
import piece


class Factory:
    def __init__(self):
        self.list_piece = [piece.Piece(0),
                           piece.Piece(1),
                           piece.Piece(2),
                           piece.Piece(3),
                           piece.Piece(4),
                           piece.Piece(5),
                           piece.Piece(6)]

        self.queue = random.choices(self.list_piece, k=4)

    def add_random_piece(self):
        used_piece = self.queue.pop(0)
        self.queue.append(random.choice(self.list_piece))
        return used_piece
