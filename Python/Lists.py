# 1.
# Complete the function below according to its docstring.

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    pass
    if len(L) < 2:
        return None

    return L[1]


# 2.
# You are analyzing sports teams. Members of each team are stored in a list.
# The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that.
# These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.
# Complete the function below to select the captain of the worst team.

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    pass
    return teams[-1][1]


