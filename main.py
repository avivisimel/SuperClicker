import pygame


score = 1

def startup():
    pygame.init()
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    X = 400
    Y = 400
    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    while True:
        display_surface.fill(white)
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


def main():
    startup()

if __name__ == '__main__':
    main()
