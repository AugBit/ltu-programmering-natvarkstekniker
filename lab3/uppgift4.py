# lägga till en röst, om person inte finns ska en skapas
def vote(dict,person):
    if person in dict:
        dict[person] = dict.get(person) + 1

    else:
        print("not found ")
        dict[person] = 1
    print(dict)


# returnera antalet röster på person, om person inte finns returnera 0
def votes(dict,person):
    pass

# returnera namnet på person med flest röster, om inte finns returnera ***OPEN***
def result(dict):
    pass

# skapa dictionary som innehåller: key = namn, value = antalet röster
names = {}
vote(names, "pedro")
vote(names, "pedro")
vote(names, "pedro")