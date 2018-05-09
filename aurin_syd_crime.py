import json
import sys
import os
import csv
def main(argv):
    input_file_name = "classified_twt_postcode.json"
    input_aurin_file_name=os.path.abspath(os.path.join(os.getcwd()))+"/data/Non-domestic_Assaults_and_Robberies_Sydney_lga_2013-2016.csv/data5088286021351305319.csv"
    output_file_name_aurin="result/aurin_syd_crime.json"
    output_file_name_twt = "result/cal_syd_postcode_crime.json"
    with open(input_aurin_file_name, 'rb') as csvfile:
        syd_data = csv.reader(csvfile)
        list_syd_data = list(syd_data)
        list_postcode=[item[1] for item in list_syd_data[1:]]
        unique_list_postcode=list(set(list_postcode))
        postcode_number=[{"postcode":element,"element,assaultes_and_robberies_num":str(list_postcode.count(element))} for element in unique_list_postcode]
    with open(output_file_name_aurin, 'w') as fp:
        json.dump(postcode_number, fp)
    data = json.load(open(input_file_name, 'r'))
    syd_sub_count = {i: [0, 0, 0] for i in unique_list_postcode}
    for each in data:
        if each["postcode"] != 'error':
            for key in syd_sub_count.keys():
                if key == each["postcode"]:
                    if each["sent"] == 'pos':
                        syd_sub_count[key][0] += 1
                    else:
                        syd_sub_count[key][1] += 1
    for key in syd_sub_count.keys():
        total = syd_sub_count[key][0] + syd_sub_count[key][1]
        syd_sub_count[key][2] = round(syd_sub_count[key][0] / float(total), 4)
    print len(syd_sub_count)
    sorted_syd_sub_count = sorted(syd_sub_count.items(), key=lambda e: e[1][2], reverse=True)
    output_sorted_syd_sub_count = [{"postcode":item[0],"postive_twt_rate":str(round(item[1][2],3))} for item in sorted_syd_sub_count]
    with open(output_file_name_twt, 'w') as fp:
        json.dump(output_sorted_syd_sub_count, fp)
if __name__ == "__main__":
    main(sys.argv[1:])

#