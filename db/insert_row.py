# Command Line API that queries a Database table.

import sys
import json

from lib.insert_row import insert_row

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
        data = {}
        select_fields = {}

        if(
            not receivedJSON or 
            "table_name" not in receivedJSON or 
            not receivedJSON["table_name"] or
            not isinstance(receivedJSON["table_name"], str)
        ):
            res["status"] = 400
            res["message"] = "Table name not provided."
        elif(
            "data" not in receivedJSON or 
            not receivedJSON["data"] or
            not isinstance(receivedJSON["data"], dict)
        ):
            res["status"] = 400
            res["message"] = "Valid data not provided."
        else:
            table_name = receivedJSON["table_name"]
            data = receivedJSON["data"]

            inserted_row = insert_row(table_name, data)

            if(not inserted_row):
                raise Exception("Data could not be inserted into table.")
            
            res["status"] = 201
            res["message"] = "Data inserted successfully."
            res["data"] = data
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))