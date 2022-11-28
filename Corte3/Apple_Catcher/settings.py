
import pygame as pg
import random
class Settings:
    def __init__(self):
        screen_info = pg.display.Info()
        self.screen_width = 1000 #screen_info.current_w
        self.screen_height = 800 #screen_info.current_h
        self.bg_color = (230, 230, 230)
        self.flag = pg.RESIZABLE

        # Inicializa la configuracion estatica
        self.apples_allowed = 3
        self.apple_limit = 3
        self.game_over = False

        # Puntos por manzana 
        self.apple_points = 2
        self.gapple_points = 4

        # escalado de nivel
        self.levelup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.basket_speed = 18
        self.apple_drop_speed = 3.5
        self.gapple_drop_speed = 5.5


    def increase_speed(self):
        self.basket_speed *= self.levelup_scale
        self.apple_drop_speed *= self.levelup_scale
        self.gapple_drop_speed *=self.levelup_scale

       
