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

positions_line = {
    0 : ((10, 100), (590, 100)),
    1 : ((10, 300), (590, 300)),
    2 : ((10, 500), (590, 500)),
    3 : ((100, 10), (100, 590)),
    4 : ((300, 10), (300, 590)),
    5 : ((500, 10), (500, 590)),
    6 : ((20, 20), (580, 580)),
    7 : ((580, 20), (20, 580))
}

board = ["-"] * 9
turn = "X"
running = True

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

def check_winner(brd):
    for i in winning_combinations:
        if brd[i[0]] == brd[i[1]] == brd[i[2]] and brd[i[0]] in ("X", "O"):
            return True, brd[i[0]], i
    return False, None, None


while running:
    iswinner, winner, combo = check_winner(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not iswinner and board.count("-") > 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            spot = None
            if mouse_y < 600:
                row = mouse_y // 200
                col = mouse_x // 200
                spot = row * 3 + col

            if spot is not None and board[spot] == "-":
                board[spot] = turn
                turn = "O" if turn == "X" else "X"

    window.fill((255, 255, 255))

    pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 600), (600, 600), 5)


    for pos, mark in enumerate(board):
        if iswinner and combo is not None and pos in winning_combinations[winning_combinations.index(combo)]:
            if mark == "O":
                pygame.draw.circle(window, (255, 0, 0), positions_cirle[pos], 65, 35)
                pygame.draw.line(window, (255, 0, 0), positions_line[winning_combinations.index(combo)][0], positions_line[winning_combinations.index(combo)][1], 30)
            elif mark == "X":
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][0][0], positions_cross[pos][0][1], 45)
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][1][0], positions_cross[pos][1][1], 45)
                pygame.draw.line(window, (0, 0, 255), positions_line[winning_combinations.index(combo)][0], positions_line[winning_combinations.index(combo)][1], 30)
        else:
            if mark == "O":
                pygame.draw.circle(window, (255, 0, 0), positions_cirle[pos], 65, 15)
            elif mark == "X":
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][0][0], positions_cross[pos][0][1], 25)
                pygame.draw.line(window, (0, 0, 255), positions_cross[pos][1][0], positions_cross[pos][1][1], 25)


    if not iswinner and board.count("-") > 0:
        text_next = font_75.render('na ťahu:', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 700))
        window.blit(text_next, rect_next)

        if turn == "X":
            pygame.draw.line(window, (0, 0, 255), (375, 675), (425, 725), 20)
            pygame.draw.line(window, (0, 0, 255), (425, 675), (375, 725), 20)
        else:
            pygame.draw.circle(window, (255, 0, 0), (400, 700), 32.5, 12)

    if iswinner and winner == "X":
        text_next = font_75.render('Vyhral', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 700))
        window.blit(text_next, rect_next)
        pygame.draw.line(window, (0, 0, 255), (375, 675), (425, 725), 30)
        pygame.draw.line(window, (0, 0, 255), (425, 675), (375, 725), 30)

    if iswinner and winner == "O":
        text_next = font_75.render('Vyhral', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 700))
        window.blit(text_next, rect_next)
        pygame.draw.circle(window, (255, 0, 0), (400, 700), 32.5, 20)

    if not iswinner and board.count("-") == 0:
        text_next = font_75.render('Je to remíza!', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(300, 700))
        window.blit(text_next, rect_next)

    pygame.display.update()

pygame.quit()