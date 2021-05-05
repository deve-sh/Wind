# Command Line API that counts the matching rows in a Database table.

import sys
import json

from lib.count_rows import count_rows

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
        else:
            table_name = receivedJSON["table_name"]
            
            if("filters" in receivedJSON and len(receivedJSON["filters"].keys()) > 0):
                filters = receivedJSON["filters"]

            counted_rows = count_rows(table_name, filters)
            
            res["status"] = 201
            res["message"] = "Counted table rows successfully."
            res["count"] = counted_rows
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))