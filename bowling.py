def score(game):
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
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'x':
                result += get_value(game[i+1])
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
