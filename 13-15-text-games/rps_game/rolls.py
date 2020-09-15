class Roll():

    def __init__(self, init_roll_name):
        self.name = init_roll_name


class Rock(Roll):
    
    def can_defeat(self, roll_name):
        if roll_name == 'Scissors':
            return True
        return False


class Paper(Roll):

    def can_defeat(self, roll_name):
        if roll_name == 'Rock':
            return True
        return False


class Scissors(Roll):

    def can_defeat(self, roll_name):
        if roll_name == 'Paper':
            return True
        return False


class Player():

    def __init__(self, init_name):
        self.name = init_name

