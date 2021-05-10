from lib.table import read_table

from lib.utils.read_bson import read_bson
from lib.utils.match_row_by_filters import match_row_by_filters

def min_fields(
    fields_to_find_min_of = [],
    table_name = "",
    filters = {}
):
    matches = []
    table_data = read_table(table_name)

    mins = {}

    for field in fields_to_find_min_of:
        mins[field] = None

    if(not table_data or not "rows" in table_data):
        raise "Table not found."
    
    if(not len(table_data["rows"])):
        return mins   # No possible matches

    # Looking in the table for matches to filters
    for row in table_data["rows"]:
        all_filters_match = match_row_by_filters(row, filters)

        if(all_filters_match):
            matches.append(row)
    
    for match in matches:
        for field in fields_to_find_max_of:
            if(
                field in match and 
                float(match[field]) and 
                (mins[field] == None or mins[field] > float(match[field]))
            ):
                mins[field] = float(match[field])

    return mins