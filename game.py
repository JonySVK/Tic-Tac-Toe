# Created by Jan Ivicic © 2025 - 2026

import time
import pygame
import os
from start import Start
from components.lang import Lang
from components.game.player import Player
from components.game.scores import Scores
from components.game.board import Board
from components.game.draw import Draw
from components.colors import Colors
from ai.minimax import Minimax
from ai.chaos import Chaos
from ai.training import Training

pygame.init()
pygame.font.init()
pygame.mixer.init()

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
            "player_o_color": self.home[5],
            "sound_status": self.home[6],
            "lang": self.home[7]
        }

        self.language = Lang()
        self.lang = self.user_settings["lang"]

        self.color_x = self.user_settings["player_x_color"][1]
        self.color_o = self.user_settings["player_o_color"][1]

        self.scores = Scores()
        self.player_x = Player(self.user_settings["player_x_name"], "X", self.scores)
        self.player_o = Player(self.user_settings["player_o_name"], "O", self.scores)
        self.board = Board(self.scores, self.player_x, self.player_o, self.user_settings["board_size"])
        self.draw = Draw(self.player_x, self.player_o, self.user_settings)

        if self.language.translate(self.lang, "Hráč vs. Počítač") in self.user_settings["game_mode"]:
            self.ai_mode = True
            self.ai_mode_difficulty = self.user_settings["game_mode"].replace(self.language.translate(self.lang, "Hráč vs. Počítač") + " ", "")
            self.minimax = Minimax(self.user_settings["board_size"], "O")
            self.multiplayer = False
            if self.ai_mode_difficulty == "EASY":
                self.depth = 2
            elif self.ai_mode_difficulty == "MEDIUM":
                self.depth = 4
            elif self.ai_mode_difficulty == "HARD":
                self.depth = 6
            elif self.ai_mode_difficulty == "EXPERT":
                self.depth = 9
            elif "CHAOS" in self.ai_mode_difficulty:
                self.depth = 6
                self.chaos = Chaos()
        elif self.language.translate(self.lang, "Hráč vs. Hráč CHAOS") in self.user_settings["game_mode"]:
            self.ai_mode = False
            self.ai_mode_difficulty = "CHAOS"
            self.chaos = Chaos()
            self.multiplayer = False
        elif self.language.translate(self.lang, "Tréning s AI") in self.user_settings["game_mode"]:
            self.ai_mode = True
            self.ai_mode_difficulty = "TRAINING"
            self.training = Training(self.user_settings["board_size"], "X", self.lang)
            self.multiplayer = False
            self.minimax = Minimax(self.user_settings["board_size"], "O")
        else:
            self.ai_mode = False
            self.ai_mode_difficulty = None
            self.multiplayer = False

        self.base_path = os.path.dirname(__file__)

        ico_path = os.path.join(self.base_path, "files", "ico.png")
        ico = pygame.image.load(ico_path).convert_alpha()
        pygame.display.set_icon(ico)

        self.sound_status_sound = "on"
        if self.user_settings["sound_status"] == "off" and self.sound_status_sound == "off":
            self.sound_status = "off"
        elif self.user_settings["sound_status"] == "off" and self.sound_status_sound == "on":
            self.sound_status = "mid"
        elif self.user_settings["sound_status"] == "on" and self.sound_status_sound == "on":
            self.sound_status = "on"

        self.sound_click_path = os.path.join(self.base_path, "files", "click.mp3")
        self.sound_win_path = os.path.join(self.base_path, "files", "win.mp3")
        self.sound_background_path = os.path.join(self.base_path, "files", "background.mp3")

        if self.sound_status == "on":
            pygame.mixer.music.load(self.sound_background_path)
            pygame.mixer.music.set_volume(0.04)
            pygame.mixer.music.play(loops=-1)

        self.turn = "X"
        self.running = True
        self.newgame = False

        self.training_text = self.language.translate(self.lang, "Aký ťah by si urobil?")
        self.human_move = None

        self.sleep = None
        self.tt_size = None
        self.win_played = False
        self.rea = False

    def run(self):
        while self.running:
            pygame.display.set_caption(self.language.translate(self.lang, "Piškvorky"))

            self.draw.window.fill((255, 255, 255))

            sound_path = os.path.join(self.base_path, "files", "sound_" + str(self.sound_status) + ".png")
            sound = pygame.image.load(sound_path).convert_alpha()
            sound = pygame.transform.scale(sound, (55, 55))
            self.draw.window.blit(sound, (5, 5))

            self.draw.draw_board()

            self.iswinner, self.winner, self.combo = self.board.check_winner(self.board.board)

            self.chaosmode = None

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
                        if self.ai_mode_difficulty == "TRAINING" and self.turn == "X":
                            self.human_move = spot
                            if self.sound_status_sound == "on":
                                click = pygame.mixer.Sound(self.sound_click_path)
                                click.set_volume(2)
                                click.play()
                        else:
                            self.board.board[spot] = self.turn
                            self.chaosmode = True
                            self.turn = "O" if self.turn == "X" else "X"
                            if self.sound_status_sound == "on":
                                click = pygame.mixer.Sound(self.sound_click_path)
                                click.set_volume(2)
                                click.play()
                    
                    self.sound_button_rect = pygame.Rect(0, 0, 60, 60)
                    if self.sound_button_rect.collidepoint(mouse_pos):
                        if self.sound_status == "on":
                            self.sound_status = "mid"
                            pygame.mixer.music.pause()
                            
                        elif self.sound_status == "mid":
                            self.sound_status = "off"
                            self.sound_status_sound = "off"
                        elif self.sound_status == "off":
                            self.sound_status = "on"
                            self.sound_status_sound = "on"
                            pygame.mixer.music.unpause()
                    
                    self.reset_button_rect = pygame.Rect(540, 0, 60, 60)
                    if self.reset_button_rect.collidepoint(mouse_pos):
                        Game().run()

                if self.ai_mode and self.turn == "O" and not self.iswinner and self.board.board.count("-") > 0:
                    ai_move = self.minimax.find_ai_best_move(self.board.board, (self.depth if self.ai_mode_difficulty != "TRAINING" else 3))
                    self.board.board[ai_move] = "O"
                    self.turn = "X"
                
                if self.ai_mode and self.ai_mode_difficulty == "TRAINING" and self.turn == "X" and not self.iswinner and self.board.board.count("-") > 0:
                    self.training_text = self.language.translate(self.lang, "Aký ťah by si urobil?")
                    self.rea = False

                    if self.human_move is not None:
                        self.rea = False
                        self.best_move, self.reason = self.training.find_human_best_move(self.board.board, 3)
                        if self.human_move == self.best_move:
                            self.training_text = self.language.translate(self.lang, "Výborný ťah!")
                            self.sleep = 2
                            self.board.board[self.best_move] = "X"
                            self.turn = "O"
                            self.human_move = None
                            self.rea = False
                        else:
                            self.tt_size = "smaller"
                            self.training_text = self.language.translate(self.lang, "Toto je ideálny ťah, pretože:")
                            self.board.board[self.best_move] = "X"
                            self.sleep = 2
                            self.turn = "O"
                            self.human_move = None
                            self.rea = True


                if self.ai_mode_difficulty == "CHAOS" and not self.iswinner and self.board.board.count("-") > 0 and self.chaosmode is True:
                    self.chaos.chaos(self.board.board)
                    self.chaosmode = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.newgame == True:
                    self.board.board = ["-"] * (9 if self.user_settings["board_size"] == 3 else (16 if self.user_settings["board_size"] == 4 else (25 if self.user_settings["board_size"] == 5 else 0)))
                    self.turn = "X"
                    self.iswinner = False
                    self.winner = None
                    self.combo = None
                    self.newgame = False
                    self.scores.added = False
                    self.win_played = False

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
                        
            if not self.ai_mode_difficulty == "TRAINING" and not self.iswinner and self.board.board.count("-") > 0:
                text_next = self.draw.font_75.render(self.language.translate(self.lang, 'na ťahu:'), True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(250, 900))
                self.draw.window.blit(text_next, rect_next)

            if self.ai_mode_difficulty == "TRAINING" and not self.iswinner and self.board.board.count("-") > 0:
                if self.tt_size == "smaller":
                    text_next = self.draw.font_25.render(self.training_text, True, (0, 0, 0))
                    if self.rea:
                        text_rea = self.draw.font_25.render(self.reason, True, (0, 0, 0))
                    self.sleep = 2
                    self.tt_size = None
                else:
                    text_next = self.draw.font_45.render(self.training_text, True, (0, 0, 0))
                    if self.rea:
                        text_rea = self.draw.font_45.render(self.reason, True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(300, 900))
                self.draw.window.blit(text_next, rect_next)
                if self.rea:
                    rect_rea = text_rea.get_rect(center=(300, 935))
                    self.draw.window.blit(text_rea, rect_rea)

            if self.turn == "X" and not self.iswinner and self.board.board.count("-") > 0 and not self.ai_mode_difficulty == "TRAINING":
                pygame.draw.line(self.draw.window, self.color_x, (375, 875), (425, 925), 20)
                pygame.draw.line(self.draw.window, self.color_x, (425, 875), (375, 925), 20)
            elif self.turn == "O" and not self.iswinner and self.board.board.count("-") > 0 and not self.ai_mode_difficulty == "TRAINING":
                pygame.draw.circle(self.draw.window, self.color_o, (400, 900), 32.5, 12)

            if self.iswinner and self.winner == "X":
                if not self.win_played and self.sound_status_sound == "on":
                    win = pygame.mixer.Sound(self.sound_win_path)
                    win.set_volume(2)
                    win.play()
                    self.win_played = True
                text_next = self.draw.font_75.render(self.language.translate(self.lang, 'Víťaz:'), True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(235, 900))
                self.draw.window.blit(text_next, rect_next)
                pygame.draw.line(self.draw.window, self.color_x, (375, 875), (425, 925), 30)
                pygame.draw.line(self.draw.window, self.color_x, (425, 875), (375, 925), 30)
                text_n = self.draw.font_30.render(self.language.translate(self.lang, 'Kliknutím začnete novú hru.'), True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            if self.iswinner and self.winner == "O":
                if not self.win_played and self.sound_status_sound == "on":
                    win = pygame.mixer.Sound(self.sound_win_path)
                    win.set_volume(2)
                    win.play()
                    self.win_played = True
                text_next = self.draw.font_75.render(self.language.translate(self.lang, 'Víťaz:'), True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(235, 900))
                self.draw.window.blit(text_next, rect_next)
                pygame.draw.circle(self.draw.window, self.color_o, (400, 900), 32.5, 20)
                text_n = self.draw.font_30.render(self.language.translate(self.lang, 'Kliknutím začnete novú hru.'), True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            if not self.iswinner and self.board.board.count("-") == 0:
                text_next = self.draw.font_75.render(self.language.translate(self.lang, 'Je to remíza!'), True, (0, 0, 0))
                rect_next = text_next.get_rect(center=(300, 900))
                self.draw.window.blit(text_next, rect_next)
                text_n = self.draw.font_30.render(self.language.translate(self.lang, 'Kliknutím začnete novú hru.'), True, (0, 0, 0))
                rect_n = text_n.get_rect(center=(300, 980))
                self.draw.window.blit(text_n, rect_n)
                self.newgame = True

            pygame.display.update()

            if self.sleep is not None:
                time.sleep(self.sleep)
                self.sleep = None

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()