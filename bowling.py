def score(game):
    game = game.lower()
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        last = get_value(game[i])

        if in_first_half is False:
            frame += 1

        in_first_half = not in_first_half

        if game[i] == 'x':
            in_first_half = True
            frame += 1

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
