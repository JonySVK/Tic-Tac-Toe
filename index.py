import pygame

pygame.init()

pygame.display.set_caption("Tic-Tac-Toe")

window = pygame.display.set_mode((600, 600))

positions_cirle = {
    1 : (100, 100),
    2 : (300, 100),
    3 : (500, 100),
    4 : (100, 300),
    5 : (300, 300),
    6 : (500, 300),
    7 : (100, 500),
    8 : (300, 500),
    9 : (500, 500)
}

positions_cross = {
    1 : (((50, 50), (150, 150)), ((150, 50), (50, 150))),
    2 : (((250, 50), (350, 150)), ((350, 50), (250, 150))),
    3 : (((450, 50), (550, 150)), ((550, 50), (450, 150))),
    4 : (((50, 250), (150, 350)), ((150, 250), (50, 350))),
    5 : (((250, 250), (350, 350)), ((350, 250), (250, 350))),
    6 : (((450, 250), (550, 350)), ((550, 250), (450, 350))),
    7 : (((50, 450), (150, 550)), ((150, 450), (50, 550))),
    8 : (((250, 450), (350, 550)), ((350, 450), (250, 550))),
    9 : (((450, 450), (550, 550)), ((550, 450), (450, 550)))
}

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

    # circle
    pygame.draw.circle(window, (255, 0, 0), (100, 100), 65, 15)

    # cross
    pygame.draw.line(window, (0, 0, 255), positions_cross[7][0][0], positions_cross[7][0][1], 25)
    pygame.draw.line(window, (0, 0, 255), positions_cross[7][1][0], positions_cross[7][1][1], 25)

    pygame.display.update()

pygame.quit()