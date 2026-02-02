import sys

def get_file_content(oldFilename):
    file = open(oldFilename, "r") 
    content = file.read()
    file.close()
    return content

def copyIntoNewFile(oldFilename, newFilename, wordToReplace, wordToReplaceWith):
    text = get_file_content(oldFilename)
    text = text.replace(wordToReplace, wordToReplaceWith)
    
    with open(newFilename,"w") as file:
        file.write(text)


oldFilename = sys.argv[1]
newFilename = sys.argv[2]
wordToReplace = sys.argv[3]
wordToReplaceWith = sys.argv[4]

copyIntoNewFile(oldFilename, newFilename, wordToReplace, wordToReplaceWith)
# python3 uppgift3.py oldFile.txt newFile.txt hello goodbye 
