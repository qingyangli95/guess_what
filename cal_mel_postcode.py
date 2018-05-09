import json
import sys

FILTER_NUM = 100  # number of twitters at least in one suburb


def main(argv):
    input_file_name = "classified_twt_postcode.json"
    input_postcode_list="data/mel_postcode_list.json"
    postcode_list=json.load(open(input_postcode_list, 'r'))
    output_file_name = "result/cal_mel_postcode.json"
    data = json.load(open(input_file_name, 'r'))
    mel_sub_count = {i: [0, 0, 0] for i in range(3000, 3797)}
    for each in data:
        if each["postcode"] != 'error':
            for key in mel_sub_count.keys():
                if key == int(each["postcode"]):
                    if each["sent"] == 'pos':
                        mel_sub_count[key][0] += 1
                    else:
                        mel_sub_count[key][1] += 1
    for key in mel_sub_count.keys():
        total = mel_sub_count[key][0] + mel_sub_count[key][1]
        if key in postcode_list:
            if total==0:
                mel_sub_count[key][2]=0
            else:
                mel_sub_count[key][2] = round(mel_sub_count[key][0] / float(total), 4)
        else:
            del mel_sub_count[key]
    print len(mel_sub_count)

    sorted_mel_sub_count = sorted(mel_sub_count.items(), key=lambda e: e[1][2], reverse=True)
    output_sorted_mel_sub_count = [{"postcode": str(item[0]), "postive_twt_rate": str(item[1][2])} for item in
                                   sorted_mel_sub_count]
    #output_postcode = [item[0] for item in sorted_mel_sub_count]
    with open(output_file_name, 'w') as fp:
        json.dump(output_sorted_mel_sub_count, fp)
    #with open(output_postcode_file_name, 'w') as fp:
        #json.dump(output_postcode, fp)


if __name__ == "__main__":
    main(sys.argv[1:])

    #
