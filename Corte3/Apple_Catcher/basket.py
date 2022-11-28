import pygame

class Basket:
    #clase para la canasta
    def __init__(self, ac_game):
       # inicializa canasta y la pone en su pocision inicial
        self.screen = ac_game.screen
        self.settings = ac_game.settings
        self.screen_rect = ac_game.screen.get_rect()

        # carga imagen
        self.image = pygame.image.load('Images/basket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        # almacena el valor decimal de la pocision de la canasta
        self.x = float(self.rect.x)

        # Movemiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # actualiza la pocision de la canasta basada en el movimiento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.basket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.basket_speed


        self.rect.x = self.x

    def blitme(self):
       #dibbuja la canasta en su pocision actual
        self.screen.blit(self.image, self.rect)