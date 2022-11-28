import sys
import threading
import time
import pygame as pg
from apple import Apple
from basket import Basket
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from sounds import Music
from threading import Thread
from gold_apple import Gapple
class Hilo(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        th1 = threading.Thread(target=ec._drop_apples, args=ec.apples)
        th1.start()
        th2 = threading.Thread(target=ec._drop_gapples, args=ec.gapples)
        th2.start()

class AppleCatcher:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, \
        self.settings.screen_height), self.settings.flag)
        pg.display.set_caption('Atrapa las manzanas')

        # fondo
        self.background = pg.image.load('Images/background.png')

        self.music = Music()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.basket = Basket(self)
        self.apples = pg.sprite.Group()
        self.gapples = pg.sprite.Group()
        self.th= Hilo()
        # boton para jugar
        self.play_button = Button(self, "Play")

        # hacer pantalla rectagular
        self.screen_rect = self.screen.get_rect()

       
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.basket.update()
                self.th.run()
               # self._drop_apples()
                self.apples.update()
              #  self._drop_bombs()
                self.gapples.update()
                self._check_apples_bottom()
                self._check_gapples_bottom()
                self._update_apples()
                self._update_gapples()
            self._update_screen()


    def check_for_level_up(self):
        # Aunmentar el nuvel cada vez que el puntaje sea un multiplo de 20
        if self.stats.score!=0 and self.stats.score%20 == 0:
            self.settings.increase_speed()
            # aumentar nivel
            self.stats.level += 1
            self.sb.prep_level()


    def _update_apples(self):
        #si la manzana cruza  la ventana, desaparece
        for apple in self.apples.copy():
            if apple.rect.bottom >= self.screen_rect.bottom:
                self.apples.remove(apple)
        self._check_basket_apple_collisions()
    
    def _update_gapples(self):
         for apple in self.apples.copy():
            if apple.rect.bottom >= self.screen_rect.bottom:
                self.apples.remove(apple)
         self._check_basket_gapple_collisions()
       
     



    def _check_basket_apple_collisions(self):
        # cada vez que la canasta y la manzana colisionan se obtiene puntos
        collisions = pg.sprite.spritecollide(self.basket, self.apples, True)
        if collisions:
            # si se detecta una colision de obtiene puntos
            self.stats.score += self.settings.apple_points
            self.check_for_level_up()
            self.music.apple_catched.play()
            self.sb.prep_score()
    
    def _check_basket_gapple_collisions(self):
        # cada vez que la canasta y la manzana colisionan se obtiene puntos
        collisions = pg.sprite.spritecollide(self.basket, self.gapples, True)
        if collisions:
            # si se detecta una colision de obtiene puntos
            self.stats.score += self.settings.gapple_points
            self.check_for_level_up()
            self.music.apple_catched.play()
            self.sb.prep_score()

    def _check_apples_bottom(self):
        # verifica si la manzana crusa el borde inferior de la ventana
        screen_rect = self.screen.get_rect()
        for apple in self.apples.sprites():
            if apple.rect.bottom >= screen_rect.bottom:
                self._apple_hit()
                break

    def _check_gapples_bottom(self):
        # verifica si la manzana crusa el borde inferior de la ventana
        screen_rect = self.screen.get_rect()
        for gapple in self.gapples.sprites():
            if gapple.rect.bottom >= screen_rect.bottom:
                break

    def _apple_hit(self):
        #revisa los intentos restantes de atrapar una manzana y ejecuta el sonido de caida. si ya no hay mas intentos, ejecuta el sonido de game over.
        if self.stats.apples_left > 0:
            self.stats.apples_left -= 1
            self.music.apple_droped.play()
            self.sb.prep_apples()
        else:
            self.music.game_over.play()
            self.stats.game_active = False
            pg.mouse.set_visible(True)
            self.music.bg_music.stop()

        
    def _drop_apples(self):
       # deja caer la manzana en una pocision random
        if len(self.apples) == 0:
                new_apple = Apple(self)
                self.apples.add(new_apple)
        if len(self.apples) == 1:
            for apple in self.apples.sprites():
                if apple.rect.bottom > 300:
                    new_apple = Apple(self)
                    self.apples.add(new_apple)
        if len(self.apples) == 2:
            for apple in self.apples.sprites():
                if apple.rect.bottom > 600:
                    new_apple = Apple(self)
                    self.apples.add(new_apple)
        if len(self.apples) == 3:
            for apple in self.apples.sprites():
                if apple.rect.bottom > 900:
                    new_apple = Apple(self)
                    self.apples.add(new_apple)

    def _drop_gapples(self):
       # deja caer la manzana en una pocision random
        if len(self.gapples) == 0:
                new_gapple = Gapple(self)
                self.gapples.add(new_gapple)
        
                    
    def _check_play_button(self, mouse_pos):
        #inicia el juego cuando el jugador le da clic al boton
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            # resetea las estadisticas del juego
            self.stats.reset_stats()
            self.stats.game_active = True
            # suena la musica de fondo
            self.music.bg_music.play()

            self.sb.prep_score()
            self.sb.prep_apples()
            self.sb.prep_level()
            # se desace de las manzanas restantes
            self.apples.empty()
            self.gapples.empty()
            # oculta el cursosr
            pg.mouse.set_visible(False)
        
        
    def _check_events(self):
        #responde a los eventos del cursosr
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            
                
    def _check_keydown_events(self, event):
        # responde a las teclas
        if event.key == pg.K_RIGHT:
            self.basket.moving_right = True
        elif event.key == pg.K_LEFT:
            self.basket.moving_left = True
        elif event.key == pg.K_SPACE:
            self._drop_apples()

    
    def _check_keyup_events(self, event):
        #responde a soltar las teclas
        if event.key == pg.K_RIGHT:
            self.basket.moving_right = False
        elif event.key == pg.K_LEFT:
            self.basket.moving_left = False


    def _update_screen(self):
        # actualiza las imagenes en pantalla
        self.screen.blit(self.background, (0,0))
        self.basket.blitme()

        for apple in self.apples.sprites():
            apple.blitme()
        for gapple in self.gapples.sprites():
            gapple.blitme()

        # Dibuja el puntaje
        self.sb.show_score()
        # dibuja el boton si el  juego esta inactivo
        if not self.stats.game_active:
            self.play_button.draw_button()

        pg.display.flip()



if __name__ == '__main__':
    ec = AppleCatcher()
    ec.run_game()


