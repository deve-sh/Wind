from utils import (
    file_exists, 
    writebson
)

def create_table(table_name = ""):
    table_filename = table_name + ".bson"
    if(file_exists(table_filename)):
        return False
    else:
        write_file(table_filename, writebson("[]"))