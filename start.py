import pygame
from components.start.select import Select
from components.colors import Colors

pygame.init()
pygame.font.init()

class Start:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.colors = Colors()

        self.window = pygame.display.set_mode((600, 1000))

        self.font_35 = pygame.font.SysFont(None, 35)
        self.font_40 = pygame.font.SysFont(None, 40)
        self.font_50 = pygame.font.SysFont(None, 50)
        self.font_60 = pygame.font.SysFont(None, 60)
        self.running = True

        pygame.display.set_caption("Tic-Tac-Toe")

        self.select1 = Select(["Hráč vs. Hráč", "Hráč vs. Počítač"])
        self.select2 = Select(["3x3", "4x4", "5x5"])
        self.select3 = Select(self.colors.get_color_list(without=["Black", "White"], default="Blue"))
        self.select4 = Select(self.colors.get_color_list(without=["Black", "White"], default="Red"))

        self.user_text_x = ""
        self.user_text_y = ""

        self.writing = None
        self.step = None

    def run(self):
        while self.running:
            self.color_x = self.select3.get_current_option()[1]
            self.color_o = self.select4.get_current_option()[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.buttons = [
                        (self.select1, rect_left1, rect_right1),
                        (self.select2, rect_left2, rect_right2),
                        (self.select3, rect_left3, rect_right3),
                        (self.select4, rect_left4, rect_right4)
                    ]
                    for i in self.buttons:
                        if i[1].collidepoint(event.pos):
                            i[0].left()
                        elif i[2].collidepoint(event.pos):
                            i[0].right()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.rect_x_o.collidepoint(event.pos):
                        self.writing = 'x'
                    elif self.rect_y_o.collidepoint(event.pos):
                        self.writing = 'y'
                    else:
                        self.writing = None

                if event.type == pygame.KEYDOWN:
                    if self.writing == 'x':
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            self.writing = None
                            self.step = "4_x_color"
                        elif event.key == pygame.K_BACKSPACE:
                            self.user_text_x = self.user_text_x[:-1]
                        elif event.key not in (pygame.K_RETURN, pygame.K_KP_ENTER):
                            if len(self.user_text_x) < 9:
                                self.user_text_x += event.unicode

                    elif self.writing == 'y':
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            self.writing = None
                            self.step = "6_y_color"
                        elif event.key == pygame.K_BACKSPACE:
                            self.user_text_y = self.user_text_y[:-1]
                        elif event.key not in (pygame.K_RETURN, pygame.K_KP_ENTER):
                            if len(self.user_text_y) < 9:
                                self.user_text_y += event.unicode
                    
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if self.step == None:
                            self.step = "1_mode"
                        elif self.step == "1_mode":
                            self.step = "2_size"
                        elif self.step == "2_size":
                            self.step = "3_x_name"
                            self.writing = 'x'
                        elif self.step == "4_x_color":
                            self.step = "5_y_name"
                            self.writing = 'y'
                        elif self.step == "6_y_color":
                            self.step = "7_confirm"
                        elif self.step == "7_confirm":
                            self.game_mode = self.select1.get_current_option()
                            self.board_size = int(self.select2.get_current_option()[0])
                            self.player_x_name = self.user_text_x if self.user_text_x != "" else "Hráč 1"
                            self.player_y_name = self.user_text_y if self.user_text_y != "" else "Hráč 2"
                            self.player_x_color = self.select3.get_current_option()
                            self.player_y_color = self.select4.get_current_option()
                            return [self.game_mode, self.board_size, self.player_x_name, self.player_y_name, self.player_x_color, self.player_y_color]
                            self.running = False
                    
                    if event.key == pygame.K_LEFT:
                        if self.step == "1_mode" or self.step is None:
                            self.select1.left()
                        elif self.step == "2_size":
                            self.rect_left2_o = pygame.Rect(130, 380, 40, 40)
                            pygame.draw.rect(self.window, self.color_x, self.rect_left2_o, 3)
                            self.select2.left()
                        elif self.step == "4_x_color":
                            self.rect_left3_o = pygame.Rect(30, 745, 40, 40)
                            pygame.draw.rect(self.window, self.color_x, self.rect_left3_o, 3)
                            self.select3.left()
                        elif self.step == "6_y_color":
                            self.rect_left4_o = pygame.Rect(330, 745, 40, 40)
                            pygame.draw.rect(self.window, self.color_o, self.rect_left4_o, 3)
                            self.select4.left()
                    
                    if event.key == pygame.K_RIGHT:
                        if self.step == "1_mode" or self.step is None:
                            self.rect_right1_o = pygame.Rect(430, 255, 40, 40)
                            pygame.draw.rect(self.window, self.color_o, self.rect_right1_o, 3)
                            self.select1.right()
                        elif self.step == "2_size":
                            self.rect_right2_o = pygame.Rect(430, 380, 40, 40)
                            pygame.draw.rect(self.window, self.color_o, self.rect_right2_o, 3)
                            self.select2.right()
                        elif self.step == "4_x_color":             
                            self.rect_right3_o = pygame.Rect(230, 745, 40, 40)
                            pygame.draw.rect(self.window, self.color_x, self.rect_right3_o, 3)
                            self.select3.right()
                        elif self.step == "6_y_color":
                            self.rect_right4_o = pygame.Rect(530, 745, 40, 40)
                            pygame.draw.rect(self.window, self.color_o, self.rect_right4_o, 3)
                            self.select4.right()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if self.rect_confirm_o.collidepoint((mouse_x, mouse_y)):
                        self.game_mode = self.select1.get_current_option()
                        self.board_size = int(self.select2.get_current_option()[0])
                        self.player_x_name = self.user_text_x if self.user_text_x != "" else "Hráč 1"
                        self.player_y_name = self.user_text_y if self.user_text_y != "" else "Hráč 2"
                        self.player_x_color = self.select3.get_current_option()
                        self.player_y_color = self.select4.get_current_option()
                        return [self.game_mode, self.board_size, self.player_x_name, self.player_y_name, self.player_x_color, self.player_y_color]
                        self.running = False
        
            self.window.fill((255, 255, 255))

            if self.step == "1_mode":
                self.rect_left1_o = pygame.Rect(180, 255, 240, 40)
                pygame.draw.rect(self.window, (0, 0, 0), self.rect_left1_o, 3)
            if self.step == "2_size":
                self.rect_left2_o = pygame.Rect(180, 380, 240, 40)
                pygame.draw.rect(self.window, (0, 0, 0), self.rect_left2_o, 3)
            if self.step == "4_x_color":
                self.rect_left3_o = pygame.Rect(115, 730, 70, 70)
                pygame.draw.rect(self.window, self.color_x, self.rect_left3_o, 3)
            if self.step == "6_y_color":
                self.rect_left3_o = pygame.Rect(415, 730, 70, 70)
                pygame.draw.rect(self.window, self.color_o, self.rect_left3_o, 3)
            if self.step == "7_confirm":
                self.rect_confirm_o = pygame.Rect(140, 870, 320, 60)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.topleft, self.rect_confirm_o.bottomleft, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.topright, self.rect_confirm_o.bottomright, 3)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.topleft, self.rect_confirm_o.midtop, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.topright, self.rect_confirm_o.midtop, 3)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.midbottom, self.rect_confirm_o.bottomleft, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.midbottom, self.rect_confirm_o.bottomright, 3)


            pygame.draw.line(self.window, self.color_x, (225, 50), (275, 100), 20)
            pygame.draw.line(self.window, self.color_x, (275, 50), (225, 100), 20)

            pygame.draw.circle(self.window, self.color_o, (350, 75), 32.5, 12)
            
            text_heading = self.font_60.render("Vitaj v hre!", True, (0, 0, 0))
            rect_heading = text_heading.get_rect(center=(300, 150))
            self.window.blit(text_heading, rect_heading)

            text_q1 = self.font_40.render("Vyber si herný mód:", True, (0, 0, 0))
            rect_q1 = text_q1.get_rect(center=(300, 225))
            self.window.blit(text_q1, rect_q1)

            opt1 = self.select1.get_current_option()

            text_opt1 = self.font_35.render(opt1, True, (0, 0, 0))
            rect_opt1 = text_opt1.get_rect(center=(300, 275))
            self.window.blit(text_opt1, rect_opt1)

            text_left1 = self.font_40.render("<", True, (0, 0, 0))
            rect_left1 = text_left1.get_rect(center=(150, 275))
            self.window.blit(text_left1, rect_left1)

            text_right1 = self.font_40.render(">", True, (0, 0, 0))
            rect_right1 = text_right1.get_rect(center=(450, 275))
            self.window.blit(text_right1, rect_right1)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_left1.collidepoint((mouse_x, mouse_y)):
                text_left1 = self.font_40.render("<", True, self.color_x)
                rect_left1 = text_left1.get_rect(center=(150, 275))
                self.window.blit(text_left1, rect_left1)
            elif rect_right1.collidepoint((mouse_x, mouse_y)):
                text_right1 = self.font_40.render(">", True, self.color_o)
                rect_right1 = text_right1.get_rect(center=(450, 275))
                self.window.blit(text_right1, rect_right1)


            text_q2 = self.font_40.render("Vyber si veľkosť hracej plochy:", True, (0, 0, 0))
            rect_q2 = text_q2.get_rect(center=(300, 350))
            self.window.blit(text_q2, rect_q2)

            opt2 = self.select2.get_current_option()

            text_opt2 = self.font_35.render(opt2, True, (0, 0, 0))
            rect_opt2 = text_opt2.get_rect(center=(300, 400))
            self.window.blit(text_opt2, rect_opt2)

            text_left2 = self.font_40.render("<", True, (0, 0, 0))
            rect_left2 = text_left2.get_rect(center=(150, 400))
            self.window.blit(text_left2, rect_left2)

            text_right2 = self.font_40.render(">", True, (0, 0, 0))
            rect_right2 = text_right2.get_rect(center=(450, 400))
            self.window.blit(text_right2, rect_right2)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_left2.collidepoint((mouse_x, mouse_y)):
                text_left2 = self.font_40.render("<", True, self.color_x)
                rect_left2 = text_left2.get_rect(center=(150, 400))
                self.window.blit(text_left2, rect_left2)
            elif rect_right2.collidepoint((mouse_x, mouse_y)):
                text_right2 = self.font_40.render(">", True, self.color_o)
                rect_right2 = text_right2.get_rect(center=(450, 400))
                self.window.blit(text_right2, rect_right2)

            pygame.draw.line(self.window, self.color_x, (125, 525), (175, 475), 20)
            pygame.draw.line(self.window, self.color_x, (175, 525), (125, 475), 20)

            pygame.draw.circle(self.window, self.color_o, (450, 500), 32.5, 12)

            self.text_x = self.font_40.render("Zadaj meno:", True, (0, 0, 0))
            self.rect_x = self.text_x.get_rect(center=(150, 575))
            self.window.blit(self.text_x, self.rect_x)

            self.text_y = self.font_40.render("Zadaj meno:", True, (0, 0, 0))
            self.rect_y = self.text_y.get_rect(center=(450, 575))
            self.window.blit(self.text_y, self.rect_y)

            self.text_x = self.font_35.render(self.user_text_x, True, (0, 0, 0))
            self.rect_x = self.text_x.get_rect(center=(150, 620))
            self.window.blit(self.text_x, self.rect_x)

            self.rect_x_o = pygame.Rect(25, 600, 250, 40)
            pygame.draw.rect(self.window, (0, 0, 0), self.rect_x_o, 3)

            self.text_y = self.font_35.render(self.user_text_y, True, (0, 0, 0))
            self.rect_y = self.text_y.get_rect(center=(450, 620))
            self.window.blit(self.text_y, self.rect_y)

            self.rect_y_o = pygame.Rect(325, 600, 250, 40)
            pygame.draw.rect(self.window, (0, 0, 0), self.rect_y_o, 3)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.rect_x_o.collidepoint((mouse_x, mouse_y)) or self.writing == 'x':
                self.rect_x_o = pygame.Rect(25, 600, 250, 40)
                pygame.draw.rect(self.window, self.color_x, self.rect_x_o, 3)
            elif self.rect_y_o.collidepoint((mouse_x, mouse_y)) or self.writing == 'y':
                self.rect_y_o = pygame.Rect(325, 600, 250, 40)
                pygame.draw.rect(self.window, self.color_o, self.rect_y_o, 3)

            self.text_x = self.font_40.render("Vyber si farbu:", True, (0, 0, 0))
            self.rect_x = self.text_x.get_rect(center=(150, 700))
            self.window.blit(self.text_x, self.rect_x)

            self.text_y = self.font_40.render("Vyber si farbu:", True, (0, 0, 0))
            self.rect_y = self.text_y.get_rect(center=(450, 700))
            self.window.blit(self.text_y, self.rect_y)

            opt3 = self.select3.get_current_option()

            pygame.draw.circle(self.window, opt3[1], (150, 765), 25)

            text_left3 = self.font_40.render("<", True, (0, 0, 0))
            rect_left3 = text_left3.get_rect(center=(50, 765))
            self.window.blit(text_left3, rect_left3)

            text_right3 = self.font_40.render(">", True, (0, 0, 0))
            rect_right3 = text_right3.get_rect(center=(250, 765))
            self.window.blit(text_right3, rect_right3)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_left3.collidepoint((mouse_x, mouse_y)):
                text_left3 = self.font_40.render("<", True, self.color_x)
                rect_left3 = text_left3.get_rect(center=(50, 765))
                self.window.blit(text_left3, rect_left3)
            elif rect_right3.collidepoint((mouse_x, mouse_y)):
                text_right3 = self.font_40.render(">", True, self.color_x)
                rect_right3 = text_right3.get_rect(center=(250, 765))
                self.window.blit(text_right3, rect_right3)

            opt4 = self.select4.get_current_option()

            pygame.draw.circle(self.window, opt4[1], (450, 765), 25)

            text_left4 = self.font_40.render("<", True, (0, 0, 0))
            rect_left4 = text_left4.get_rect(center=(350, 765))
            self.window.blit(text_left4, rect_left4)

            text_right4 = self.font_40.render(">", True, (0, 0, 0))
            rect_right4 = text_right4.get_rect(center=(550, 765))
            self.window.blit(text_right4, rect_right4)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_left4.collidepoint((mouse_x, mouse_y)):
                text_left4 = self.font_40.render("<", True, self.color_o)
                rect_left4 = text_left4.get_rect(center=(350, 765))
                self.window.blit(text_left4, rect_left4)
            elif rect_right4.collidepoint((mouse_x, mouse_y)):
                text_right4 = self.font_40.render(">", True, self.color_o)
                rect_right4 = text_right4.get_rect(center=(550, 765))
                self.window.blit(text_right4, rect_right4)

            self.text_confirm = self.font_35.render("POTVRDIŤ A ZAČAŤ HRU", True, (0, 0, 0))
            self.rect_confirm = self.text_confirm.get_rect(center=(300, 900))
            self.window.blit(self.text_confirm, self.rect_confirm)

            self.rect_confirm_o = pygame.Rect(140, 870, 320, 60)
            pygame.draw.rect(self.window, (0, 0, 0), self.rect_confirm_o, 3)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.rect_confirm_o.collidepoint((mouse_x, mouse_y)):
                self.rect_confirm_o = pygame.Rect(140, 870, 320, 60)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.topleft, self.rect_confirm_o.bottomleft, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.topright, self.rect_confirm_o.bottomright, 3)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.topleft, self.rect_confirm_o.midtop, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.topright, self.rect_confirm_o.midtop, 3)
                pygame.draw.line(self.window, self.color_x, self.rect_confirm_o.midbottom, self.rect_confirm_o.bottomleft, 3)
                pygame.draw.line(self.window, self.color_o, self.rect_confirm_o.midbottom, self.rect_confirm_o.bottomright, 3)

            pygame.display.update()

            self.clock.tick(60)

if __name__ == "__main__":
    Start().run()