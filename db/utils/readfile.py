# Gets and reads file.

def readfile(filename = ""):
    try:
        file = open(filename, "r")
        fileContents = file.read()
        file.close()
        return fileContents
    except:
        return None