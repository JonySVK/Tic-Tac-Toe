class Player:
    def __init__(self, name, symbol, scores):
        self.scores = scores
        
        self.name = name
        self.symbol = symbol
        self.score = self.scores.get()[0] if symbol == "X" else self.scores.get()[1]

    def update_score(self):
        x_score, o_score = self.scores.get()
        self.score = x_score if self.symbol == "X" else o_score