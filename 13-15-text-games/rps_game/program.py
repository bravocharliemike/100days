from actors import Rock, Paper, Scissors, Player
import random


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player_1 = Player(name)
    player_2 = Player('computer')

    game_loop(player_1, player_2, rolls)


def print_header():
    print('-' * 50)
    print('ROCK PAPER SCISSORS GAME'.center(50))
    print('-' * 50)


def build_the_three_rolls():
    rolls = [
            Rock('Rock'),
            Paper('Paper'),
            Scissors('Scissors')
            ]
    return rolls

def get_players_name():
    player = input('Enter your name: ')
    return player


def game_loop(player_1, player_2, rolls):
    count = 1
    while count < 3:
        print(f'!!! The loop count is now {count}')
        p2_roll = random.choice(rolls)
        print(f'!!! The computer chose {p2_roll.name}')
        player_choice = int(input('Choose your roll:\n' 
            '[1] Rock\n'
            '[2] Paper\n'
            '[3] Scissors\n'))
        
        if player_choice == 1:
            p1_roll = rolls[0]
        elif player_choice == 2:
            p1_roll = rolls[1]
        elif player_choice == 3:
            p1_roll = rolls[2]
        else:
            print('Invalid choice')

        outcome = p1_roll.can_defeat(p2_roll.name)
        
        human_score, computer_score = 0, 0
        # display throws
        print(f'Computer rolls {p2_roll.name} and {player_1.name} rolls {p1_roll.name}')
        # display winner for this round
        if outcome:
            print(f'Player {player_1.name} wins!')
            human_score += 1
            print(f'!!! The human score is now {human_score}')
        else:
            print(f'The computer wins')
            computer_score += 1
            print(f'!!! The computer score is now {computer_score}')
        count += 1

    # Decide who won
    print('\n' + '-' * 50)
    print('Game Over'.center(50))
    print('-' * 50)       

    if human_score > computer_score:
        print(f'{player_1.name} wins!')
    else:
        print(f'{player_2.name} wins :(')


# Begin program
if __name__ == '__main__':
    main()
