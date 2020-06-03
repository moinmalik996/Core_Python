import csv

with open('data.csv', 'r') as my_csv:
    field_names = ['f_name', 'l_name', 'email']
    csv_reader = csv.DictReader(my_csv, fieldnames=field_names)
    for line in csv_reader:
        print(line)
    with open('copy.csv', 'w') as my_copy:
        field_names = ['f_name', 'l_name', 'email']
        csv_writer = csv.DictWriter(my_copy, fieldnames=field_names, delimiter='\t')
        csv_writer.writeheader()
        for data in csv_reader:
            csv_writer.writerow(data)


# with open('data.csv', 'r') as my_csv:
#     csv_reader = csv.reader(my_csv, delimiter='\t')
#     for line in csv_reader:
#         print(line)
