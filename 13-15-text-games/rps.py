#All it needs to do is ask the player for their name and print some sort of 
#header telling them the title of the application.

def main():
    player_name = input('Enter your name: ')
    print_header()
    game_loop()


def print_header():
    print('-' * 50)
    print('ROCK PAPER SCISSORS GAME'.center(50))
    print('-' * 50)


def game_loop():
    pass

if __name__ == '__main__':
    main()
