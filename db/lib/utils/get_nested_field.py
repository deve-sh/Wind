def get_nested_field(dictionary, parts):
    """ extracts a value from a dictionary using a dotted path string """

    if type(parts) is str:
        parts = parts.split('.')

    if len(parts) > 1 and parts[0] in dictionary:
        return get_nested_field(dictionary[parts[0]], parts[1:])

    if(parts[0] not in dictionary):
        return None

    return dictionary[parts[0]]