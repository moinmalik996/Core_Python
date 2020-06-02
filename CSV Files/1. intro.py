import csv


with open('data.csv', 'r') as my_csv:
    csv_reader = csv.reader(my_csv)
    with open('copy.csv', 'w') as my_copy:
        field_names = ['first_name','last_name','email']
        csv_writer = csv.writer(my_copy, field_names=field_names delimiter='-')  # delimiter is used to replace comma or space with '-'
        for line in csv_reader:
            csv_writer.writerow(line)



# with open('data.csv', 'r') as my_csv:
#     csv_reader = csv.reader(my_csv, delimiter='\t')
#     for line in csv_reader:
#         print(line)
