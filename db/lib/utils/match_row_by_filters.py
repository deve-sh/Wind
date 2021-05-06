from lib.utils.get_nested_field import get_nested_field

def match_row_by_filters(row = {}, filters = {}):
    all_filters_match = True
    for key in filters:
        if("." in key):
            # If the user is using dot notations to query inner object structures.
            if(get_nested_field(row, key) != filters[key]):
                all_filters_match = False
                break
        elif(not key in row or row[key] != filters[key]):
            all_filters_match = False
            break
    return all_filters_match