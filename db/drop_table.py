# Command Line API that creates a Database table.

import sys
import json

from lib.drop_table import drop_table

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
            dropped_table = drop_table(table_name)

            if(not dropped_table):
                raise Exception("Table could not be dropped.")
            
            res["status"] = 201
            res["message"] = "Dropped table successfully."
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))