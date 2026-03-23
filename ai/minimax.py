# Created by Jan Ivicic © 2025 - 2026

class Minimax:
    def __init__(self, board_size, ai_char):
        self.board_size = board_size
        self.ai_char = ai_char
        self.human_char = "O" if ai_char == "X" else "X"
        if self.board_size == 3:
            self.winning_combinations = [
                        (0, 1, 2),
                        (3, 4, 5),
                        (6, 7, 8),
                        (0, 3, 6),
                        (1, 4, 7),
                        (2, 5, 8),
                        (0, 4, 8),
                        (2, 4, 6)
                    ]
        if self.board_size == 4:
            self.winning_combinations = [
                    (0, 1, 2, 3),
                    (4, 5, 6, 7),
                    (8, 9, 10, 11),
                    (12, 13, 14, 15),
                    (0, 4, 8, 12),
                    (1, 5, 9, 13),
                    (2, 6, 10, 14),
                    (3, 7, 11, 15),
                    (0, 5, 10, 15),
                    (3, 6, 9, 12)
                    ]
        if self.board_size == 5:
            self.winning_combinations = [
                    (0, 1, 2, 3, 4),
                    (5, 6, 7, 8, 9),
                    (10, 11, 12, 13, 14),
                    (15, 16, 17, 18, 19),
                    (20, 21, 22, 23, 24),
                    (0, 5, 10, 15, 20),
                    (1, 6, 11, 16, 21),
                    (2, 7, 12, 17, 22),
                    (3, 8, 13, 18, 23),
                    (4, 9, 14, 19, 24),
                    (0, 6, 12, 18, 24),
                    (4, 8, 12, 16, 20)
            ]

    def find_ai_best_move(self, board, depth):
        best_score = float("-inf")
        best_move = None
        alpha = float("-inf")
        beta = float("inf")

        for i in range(len(board)):
            if board[i] == "-":
                board[i] = self.ai_char
                score = self.minimax(board, depth - 1, False, alpha, beta)
                board[i] = "-"

                if score > best_score:
                    best_score = score
                    best_move = i

                alpha = max(alpha, best_score)

        return best_move

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        winner = self.check_winner(board)

        if winner == self.ai_char:
            return 10 + depth
        if winner == self.human_char:
            return -10 - depth
        if "-" not in board or depth == 0:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(len(board)):
                if board[i] == "-":
                    board[i] = self.ai_char
                    score = self.minimax(board, depth - 1, False, alpha, beta)
                    board[i] = "-"
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)

                    if alpha >= beta:
                        break

            return best_score
        else:
            best_score = float("inf")
            for i in range(len(board)):
                if board[i] == "-":
                    board[i] = self.human_char
                    score = self.minimax(board, depth - 1, True, alpha, beta)
                    board[i] = "-"
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)

                    if alpha >= beta:
                        break

            return best_score

    def check_winner(self, board):
        for combo in self.winning_combinations:
            first = board[combo[0]]
            if first == "-":
                continue
            if all(board[i] == first for i in combo):
                return first
        return None