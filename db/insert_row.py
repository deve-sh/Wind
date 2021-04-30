from utils.write_file import write_file
from utils.write_bson import write_bson

from table import (
    read_table,
    get_table_file_name
)
from uuid import uuid4

def generate_unique_row_id():
    return str(uuid4()).replace("-", "")[0:20]

def insert_row(table_name = "", row_data = {}):
    table_data = read_table(table_name)
    table_filename = get_table_file_name(table_name)
    if(not table_data):
        raise "Table could not be read."
    data_to_add = {
        **row_data,
        "uniqueId": generate_unique_id()
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
        return True