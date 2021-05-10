from lib.table import read_table

from lib.utils.read_bson import read_bson
from lib.utils.match_row_by_filters import match_row_by_filters

import json

def sum_fields(
    fields_to_sum = [],
    table_name = "",
    filters = {}
):
    matches = []
    table_data = read_table(table_name)

    sums = {}

    for field in fields_to_sum:
        sums[field] = 0

    if(not table_data or not "rows" in table_data):
        raise "Table not found."
    
    if(not len(table_data["rows"])):
        return sums   # No possible matches

    # Looking in the table for matches to filters
    for row in table_data["rows"]:
        all_filters_match = match_row_by_filters(row, filters)

        if(all_filters_match):
            matches.append(row)
            if(only_one):
                break
    
    for match in matches:
        for field in fields_to_sum:
            if field in match and float(match[field]):
                sums[field] += match[field]

    return sums