# Gets and reads file.

def readfile(filename = ""):
    file = open(filename, "r")
    fileContents = file.read()
    file.close()
    return fileContents