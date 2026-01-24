# Created by Jan Ivicic © 2025 - 2026

import pygame
from start import Start
from components.game.player import Player
from components.game.scores import Scores
from components.game.board import Board
from components.game.draw import Draw
from components.colors import Colors

pygame.init()
pygame.font.init()

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.colors = Colors()
        self.home = Start().run()

        self.user_settings = {
            "game_mode": self.home[0],
            "board_size": self.home[1],
            "player_x_name": self.home[2],
            "player_o_name": self.home[3],
            "player_x_color": self.home[4],
            "player_o_color": self.home[5]
        }

        self.color_x = self.user_settings["player_x_color"][1]
        self.color_o = self.user_settings["player_o_color"][1]

        self.scores = Scores()
        self.player_x = Player(self.user_settings["player_x_name"], "X", self.scores)
        self.player_o = Player(self.user_settings["player_o_name"], "O", self.scores)
        self.board = Board(self.scores, self.player_x, self.player_o, self.user_settings["board_size"])
        self.draw = Draw(self.player_x, self.player_o, self.user_settings)

        pygame.display.set_caption("Tic-Tac-Toe")

        self.turn = "X"
        self.running = True
        self.newgame = False
        
    def run(self):
        while self.running:
            self.draw.window.fill((255, 255, 255))

            self.draw.draw_board()

            self.iswinner, self.winner, self.combo = self.board.check_winner(self.board.board)

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.iswinner and self.board.board.count("-") > 0:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    spot = None
                    if mouse_y >= 200 and mouse_y <= 800 and self.user_settings["board_size"] == 3:
                        row = (mouse_y - 200) // 200
                        col = mouse_x // 200
                        spot = row * 3 + col
                    elif mouse_y >= 200 and mouse_y <= 1000 and self.user_settings["board_size"] == 4:
                        row = (mouse_y - 200) // 150
                        col = mouse_x // 150
                        spot = row * 4 + col
                    elif mouse_y >= 200 and mouse_y <= 1200 and self.user_settings["board_size"] == 5:
                        row = (mouse_y - 200) // 120
                        col = mouse_x // 120
                        spot = row * 5 + col

                    if spot is not None and spot < len(self.board.board) and self.board.board[spot] == "-":
                        self.board.board[spot] = self.turn
                        self.turn = "O" if self.turn == "X" else "X"
                    else:
                        pass
                    
                    self.reset_button_rect = pygame.Rect(540, 0, 60, 60)
                    if self.reset_button_rect.collidepoint(mouse_pos):
                        Game().run()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.newgame == True:
                    self.board.board = ["-"] * (9 if self.user_settings["board_size"] == 3 else (16 if self.user_settings["board_size"] == 4 else (25 if self.user_settings["board_size"] == 5 else 0)))
                    self.turn = "X"
                    self.iswinner = False
                    self.winner = None
                    self.combo = None
                    self.newgame = False
                    self.scores.added = False

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.user_settings["board_size"] == 3:
                for i in range (9):
                    rect = pygame.Rect((i % 3) * 200, 200 + (i // 3) * 200, 200, 200)
                    mouse_pos = (mouse_x, mouse_y)
                    if rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "X":
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][0][0], self.board.positions_cross[i][0][1], 25)
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][1][0], self.board.positions_cross[i][1][1], 25)
                    elif rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "O":
                        pygame.draw.circle(self.draw.window, self.colors.get_hover_color_code(code=self.color_o), self.board.positions_cirle[i], (65 if self.user_settings["board_size"] == 3 else (50 if self.user_settings["board_size"] == 4 else (40 if self.user_settings["board_size"] == 5 else 0))), 15)
            elif self.user_settings["board_size"] == 4:
                for i in range (16):
                    rect = pygame.Rect((i % 4) * 150, 200 + (i // 4) * 150, 150, 150)
                    mouse_pos = (mouse_x, mouse_y)
                    if rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "X":
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][0][0], self.board.positions_cross[i][0][1], 25)
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][1][0], self.board.positions_cross[i][1][1], 25)
                    elif rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "O":
                        pygame.draw.circle(self.draw.window, self.colors.get_hover_color_code(code=self.color_o), self.board.positions_cirle[i], (65 if self.user_settings["board_size"] == 3 else (50 if self.user_settings["board_size"] == 4 else (40 if self.user_settings["board_size"] == 5 else 0))), 15)
            elif self.user_settings["board_size"] == 5:
                for i in range (25):
                    rect = pygame.Rect((i % 5) * 120, 200 + (i // 5) * 120, 120, 120)
                    mouse_pos = (mouse_x, mouse_y)
                    if rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "X":
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][0][0], self.board.positions_cross[i][0][1], 25)
                        pygame.draw.line(self.draw.window, self.colors.get_hover_color_code(code=self.color_x), self.board.positions_cross[i][1][0], self.board.positions_cross[i][1][1], 25)
                    elif rect.collidepoint(mouse_pos) and self.board.board[i] == "-" and not self.iswinner and self.board.board.count("-") > 0 and self.turn == "O":
                        pygame.draw.circle(self.draw.window, self.colors.get_hover_color_code(code=self.color_o), self.board.positions_cirle[i], (65 if self.user_settings["board_size"] == 3 else (50 if self.user_settings["board_size"] == 4 else (40 if self.user_settings["board_size"] == 5 else 0))), 15)



            for pos, mark in enumerate(self.board.board):
                if self.iswinner and self.combo is not None and pos in self.board.winning_combinations[self.board.winning_combinations.index(self.combo)]:
                    if mark == "O":
                        pygame.draw.circle(self.draw.window, self.color_o, self.board.positions_cirle[pos], (65 if self.user_settings["board_size"] == 3 else (50 if self.user_settings["board_size"] == 4 else (40 if self.user_settings["board_size"] == 5 else 0))), 35)
                        pygame.draw.line(self.draw.window, self.color_o, self.board.positions_line[self.board.winning_combinations.index(self.combo)][0], self.board.positions_line[self.board.winning_combinations.index(self.combo)][1], (30 if self.user_settings["board_size"] == 3 else (25 if self.user_settings["board_size"] == 4 else (20 if self.user_settings["board_size"] == 5 else 0))))
                    elif mark == "X":
                        pygame.draw.line(self.draw.window, self.color_x, self.board.positions_cross[pos][0][0], self.board.positions_cross[pos][0][1], 45)
                        pygame.draw.line(self.draw.window, self.color_x, self.board.positions_cross[pos][1][0], self.board.positions_cross[pos][1][1], 45)
                        pygame.draw.line(self.draw.window, self.color_x, self.board.positions_line[self.board.winning_combinations.index(self.combo)][0], self.board.positions_line[self.board.winning_combinations.index(self.combo)][1], (30 if self.user_settings["board_size"] == 3 else (25 if self.user_settings["board_size"] == 4 else (20 if self.user_settings["board_size"] == 5 else 0))))
                else:
                    if mark == "O":
                        pygame.draw.circle(self.draw.window, self.color_o, self.board.positions_cirle[pos], (65 if self.user_settings["board_size"] == 3 else (50 if self.user_settings["board_size"] == 4 else (40 if self.user_settings["board_size"] == 5 else 0))), 15)
                    elif mark == "X":
                        pygame.draw.line(self.draw.window, self.color_x, self.board.positions_cross[pos][0][0], self.board.positions_cross[pos][0][1], 25)
                        pygame.draw.line(self.draw.window, self.color_x, self.board.positions_cross[pos][1][0], self.board.positions_cross[pos][1][1], 25)


            if not self.iswinner and self.board.board.count("-") > 0:
                text_next = self.draw.font_75.render('na ťahu:', True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(250, 900))
                self.draw.window.blit(text_next, rect_next)

            if self.turn == "X" and not self.iswinner and self.board.board.count("-") > 0:
                pygame.draw.line(self.draw.window, self.color_x, (375, 875), (425, 925), 20)
                pygame.draw.line(self.draw.window, self.color_x, (425, 875), (375, 925), 20)
            elif self.turn == "O" and not self.iswinner and self.board.board.count("-") > 0:
                pygame.draw.circle(self.draw.window, self.color_o, (400, 900), 32.5, 12)

            if self.iswinner and self.winner == "X":
                text_next = self.draw.font_75.render('Vyhral', True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(250, 900))
                self.draw.window.blit(text_next, rect_next)
                pygame.draw.line(self.draw.window, self.color_x, (375, 875), (425, 925), 30)
                pygame.draw.line(self.draw.window, self.color_x, (425, 875), (375, 925), 30)
                text_n = self.draw.font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            if self.iswinner and self.winner == "O":
                text_next = self.draw.font_75.render('Vyhral', True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(250, 900))
                self.draw.window.blit(text_next, rect_next)
                pygame.draw.circle(self.draw.window, self.color_o, (400, 900), 32.5, 20)
                text_n = self.draw.font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            if not self.iswinner and self.board.board.count("-") == 0:
                text_next = self.draw.font_75.render('Je to remíza!', True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(300, 900))
                self.draw.window.blit(text_next, rect_next)
                text_n = self.draw.font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()