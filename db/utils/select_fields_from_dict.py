def select_fields_from_dict(dictionary = {}, fields_to_select = {}):
    filtered_match = {}
    for field in dictionary:
        if(field in fields_to_select and fields_to_select[field]):
            filtered_match[field] = dictionary[field]

    if(len(filtered_match.keys()) > 0):
        return filtered_match
    return None