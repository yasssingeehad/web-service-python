import csv


with open('external_id_type.csv' , 'r')as external_id_file:
    external_id_csv = csv.reader(external_id_file)
    external_id_dict = {}
    for i in external_id_csv:
        external_id_dict[i[0]] = i[2]
    # print(external_id_dict)
    
    print("The external ID type for 211 is " , external_id_dict['211'])