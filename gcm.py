import json
import re
from to_suburb import search


def getp(data):
    latitude = data["key"]["coordinates"][1]
    longitude = data["key"]["coordinates"][0]
    tup = search(latitude, longitude)
    if tup is not None:
        data["postcode"] = tup[1]
    else:
        data["postcode"] = "error"
    return data


with open("coordinates.json") as f1:
    fl = f1.readline()

with open("twt_postcode.json","w") as myfile:
    #myfile.write("{\"total_rows\":62002,\"offset\":0,\"rows\":[\n")
    myfile.write(fl) 
mydata = json.load(open('coordinates.json'))
cdlist = mydata["rows"]

result = map(getp, cdlist)

#print (result)
with open("twt_postcode.json","a") as myfile2:
    for j in result:
        if j["postcode"] != "error":       
            myin = "{k},\n".format(k=json.dumps(j))
            myfile2.write(myin)

with open("twt_postcode.json","a") as myfile:
    myfile.write("{\"value\": \"Puput\",\"address\": \"217-223 Grattan St, Carlton VIC 3053, Australia\",  \"key\": {\"coordinates\": [144.9612697, -37.8001786], \"type\": \"Point\"}, \"postcode\": \"3053\", \"id\": \"990850686521757697\"}\n]}")















