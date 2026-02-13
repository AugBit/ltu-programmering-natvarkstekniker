def vote(dict, person):
    dict[person] = dict.get(person, 0) + 1


def votes(dict, person):
    score = dict.get(person, 0)
    print(score)
    return score


def result(dict):
    winner = "***OPEN***"

    if dict == {}:
        print(winner)
        return winner
    elif moreThanOneWinner(dict):
        print(winner)
        return winner

    winner = max(dict, key=dict.get)
    print(winner)
    return winner


# räknar ut om det finns mer än 1 vinnare
def moreThanOneWinner(dict):
    counter = 0
    resultToCompare = ""

    for value in dict.values():
        if resultToCompare == value:
            counter = counter + 1
        resultToCompare = value

    if counter > 0:
        return True
    else:
        return False


names = {}
vote(names, "Per")
vote(names, "Inga")
vote(names, "Per")
votes(names, "Per")
result(names)
