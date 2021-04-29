def write_file(filename = "", contents = ""):
    try:
        file = open(filename, "w")
        file.write(contents)
        file.close()
        return True
    except:
        print("Something went wrong when writing to the file.")
        return False