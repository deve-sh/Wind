# Function to drop a table by deleting the file associated with it.
import os

from lib.table import get_table_file_name

def drop_table(table_name):
    table_filename = get_table_file_name(table_name)
    if os.path.exists(table_filename):
        try:
            os.remove(table_filename)
            return True
        except Exception as e:
            raise Exception("Table could not be deleted.")
    else:
        raise Exception("Table not found.")
