# Created by Jan Ivicic © 2025 - 2026

import pygame

pygame.init()
pygame.font.init()

class Draw:
    def __init__(self, player_x, player_o, user_settings):
        self.player_x = player_x
        self.player_o = player_o
        
        self.user_settings = user_settings

        self.color_x = self.user_settings["player_x_color"][1]
        self.color_o = self.user_settings["player_o_color"][1]

        self.font_75 = pygame.font.SysFont(None, 75)
        self.font_45 = pygame.font.SysFont(None, 45)
        self.font_30 = pygame.font.SysFont(None, 30)

        self.window = pygame.display.set_mode((600, 1000))
        self.window.fill((255, 255, 255))
        
    def draw_board(self):
        pygame.draw.circle(self.window, (0, 0, 0), (570, 30), 22.5, 5)
        pygame.draw.line(self.window, (255, 255, 255), (570, 30), (540, 40), 20)
        pygame.draw.line(self.window, (0, 0, 0), (567, 34), (556, 41), 5)
        pygame.draw.line(self.window, (0, 0, 0), (558, 58), (556, 41), 5)

        if self.user_settings["board_size"] == 3:
            self.text_playerx = self.font_45.render(self.player_x.name, True, (0, 0, 0))
            self.rect_playerx = self.text_playerx.get_rect(center=(200, 150))
            self.window.blit(self.text_playerx, self.rect_playerx)
            self.text_playerx_score = self.font_75.render(str(self.player_x.score), True, (0, 0, 0))
            self.rect_playerx_score = self.text_playerx_score.get_rect(center=(75, 100))
            self.window.blit(self.text_playerx_score, self.rect_playerx_score)
            pygame.draw.line(self.window, self.color_x, (175, 50), (225, 100), 20)
            pygame.draw.line(self.window, self.color_x, (225, 50), (175, 100), 20)

            self.text_playero = self.font_45.render(self.player_o.name, True, (0, 0, 0))
            self.rect_playero = self.text_playero.get_rect(center=(400, 150))
            self.window.blit(self.text_playero, self.rect_playero)
            self.text_playero_score = self.font_75.render(str(self.player_o.score), True, (0, 0, 0))
            self.rect_playero_score = self.text_playero_score.get_rect(center=(525, 100))
            self.window.blit(self.text_playero_score, self.rect_playero_score)
            pygame.draw.circle(self.window, self.color_o, (400, 75), 32.5, 12)

            pygame.draw.line(self.window, (0, 0, 0), (300, 25), (300, 175), 3)

            pygame.draw.line(self.window, (0, 0, 0), (200, 200), (200, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (400, 200), (400, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 200), (600, 200), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 400), (600, 400), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 600), (600, 600), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 800), (600, 800), 5)

        elif self.user_settings["board_size"] == 4:
            self.text_playerx = self.font_45.render(self.player_x.name, True, (0, 0, 0))
            self.rect_playerx = self.text_playerx.get_rect(center=(200, 150))
            self.window.blit(self.text_playerx, self.rect_playerx)
            self.text_playerx_score = self.font_75.render(str(self.player_x.score), True, (0, 0, 0))
            self.rect_playerx_score = self.text_playerx_score.get_rect(center=(75, 100))
            self.window.blit(self.text_playerx_score, self.rect_playerx_score)
            pygame.draw.line(self.window, self.color_x, (175, 50), (225, 100), 20)
            pygame.draw.line(self.window, self.color_x, (225, 50), (175, 100), 20)

            self.text_playero = self.font_45.render(self.player_o.name, True, (0, 0, 0))
            self.rect_playero = self.text_playero.get_rect(center=(400, 150))
            self.window.blit(self.text_playero, self.rect_playero)
            self.text_playero_score = self.font_75.render(str(self.player_o.score), True, (0, 0, 0))
            self.rect_playero_score = self.text_playero_score.get_rect(center=(525, 100))
            self.window.blit(self.text_playero_score, self.rect_playero_score)
            pygame.draw.circle(self.window, self.color_o, (400, 75), 32.5, 12)

            pygame.draw.line(self.window, (0, 0, 0), (300, 25), (300, 175), 3)

            pygame.draw.line(self.window, (0, 0, 0), (150, 200), (150, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (300, 200), (300, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (450, 200), (450, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 200), (800, 200), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 350), (800, 350), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 500), (800, 500), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 650), (800, 650), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 800), (800, 800), 5)

        elif self.user_settings["board_size"] == 5:
            self.text_playerx = self.font_45.render(self.player_x.name, True, (0, 0, 0))
            self.rect_playerx = self.text_playerx.get_rect(center=(200, 150))
            self.window.blit(self.text_playerx, self.rect_playerx)
            self.text_playerx_score = self.font_75.render(str(self.player_x.score), True, (0, 0, 0))
            self.rect_playerx_score = self.text_playerx_score.get_rect(center=(75, 100))
            self.window.blit(self.text_playerx_score, self.rect_playerx_score)
            pygame.draw.line(self.window, self.color_x, (175, 50), (225, 100), 20)
            pygame.draw.line(self.window, self.color_x, (225, 50), (175, 100), 20)

            self.text_playero = self.font_45.render(self.player_o.name, True, (0, 0, 0))
            self.rect_playero = self.text_playero.get_rect(center=(400, 150))
            self.window.blit(self.text_playero, self.rect_playero)
            self.text_playero_score = self.font_75.render(str(self.player_o.score), True, (0, 0, 0))
            self.rect_playero_score = self.text_playero_score.get_rect(center=(525, 100))
            self.window.blit(self.text_playero_score, self.rect_playero_score)
            pygame.draw.circle(self.window, self.color_o, (400, 75), 32.5, 12)

            pygame.draw.line(self.window, (0, 0, 0), (300, 25), (300, 175), 3)

            pygame.draw.line(self.window, (0, 0, 0), (120, 200), (120, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (240, 200), (240, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (360, 200), (360, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (480, 200), (480, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (600, 200), (600, 800), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 200), (800, 200), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 320), (800, 320), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 440), (800, 440), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 560), (800, 560), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 680), (800, 680), 5)
            pygame.draw.line(self.window, (0, 0, 0), (0, 800), (800, 800), 5)         
