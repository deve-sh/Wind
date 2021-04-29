import os

from utils.file_exists import file_exists
from utils.write_bson import write_bson
from utils.read_bson import read_bson
from utils.write_file import write_file
from utils.read_file import read_file

def create_table(table_name = ""):
    table_filename = "tables/" + table_name + ".bson"
    if(file_exists(table_filename)):
        return False
    else:
        # Check if tables folder exists. If not, create it.
        tables_folder_exists = os.path.exists("./tables")
        if(not tables_folder_exists):
            print("Folder does not exist.")
            os.makedirs("./tables")
        
        creation_success = write_file(
            table_filename,
            write_bson({ "rows": [] }),
            True
        )
        return creation_success

def read_table(table_name = ""):
    table_filename = "tables/" + table_name + ".bson"
    if(not file_exists(table_filename)):
        return False
    else:
        bson = read_file(table_filename, True)
        return read_bson(bson)