# Gets and reads file.

def readfile(filename = ""):
    file = open(filename, "r")
    return file.read()