from __future__ import division
import re
import json
import sys
import os
import csv
import operator

def main(argv):
    input_twt_file_name="data/mel_postcode_list.json"
    input_abs_file_name="data/pre_2016Census_G17_VIC_POA.csv"
    output_file_name="result/ABS_mel_income.json"
    twt_data = json.load(open(input_twt_file_name,'rb'))
    mel_data=[]
    with open(input_abs_file_name, 'rb') as csvfile:
        vic_data = csv.reader(csvfile)
        list_vic_data = list(vic_data)
        for row in list_vic_data:
            if "CODE" in row[0]:
                avg_income_list=[sum(map(int,re.findall(r"\d+",row[element])))/len(re.findall(r"\d+",row[element])) for element in range(1,len(row))]
                #print avg_income_list
            else:
                for postcode in twt_data:
                    if str(postcode) in row[0]:
                        row[0]=row[0].replace("POA","")
                        row[1]=round((sum(t * c for t, c in zip(avg_income_list, map(int,row[1:len(row)])))/sum(map(int,row[1:len(row)]))),2)
                        mel_data+=[{"postcode":row[0],"average_income":str(row[1])}]
        #sorted_mel_data=sorted(mel_data, key=operator.itemgetter("average_income"))
        #sorted_mel_data = sorted(mel_data, key=lambda e: e["average_income"], reverse=True)
    with open(output_file_name, 'w') as fp:
        json.dump(mel_data, fp)

if __name__ == "__main__":
    main(sys.argv[1:])

#