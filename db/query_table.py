from table import read_table
from utils.read_bson import read_bson
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
        all_filters_match = True
        for key in filters:
            if(not key in row or row[key] != filters[key]):
                all_filters_match = False
                break

        if(all_filters_match):
            matches.append(row)
            if(only_one):
                break
    
    filtered_matches = []

    if(len(matches) > 0 and len(select_fields.keys()) > 0):
        for match in matches:
            filtered_match = {}
            for field in match:
                if(field in select_fields and select_fields[field]):
                    filtered_match[field] = match[field]

            if(len(filtered_match.keys()) > 0):
                filtered_matches.append(filtered_match)

    print(json.dumps(filtered_matches, indent = 4))
    return matches