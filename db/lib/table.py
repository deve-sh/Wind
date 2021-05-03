import os

from uuid import uuid4

from lib.utils.file_exists import file_exists
from lib.utils.write_bson import write_bson
from lib.utils.read_bson import read_bson
from lib.utils.write_file import write_file
from lib.utils.read_file import read_file

def get_table_file_name(table_name = ""):
    return "tables/" + table_name + ".bson"

def create_table(table_name = ""):
    table_filename = get_table_file_name(table_name)
    if(file_exists(table_filename)):
        raise Exception("Table is already present.")
    else:
        # Check if tables folder exists. If not, create it.
        tables_folder_exists = os.path.exists("./tables")
        if(not tables_folder_exists):
            os.makedirs("./tables")
        
        creation_success = write_file(
            table_filename,
            write_bson({ "rows": [] }),
            True
        )
        return creation_success

def read_table(table_name = ""):
    table_filename = get_table_file_name(table_name)
    if(not file_exists(table_filename)):
        return None
    else:
        bson = read_file(table_filename, True)
        return read_bson(bson)