import os

from utils.file_exists import file_exists
from utils.write_bson import write_bson
from utils.read_bson import read_bson
from utils.write_file import write_file
from utils.read_file import read_file

def get_table_file_name(table_name = ""):
    return "tables/" + table_name + ".bson"

def create_table(table_name = ""):
    table_filename = get_table_file_name(table_name)
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
    table_filename = get_table_file_name(table_name)
    if(not file_exists(table_filename)):
        return None
    else:
        bson = read_file(table_filename, True)
        return read_bson(bson)

def insert_row(table_name = "", row_data = {}):
    table_data = read_table(table_name)
    table_filename = get_table_file_name(table_name)
    if(not table_data):
        raise "Table could not be read."
    data_to_add = {
        **row_data,
        "uniqueId": 1234
    }
    table_data["rows"].append(data_to_add)

    table_updated = write_file(
        table_filename,
        write_bson(table_data),
        True
    )

    if(not table_updated):
        raise "Table could not be updated."
    else:
        print(table_data)
        return True