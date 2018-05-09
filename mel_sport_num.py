import json
import sys
import os
import operator
def main(argv):
    input_city_file = "data/mel_postcode_list.json"
    input_data_file = os.path.abspath(os.path.join(os.getcwd()))+"/data/Victoria_Sport_and_Recreation_Facility_Locations_2015-2016.json/data1371106444852996067.json"
    output_file_name="result/aurin_mel_sport.json"
    list_postcode = json.load(open(input_city_file))
    city_sport={key: 0 for key in list_postcode}
    data = json.load(open(input_data_file))["features"]
    for key in city_sport.keys():
        for idx,item in enumerate(data):
            try:
                a=item["properties"]["postcode"]
                if a!="None":
                    if a == int(key):
                        city_sport[key]+=1
            except:
                print item["properties"]["postcode"]
    #sorted_city_sport = sorted(city_sport.items(), key=operator.itemgetter(1),reverse=True)
    format_output=[]
    for key in city_sport.keys():
        temp={}
        temp["postcode"]=str(key)
        temp["sport_and_recreateion_facility_num"] = str(city_sport[key])
        format_output.append(temp)
    with open(output_file_name, 'w') as fp:
        json.dump(format_output, fp)
if __name__ == "__main__":
    main(sys.argv[1:])

#