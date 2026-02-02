def get_file_content(filename):
    file = open(filename, "r") 
    content = file.read()   
    print(content)
    file.close()
    return content
    
get_file_content("oldFile.txt")
