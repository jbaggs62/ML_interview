import json
import csv

# Function to convert a CSV to JSON
# Takes the file paths as arguments
reader = csv.DictReader(open("testjson.csv"))
dictobj = next(reader)
json_object = json.dumps(dictobj, indent=4)

print(json_object)