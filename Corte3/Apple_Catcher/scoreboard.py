import pygame.font
from pygame.sprite import Group

from apple import Apple

class Scoreboard:
    def __init__(self, ac_game):
        self.ac_game = ac_game
        self.screen = ac_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ac_game.settings
        self.stats = ac_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_apples()
        self.prep_level()

    # Muestra el nivel
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)
        # posicion del nivel
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # muestra intentos de dejar caer una manzana.
    def prep_apples(self):
        #manzanas faltantes
        self.apples = Group()
        for apple_number in range(self.stats.apples_left):
            apple = Apple(self.ac_game)
            apple.rect.x = 10 + apple_number * apple.rect.width
            apple.rect.y = 10
            self.apples.add(apple)

    # Muestra total de puntos
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #enseña  el puntaje
        self.screen.blit(self.score_image, self.score_rect)
        self.apples.draw(self.screen)
        self.screen.blit(self.level_image, self.level_rect)