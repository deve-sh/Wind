def get_nested_field(dictionary, parts):
    """ extracts a value from a dictionary using a dotted path string """

    if type(parts) is str:
        parts = parts.split('.')

    if len(parts) > 1:
        return get_nested_field(dictionary[parts[0]], parts[1:])

    return dictionary[parts[0]]