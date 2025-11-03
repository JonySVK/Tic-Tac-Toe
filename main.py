import pygame

pygame.init()

pygame.display.set_caption("Tic-Tac-Toe")

font = pygame.font.SysFont(None, 40)

window = pygame.display.set_mode((600, 600))

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)

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

    # circle
    # pygame.draw.circle(window, (255, 0, 0), (100, 100), 65, 15)

    # cross
    # pygame.draw.line(window, (0, 0, 255), positions_cross[7][0][0], positions_cross[7][0][1], 25)
    # pygame.draw.line(window, (0, 0, 255), positions_cross[7][1][0], positions_cross[7][1][1], 25)

    pygame.display.update()

pygame.quit()