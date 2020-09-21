import itertools

friends = 'Bob Dante Julian Martin'.split()

def friends_teams(friends_list, team_size=2, order_does_matter=False):
    """The function takes a list of friends, a team size (2 by default) and
    an order does matter argument. It returns all possible teams. If order does
    matter is set to True the number of teams is greater"""

    # if order matters then you use permutations
    if order_does_matter:
        return list(itertools.permutations(friends_list, team_size))
    # else just use combinations because order doesn't matter
    return list(itertools.combinations(friends_list, team_size))

