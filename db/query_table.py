from table import read_table

from utils.read_bson import read_bson
from utils.select_fields_from_dict import select_fields_from_dict
from utils.match_row_by_filters import match_row_by_filters

import json

def query_table(
    table_name = "", 
    filters = {}, 
    only_one = False, 
    select_fields = {}
):
    matches = []
    table_data = read_table(table_name)

    if(not table_data or not "rows" in table_data):
        raise "Table not found."
    
    if(not len(table_data["rows"])):
        return []   # No possible matches

    # Looking in the table for matches to filters
    for row in table_data["rows"]:
        all_filters_match = match_row_by_filters(row, filters)

        if(all_filters_match):
            matches.append(row)
            if(only_one):
                break
    
    filtered_matches = []

    if(len(matches) > 0 and len(select_fields.keys()) > 0):
        for match in matches:
            filtered_match = select_fields_from_dict(match, select_fields)
            if(filtered_match):
                filtered_matches.append(filtered_match)
    else:
        filtered_matches = matches

    if(only_one):
        if(len(filtered_matches) > 0):
            return filtered_matches[0]
        else:
            return None
    return filtered_matches