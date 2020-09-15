from rolls import Rock, Paper, Scissors, Player
import random


def main():
    print_header()
    rolls = build_the_three_rolls()  # create the three types of rolls
    name = get_players_name()  # ask for user's name

    player_1 = Player(name)
    player_2 = Player('Computer')
    
    # Begin the main game loop
    game_loop(player_1, player_2, rolls)

def print_header():
    print('-' * 50)
    print('ROCK PAPER SCISSORS GAME'.center(50))
    print('-' * 50)

def build_the_three_rolls():
    rolls = [Rock('Rock'),
            Paper('Paper'),
            Scissors('Scissors')]
    return rolls

def get_players_name():
    player = input('Enter your name: ').title()
    return player

def game_loop(player_1, player_2, rolls):
    count = 1  # this controls the loop
    # Variables to keep track of players' scores
    human_score, computer_score = 0, 0

    while count < 3:
        p2_roll = random.choice(rolls)  # Random computer choice

        # Validate user's choice
        while True:
            try:
                player_choice = int(input('Choose your roll:\n'
                                            '[1] Rock\n'
                                            '[2] Paper\n'
                                            '[3] Scissors\n'
                                            '> '))
                p1_roll = rolls[player_choice - 1]
                break
            except:
                print('Invalid choice')

        outcome = p1_roll.can_defeat(p2_roll.name)  # True if human wins
        
        # display both players' rolls
        print(f'Computer rolls {p2_roll.name} and {player_1.name} rolls {p1_roll.name}\n')
        
        # display winner for this round
        if outcome:
            print(f'{player_1.name} wins this round!\n')
            human_score += 1
        else:
            print(f'The computer wins this round!\n')
            computer_score += 1
        
        count += 1

    # Banner to signal game is over
    print('\n' + '-' * 50)
    print('Game Over'.center(50))

    # Work out who wins 
    print('-' * 50)
    print('SCOREBOARD'.center(50))
    print()

    print(f'\t{player_2.name}: {computer_score}\t\t{player_1.name}: {human_score}\n')
    
    if human_score > computer_score:
        print(f'{player_1.name} wins!\n')
    elif human_score == computer_score:
        print("It's a tie!\n")
    else:
        print(f'{player_2.name} wins :(\n')


# Begin program loop
if __name__ == '__main__':
    main()
