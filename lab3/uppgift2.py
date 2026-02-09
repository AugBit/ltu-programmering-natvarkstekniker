def varannan(list):
    i = 0
    evenNames = []
    unEvenNames = []

    for name in list:
        if i % 2 == 0:
            evenNames.append(name)
            i = i + 1
        else:
            unEvenNames.append(name)
            i = i + 1
    
    allNames = (evenNames, unEvenNames)
    print(allNames)

varannan(["Maud","Marie","Mikaela","Maria","Madeleine"])