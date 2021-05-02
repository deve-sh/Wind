# Counts rows in a table, matching filters.

from table.read_table import read_table
from utils.match_row_by_filters import match_row_by_filters

def count_rows(table_name = "", filters = {}):
    rows = read_table(table_name)["rows"]
    count = 0

    if(len(filters.keys()) == 0):
        return len(rows)
    else:
        for row in rows:
            if(match_row_by_filters(row)):
                count += 1
    return count