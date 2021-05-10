# Command Line API that counts the matching rows in a Database table.

import sys
import json

from lib.sum_fields import sum_fields

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
            "fields_to_sum" not in receivedJSON or
            not isinstance(receivedJSON["fields_to_sum"], list)
        ):
            res["status"] = 400
            res["message"] = "Fields to Sum Not provided."
        else:
            table_name = receivedJSON["table_name"]
            
            if("filters" in receivedJSON and len(receivedJSON["filters"].keys()) > 0):
                filters = receivedJSON["filters"]
            
            fields_to_sum = receivedJSON["fields_to_sum"]

            sums = sum_fields(fields_to_sum, table_name, filters)
            
            res["status"] = 201
            res["message"] = "Summed fields successfully."
            res["sums"] = sums
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))