def match_row_by_filters(row = {}, filters = {}):
    all_filters_match = True
    for key in filters:
        if(not key in row or row[key] != filters[key]):
            all_filters_match = False
            break
    return all_filters_match