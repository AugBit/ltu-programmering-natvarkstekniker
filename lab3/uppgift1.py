# skapa lista som innehåller alla konsonanter
# konsonanter ska dubblas runt vokal tex: "h" blir hoh

# iterera igenom varje bokstav i en sträng, kolla om bokstav finns i listan med konsonanter 
 
# om den finns, gör så att det blir ett h framför och h bakom 

listOfKons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
stringToCheck = "hej"
stringToModify = ""
addChar = True

for x in stringToCheck:
    if addChar == True:
        print(x)
    addChar = True
    for y in listOfKons:
        #print(x, " : ", y)
        if x == y:
            print("h" + x + "h")
            addChar = False
            


print(stringToModify)