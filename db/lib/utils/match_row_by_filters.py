from lib.utils.get_nested_field import get_nested_field

reserved_querying_filters = ["_or"]
reserved_membership_filters = ["_in", "_nin", "_includes"]

def match_row_by_filters(row = {}, filters = {}):
    all_filters_match = True
    for key in filters:
        if("." in key):
            # If the user is using dot notations to query inner object structures.
            value_to_match = get_nested_field(row, key)
            if(value_to_match != filters[key]):
                all_filters_match = False
                break
        elif(not key in row or row[key] != filters[key]):
            all_filters_match = False
            break
    return all_filters_match