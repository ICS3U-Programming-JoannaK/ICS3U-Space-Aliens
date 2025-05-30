#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: May 28, 2025
# This program is the "space Aliens" program for RST-01


import ugame
import stage


def game_scene():

    # displays the greeting message
    print("== PYDASH ==")
    print("Good Luck, Jumper.")

    while True:
        # placeholder
        pass


if __name__ == "__main__":
    game_scene()


    image_bank_background = stage.Bank.from_png(Screenshot 2025-05-28 140820.png)
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()


import ugame
import stage

def game_scene():
    
    image_bank_background = stage.Bank.from_bmp24("Screenshot 2025-05-28 140820 (1).bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 10)
    game.layers = [background]
    game.render_block()
    
    while True:
         pass

if __name__ == "__main__":
    game_scene()



    import ugame
import stage

def game_scene():
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()
    
    while True:
         pass

if __name__ == "__main__":
    game_scene()