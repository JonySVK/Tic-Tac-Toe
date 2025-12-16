import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption("Tic-Tac-Toe")

font_75 = pygame.font.SysFont(None, 75)
font_45 = pygame.font.SysFont(None, 45)
font_30 = pygame.font.SysFont(None, 30)

window = pygame.display.set_mode((600, 1000))

positions_cirle = {
    0 : (100, 300),
    1 : (300, 300),
    2 : (500, 300),
    3 : (100, 500),
    4 : (300, 500),
    5 : (500, 500),
    6 : (100, 700),
    7 : (300, 700),
    8 : (500, 700)
}

positions_cross = {
    0 : (((50, 250), (150, 350)), ((150, 250), (50, 350))),
    1 : (((250, 250), (350, 350)), ((350, 250), (250, 350))),
    2 : (((450, 250), (550, 350)), ((550, 250), (450, 350))),
    3 : (((50, 450), (150, 550)), ((150, 450), (50, 550))),
    4 : (((250, 450), (350, 550)), ((350, 450), (250, 550))),
    5 : (((450, 450), (550, 550)), ((550, 450), (450, 550))),
    6 : (((50, 650), (150, 750)), ((150, 650), (50, 750))),
    7 : (((250, 650), (350, 750)), ((350, 650), (250, 750))),
    8 : (((450, 650), (550, 750)), ((550, 650), (450, 750)))
}

positions_line = {
    0 : ((10, 300), (590, 300)),
    1 : ((10, 500), (590, 500)),
    2 : ((10, 700), (590, 700)),
    3 : ((100, 210), (100, 790)),
    4 : ((300, 210), (300, 790)),
    5 : ((500, 210), (500, 790)),
    6 : ((20, 220), (580, 780)),
    7 : ((580, 220), (20, 780))
}

board = ["-"] * 9
turn = "X"
running = True
newgame = False

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

playerx = {
    "name": "Hráč 1",
    "score" : 0
}

playero = {
    "name": "Hráč 2",
    "score" : 0
}

while running:
    iswinner, winner, combo = check_winner(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not iswinner and board.count("-") > 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            spot = None
            if mouse_y >= 200 and mouse_y <= 800:
                row = (mouse_y - 200) // 200
                col = mouse_x // 200
                spot = row * 3 + col

            if spot is not None and board[spot] == "-":
                board[spot] = turn
                turn = "O" if turn == "X" else "X"
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and newgame == True:
            board = ["-"] * 9
            turn = "X"
            iswinner = False
            winner = None
            combo = None
            newgame = False

    window.fill((255, 255, 255))

    text_playerx = font_45.render(playerx["name"], True, (0, 0, 0))
    rect_playerx = text_playerx.get_rect(center=(200, 150))
    window.blit(text_playerx, rect_playerx)
    text_playerx_score = font_75.render(str(playerx["score"]), True, (0, 0, 0))
    rect_playerx_score = text_playerx_score.get_rect(center=(75, 100))
    window.blit(text_playerx_score, rect_playerx_score)
    pygame.draw.line(window, (0, 0, 255), (175, 50), (225, 100), 20)
    pygame.draw.line(window, (0, 0, 255), (225, 50), (175, 100), 20)

    text_playero = font_45.render(playero["name"], True, (0, 0, 0))
    rect_playero = text_playero.get_rect(center=(400, 150))
    window.blit(text_playero, rect_playero)
    text_playero_score = font_75.render(str(playero["score"]), True, (0, 0, 0))
    rect_playero_score = text_playero_score.get_rect(center=(525, 100))
    window.blit(text_playero_score, rect_playero_score)
    pygame.draw.circle(window, (255, 0, 0), (400, 75), 32.5, 12)

    pygame.draw.line(window, (0, 0, 0), (300, 25), (300, 175), 3)

    pygame.draw.line(window, (0, 0, 0), (200, 200), (200, 800), 5)
    pygame.draw.line(window, (0, 0, 0), (400, 200), (400, 800), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 600), (600, 600), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 800), (600, 800), 5)


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
        rect_next = text_next.get_rect(center=(250, 900))
        window.blit(text_next, rect_next)

        if turn == "X":
            pygame.draw.line(window, (0, 0, 255), (375, 875), (425, 925), 20)
            pygame.draw.line(window, (0, 0, 255), (425, 875), (375, 925), 20)
        else:
            pygame.draw.circle(window, (255, 0, 0), (400, 900), 32.5, 12)

    if iswinner and winner == "X":
        text_next = font_75.render('Vyhral', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 900))
        window.blit(text_next, rect_next)
        pygame.draw.line(window, (0, 0, 255), (375, 875), (425, 925), 30)
        pygame.draw.line(window, (0, 0, 255), (425, 875), (375, 925), 30)
        text_n = font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
        rect_n = text_n.get_rect(center=(300, 980))
        window.blit(text_n, rect_n)
        newgame = True

    if iswinner and winner == "O":
        text_next = font_75.render('Vyhral', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(250, 900))
        window.blit(text_next, rect_next)
        pygame.draw.circle(window, (255, 0, 0), (400, 900), 32.5, 20)
        text_n = font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
        rect_n = text_n.get_rect(center=(300, 980))
        window.blit(text_n, rect_n)
        newgame = True

    if not iswinner and board.count("-") == 0:
        text_next = font_75.render('Je to remíza!', True, (0, 0, 0))
        rect_next = text_next.get_rect(center=(300, 900))
        window.blit(text_next, rect_next)
        text_n = font_30.render('Kliknutím začnete novú hru.', True, (0, 0, 0))
        rect_n = text_n.get_rect(center=(300, 980))
        window.blit(text_n, rect_n)
        newgame = True

    pygame.display.update()

pygame.quit()