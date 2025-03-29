#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import menu


class game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        while True:
            Menu = menu(self.window)
            menu_return = Menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass
