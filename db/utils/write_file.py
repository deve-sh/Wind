def write_file(filename = "", contents = "", binary = False):
    try:
        file = open(filename, "w" if not binary else "wb")
        file.write(contents)
        file.close()
        return True
    except Exception as err:
        print(err)
        return False