def score(game):
    """Gets a bowling game scores in a list or string and returns the the total score
    Arguments:
        game = string or list of chars. Valid values each char: numbers 1-9, "x", "/", "-"
    Returns:
        integer of total score
    """
    game = game.lower()
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):
        if frame < 10:
            # Normal gameplay      
            if game[i] == "x":
                # Case "Strike"
                result += calculate_strike(game, i)
                frame += 1
                in_first_half = True

            elif game[i] == "/":
                # Case "Spare"
                result += calculate_spare(game, i)
                frame += 1
                in_first_half = True

            else:
                # Case Default
                result += get_value(game[i])
                if in_first_half is False:
                    frame += 1
                    in_first_half = True
                else:
                    in_first_half = False
        else:
            # Bonus rounds
            result += get_value(game[i])

    return result


def calculate_strike(game, i):
    """Calculates the total points for a strike 
    Arguments:
        game: list or string
        i: integer
    Result:
        integer of points to give in the current frame
    """

    if game[i+2] == '/':
        result = get_value(game[i]) + get_value(game[i+2])
    else:
        result = get_value(game[i]) + get_value(game[i+1]) + get_value(game[i+2])
   
    return result


def calculate_spare(game, i):
    """Calculates the total points for a spare
    Arguments:
        game: list or string
        i: integer
    Result:
        integer of points to give in the current frame
    """
    MAX_SCORE = 10
    result = MAX_SCORE - get_value(game[i-1]) + get_value(game[i+1])
    
    return result


def get_value(char):
    """A 1 character long string and returns the score it means
    Arguments:
        char = a 1 character long string
    Returns:
        integer value of score
    """

    SCORE_TABLE = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "x": 10,
        "/": 10,
        "-": 0,
    }

    try:
        return SCORE_TABLE[char]
    except ValueError:
        raise ValueError()
