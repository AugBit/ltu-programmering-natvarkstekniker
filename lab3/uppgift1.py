def rovarspraket(stringToCheck):
    listOfKons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]
    word = ""

    for x in stringToCheck:
        for y in listOfKons:
            if x == y:
                letter = x + "o" + x 
                break
            else:
                letter = x

        word = word + letter

    print(word)

rovarspraket("hej")