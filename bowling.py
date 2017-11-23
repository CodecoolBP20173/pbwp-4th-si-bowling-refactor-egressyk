def score(game):
    """Gets a bowling game scores in a list or string and returns the the total score

    Arguments:
        game = string or list of chars. Valid values each char: numbers 1-9, "x", "/", "-"

    Returns:
        integer of total score
    """

    MAX_SCORE = 10
    MAX_FRAME = 10

    game = game.lower()

    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):
        if game[i] == '/':
            result += MAX_SCORE - get_value(game[i-1])
        else:
            result += get_value(game[i])

        if frame < MAX_FRAME and get_value(game[i]) == MAX_SCORE:
            result += get_value(game[i+1])
            if game[i] == 'x':
                if game[i+2] == '/':
                    result += MAX_SCORE - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        if in_first_half is False:
            frame += 1

        if game[i] == 'x':
            in_first_half = True
            frame += 1
        else:
            in_first_half = not in_first_half

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
