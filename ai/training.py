# Created by Jan Ivicic © 2025 - 2026

from ai.minimax import Minimax
from components.lang import Lang

class Training:
    def __init__(self, board_size, human_char, lang):
        self.board_size = board_size
        self.human_char = human_char
        self.minimax = Minimax(board_size, human_char)

        self.center = {3: 4, 4: 8, 5: 12}
        self.corners = {3: [0, 2, 6, 8], 4: [0, 3, 12, 15], 5: [0, 4, 20, 24]}

        self.language = Lang()
        self.lang = lang
    
    def find_human_best_move(self, board, depth):
        best_move = self.minimax.find_ai_best_move(board, depth)

        reason = self.analyze_move(board, best_move)

        return best_move, reason

    def analyze_move(self, board, move):
        # simuluj ťah
        board[move] = self.human_char

        if self.minimax.check_winner(board) == self.minimax.ai_char:
            board[move] = "-"
            return self.language.translate(self.lang, "Tento ťah vedie k okamžitej výhre.")

        if self.opponent_can_win_next(board):
            board[move] = "-"
            return self.language.translate(self.lang, "Tento ťah blokuje výhru súpera.")

        if len(board) == 9 and move == self.center[self.board_size]:
            board[move] = "-"
            return self.language.translate(self.lang, "Stred je strategicky najsilnejšia pozícia.")

        if len(board) == 9 and move in self.corners[self.board_size]:
            board[move] = "-"
            return self.language.translate(self.lang, "Rohy sú výhodné pre budovanie výhry.")

        board[move] = "-"
        return self.language.translate(self.lang, "Toto je najlepší strategický ťah.")


    def opponent_can_win_next(self, board):
        for i in range(len(board)):
            if board[i] == "-":
                board[i] = self.minimax.human_char
                if self.minimax.check_winner(board) == self.minimax.human_char:
                    board[i] = "-"
                    return True
                board[i] = "-"
        return False