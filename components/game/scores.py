class Scores:
    def __init__(self):
        self.player_x_score = 0
        self.player_o_score = 0

        self.added = False
    
    def add(self, winner):
        if winner == "X":
            self.player_x_score += 1
        elif winner == "O":
            self.player_o_score += 1

    
    def get(self):
        return self.player_x_score, self.player_o_score