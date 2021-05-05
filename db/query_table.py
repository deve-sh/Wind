# Command Line API that queries a Database table.

import sys
import json

from lib.query_table import query_table

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
        only_one = False
        select_fields = {}

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
            
            if("only_one" in receivedJSON and receivedJSON["only_one"]):
                only_one = receivedJSON["only_one"]

            if("select_fields" in receivedJSON and len(receivedJSON["select_fields"].keys()) > 0):
                select_fields = receivedJSON["select_fields"]

            queried_table = query_table(table_name, filters, only_one, select_fields)

            if(not isinstance(queried_table, list) and not queried_table):
                raise Exception("Table could not be queried.")
            
            res["status"] = 201
            res["message"] = "Queried table successfully."
            res["data"] = queried_table
except Exception as e:
    res["status"] = 500
    res["message"] = str(e)

print(json.dumps(res))