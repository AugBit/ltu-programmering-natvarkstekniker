# lägga till en röst, om person inte finns ska en skapas
def vote(dict,person):
    dict[person] = dict.get(person, 0) + 1

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
print(names)