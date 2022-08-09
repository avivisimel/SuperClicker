import pygame
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400


def createWin():
    background_colour = (234, 212, 252)
    screen = pygame.display.set_mode((854, 480))
    pygame.display.set_caption('Super Clicker')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True


    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


def createLabel():
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('Arial Rounded MT Bold', 350)
    text = font.render('GeeksForGeeks', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    while True:
        display_surface.blit(text, textRect)


def main():
    createWin()
    return
main()