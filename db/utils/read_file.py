# Gets and reads file.

def read_file(filename = "", binary = False):
    try:
        file = open(filename, "r" if not binary else "rb")
        fileContents = file.read()
        file.close()
        return fileContents
    except:
        return None