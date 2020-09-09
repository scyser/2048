import os
import keyboard
import time
from matrix import Game2048

if __name__ == '__main__':
    size = int(input("Enter size: "))
    game = Game2048(size)

    os.system('CLS')
    print(game.game)
    print(f'score is {game.score}')

    while True:
        if keyboard.is_pressed('right'):
            if not game.block_key("right"):
                os.system('CLS')
                print(game.press_right())
                print(f'score is {game.score}')
                time.sleep(0.5)
        if keyboard.is_pressed('left'):
            if not game.block_key("left"):
                os.system('CLS')
                print(game.press_left())
                print(f'score is {game.score}')
                time.sleep(0.5)
        if game.checker() == -1:
            break
    print("Game over!")

