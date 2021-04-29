import bson

def write_bson(json_string = ""):
    return bson.dumps(json_string)