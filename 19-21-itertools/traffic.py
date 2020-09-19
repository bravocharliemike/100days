import random
import itertools
import time

def main():
    lights = 'red amber green'
    traffic = itertools.cycle(lights.split())
    pause = random.randint(3, 6)

    for color in traffic:
        if color == 'amber':
            print(f'Attention, the light is {color}')
            time.sleep(2)
        elif color == 'red':
            print(f'STOP!, the light is {color}')
            time.sleep(pause)
        elif color == 'green':
            print(f'You may proceed, the light is {color}')
            time.sleep(pause)


if __name__ == '__main__':
    main()
