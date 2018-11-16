#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pygame
from Game_plum import Game
from Config import Config
def main():
    display = pygame.display.set_mode((Config['game']['height'],Config['game']['width']))
    pygame.display.set_caption(Config['game']['caption'])

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()
