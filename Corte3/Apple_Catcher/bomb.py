import pygame
import random
from pygame.sprite import Sprite
class Bomb(Sprite):
   #clase para las manzanas
    def __init__(self, ac_game):
        #inicializa la bombay la pone en su pocision de inicio
        super().__init__()
        self.screen = ac_game.screen
        self.settings = ac_game.settings
        self.screen_rect = ac_game.screen.get_rect()

        # carga la imagen
        self.image = pygame.image.load('Images/bomb.png')
        self.rect = self.image.get_rect()

        # Define la localizacion de donde entrara la bomba
        self.rect.x = random.randrange(20, self.screen_rect.right-30)
        self.rect.y = 0
        
        # almancena el valor decimal de la pocision de la manzana
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.settings.bomb_drop_speed
        self.rect.y = self.y


    def blitme(self):
        # dibuja la canasta en su pocision actual
        self.screen.blit(self.image, self.rect)
