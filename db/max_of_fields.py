# Command Line API that find the max of fields in a Database table.

import sys
import json

from lib.max_of_fields import max_fields

arguments = sys.argv

res = {
    "status": 200
}

try:
    if(len(arguments) <= 1):
        res["status"] = 400
        res["message"] = "Invalid Number of Arguments"
    else:
        receivedJSON = json.loads(arguments[1])
        filters = {}

        if(
            not receivedJSON or 
            "table_name" not in receivedJSON or 
            not receivedJSON["table_name"] or
            not isinstance(receivedJSON["table_name"], str)
        ):
            res["status"] = 400
            res["message"] = "Table name not provided."
        elif(
            "fields_to_find_max_of" not in receivedJSON or
            not isinstance(receivedJSON["fields_to_find_max_of"], list)
        ):
            res["status"] = 400
            res["message"] = "Fields to find max of not provided."
        else:
            table_name = receivedJSON["table_name"]
            
            if("filters" in receivedJSON and len(receivedJSON["filters"].keys()) > 0):
                filters = receivedJSON["filters"]
            
            fields_to_find_max_of = receivedJSON["fields_to_find_max_of"]

            maxs = max_fields(fields_to_find_max_of, table_name, filters)
            
            res["status"] = 201
            res["message"] = "Found max of fields successfully."
            res["maxs"] = maxs
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))