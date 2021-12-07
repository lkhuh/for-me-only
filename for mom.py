import pygame
pygame.init()
pygame.mixer.init()

class Button():
    def __init__(self, x, y, image,):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


def second_screen():
    pygame.mixer.music.load("C:\\Users\\Dell\\Downloads\\Happy Birthday Song in English - www.beatdreamer.com.mp3")
    pygame.mixer.music.play()
    font = pygame.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        text = font.render(text, True, color)
        second_window.blit(text, [x, y])

    second_window = pygame.display.set_mode((800, 555))
    light_yellow = 255, 255, 102
    black = 0, 0, 0
    clock = pygame.time.Clock()
    fps = 60
    white = 255, 255, 255
    pygame.display.set_caption("HAPPY BIRTHDAY MOMMY")

    clock.tick(fps)
    pygame.display.update()
    run = True
    while run:
        second_window.fill(light_yellow)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        text_screen("HAPPY BIRTHDAY MUMMY", black, 160, 80)
        pygame.display.update()



def main_screen():
    font = pygame.font.SysFont(None,55)
    def text_screen(text, color, x, y):
        text = font.render(text, True, color)
        main_window.blit(text, [x, y])
    main_window = pygame.display.set_mode((800, 555))
    light_yellow = 255,255,102
    black = 0,0,0
    clock = pygame.time.Clock()
    fps = 60
    white = 255,255,255
    pygame.display.set_caption("HAPPY BIRTHDAY MOMMY")
    main_img = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Pictures\\mom.png").convert_alpha()
    clock.tick(fps)
    pygame.display.update()
    run = True
    while run:
        main_window.fill(light_yellow)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    second_screen()


        main_window.blit(main_img, (230, 150))
        text_screen("HAPPY BIRTHDAY MUMMY", black, 160, 80)
        pygame.display.update()


def home_screen():
    font = pygame.font.SysFont(None,55)
    def text_screen(text, color, x, y):
        text = font.render(text, True, color)
        home_screen.blit(text, [x, y])
    # pygame.mixer.init()
    # pygame.mixer.music.load("C:\\Users\\Dell\\Downloads\\Shape of You(PagalWorld.com.se).mp3")
    # pygame.mixer.music.play()
    home_screen = pygame.display.set_mode([900, 600])
    light_blue = 173, 216, 230
    grey = 128, 126, 120
    black = 0,0,0
    pygame.display.set_caption("HAPPY BIRTHDAY MUMMY")
    text_screen("HAPPY BIRTHDAY", black, 355, 210)
    start_img = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Pictures\\mom.png").convert_alpha()
    exit_img = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Pictures\\mom's birthday candle.png").convert_alpha()
    exit_button = Button(700, 250, exit_img)
    start_button = Button(290, 200, start_img)
    exit_img1 = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Pictures\\mom's birthday candle.png").convert_alpha()
    exit_button1 = Button(150, 250, exit_img1)


    run = True

    while run:
        home_screen.fill(light_blue)
        text_screen("HAPPY BIRTHDAY MUMMY",black,210,50)
        if start_button.draw(home_screen):
            main_screen()
        if exit_button.draw(home_screen):
            pygame.quit()
        if exit_button1.draw(home_screen):
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()

# birthday_window()
home_screen()
pygame.quit()
quit()