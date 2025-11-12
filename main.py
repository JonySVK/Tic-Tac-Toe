import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption("Tic-Tac-Toe")

font_75 = pygame.font.SysFont(None, 75)

window = pygame.display.set_mode((600, 800))

positions_cirle = {
    0 : (100, 100),
    1 : (300, 100),
    2 : (500, 100),
    3 : (100, 300),
    4 : (300, 300),
    5 : (500, 300),
    6 : (100, 500),
    7 : (300, 500),
    8 : (500, 500)
}

positions_cross = {
    0 : (((50, 50), (150, 150)), ((150, 50), (50, 150))),
    1 : (((250, 50), (350, 150)), ((350, 50), (250, 150))),
    2 : (((450, 50), (550, 150)), ((550, 50), (450, 150))),
    3 : (((50, 250), (150, 350)), ((150, 250), (50, 350))),
    4 : (((250, 250), (350, 350)), ((350, 250), (250, 350))),
    5 : (((450, 250), (550, 350)), ((550, 250), (450, 350))),
    6 : (((50, 450), (150, 550)), ((150, 450), (50, 550))),
    7 : (((250, 450), (350, 550)), ((350, 450), (250, 550))),
    8 : (((450, 450), (550, 550)), ((550, 450), (450, 550)))
}

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

turn = "X"

running = True

def check_winner(brd):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for i in winning_combinations:
        if brd[i[0]] == brd[i[1]] == brd[i[2]] and brd[i[0]] != "-":
            return True, i
        else:
            return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if check_winner(board) is not True and board.count("-") > 0:
        window.fill((255, 255, 255))

        pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 5)
        pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 600), (600, 600), 5)

        if check_winner(board) is True:
            text_nxt = font_75.render('Jej', True, (0, 0, 0))
            rect_nxt = text_nxt.get_rect(center=(250, 200))
            window.blit(text_nxt, rect_nxt)
        elif board.count("-") == 0:
            window.fill((255, 0, 0))
            text_nxt = font_75.render('No', True, (0, 0, 0))
            rect_nxt = text_nxt.get_rect(center=(250, 200))
            window.blit(text_nxt, rect_nxt)


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            spot = None
            if mouse_x < 200 and mouse_y < 200:
                spot = 0
            elif 200 < mouse_x < 400 and mouse_y < 200:
                spot = 1
            elif 400 < mouse_x < 600 and mouse_y < 200:
                spot = 2
            elif mouse_x < 200 and 200 < mouse_y < 400:
                spot = 3
            elif 200 < mouse_x < 400 and 200 < mouse_y < 400:
                spot = 4
            elif 400 < mouse_x < 600 and 200 < mouse_y < 400:
                spot = 5
            elif mouse_x < 200 and 400 < mouse_y < 600:
                spot = 6
            elif 200 < mouse_x < 400 and 400 < mouse_y < 600:
                spot = 7
            elif 400 < mouse_x < 600 and 400 < mouse_y < 600:
                spot = 8

            if spot is not None and board[spot] == "-":
                board[spot] = turn
                turn = "O" if turn == "X" else "X"       

        pos = -1
        for x in board:
            pos += 1
            if x == "O":
                pygame.draw.circle(window, (255, 0, 0), positions_cirle[pos], 65, 15)
            elif x == "X":
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][0][0], positions_cross[pos][0][1], 25)
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][1][0], positions_cross[pos][1][1], 25)
        
        text_next = font_75.render('na ťahu:', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 700))
        window.blit(text_next, rect_next)

        if turn == "X":
            pygame.draw.line(window, (0, 0, 255), (375, 675), (425, 725), 20)
            pygame.draw.line(window, (0, 0, 255), (425, 675), (375, 725), 20)
        else:
            pygame.draw.circle(window, (255, 0, 0), (400, 700), 32.5, 12)

        pygame.display.update()

    elif check_winner(board) is True:
        pass

    elif check_winner(board) is not True and board.count("-") == 0:
        window.fill((0, 0, 0))

        text_tie = font_75.render('Je to remíza!', True, (255, 255, 255))
        rect_tie = text_tie.get_rect(center=(300, 400))
        window.blit(text_tie, rect_tie)

        pygame.display.update()

pygame.quit()