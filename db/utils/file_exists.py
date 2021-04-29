import pathlib

def file_exists(filename = ""):
    file = pathlib.Path(filename)
    return file.exists()