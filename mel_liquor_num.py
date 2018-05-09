import json
import sys
import os
import operator
def main(argv):
    input_city_file="data/mel_postcode_list.json"
    input_data_file = os.path.abspath(os.path.join(os.getcwd()))+"/data/Liquor_Licences__Gaming_Venues__VCGLR__2016.json/data8750121850046591027.json"
    output_file_name="result/aurin_mel_liquor.json"
    list_postcode=json.load(open(input_city_file))
    city_liquor={key: 0 for key in list_postcode}
    data = json.load(open(input_data_file))["features"]
    for key in city_liquor.keys():
        for idx,item in enumerate(data):
            try:
                a=item["properties"]["postcode"]
                if a!="None":
                    if a == int(key):
                        city_liquor[key]+=1
            except:
                print item["properties"]["postcode"]
    #sorted_city_liquor = sorted(city_liquor.items(), key=operator.itemgetter(1),reverse=True)
    format_output=[]
    for key in city_liquor.keys():
        temp={}
        temp["postcode"]=str(key)
        temp["liquor_license_num"] = str(city_liquor[key])
        format_output.append(temp)
    with open(output_file_name, 'w') as fp:
        json.dump(format_output, fp)

if __name__ == "__main__":
    main(sys.argv[1:])

#