# Created by Jan Ivicic © 2025 - 2026

import random

class Chaos:
    def __init__(self):
        pass

    def chaos(self, board):
        self.board = board

        for i in range(random.randint(1, 3)):
            self.x = random.randint(0, len(self.board) - 1)
            self.y = random.randint(0, 2)
            if self.y == 0 and self.board[self.x] != "X":
                self.board[self.x] = "X"
            elif self.y == 1 and self.board[self.x] != "O":
                self.board[self.x] = "O"
            elif self.y == 2 and self.board[self.x] != "-":
                self.board[self.x] = "-"

        return self.board
                
            

