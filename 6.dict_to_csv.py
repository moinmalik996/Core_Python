import csv

csv_columns = ['Title-1', 'Title-2', 'Title-3']

dict_data = [
    {'Title-1': '1', 'Title-2': 'a', 'Title-3': '08/18/07'},
    {'Title-1': '2', 'Title-2': 'b', 'Title-3': '08/18/07'},
    {'Title-1': '3', 'Title-2': 'c', 'Title-3': '08/18/07'},
    {'Title-1': '4', 'Title-2': 'd', 'Title-3': '08/18/07'},
    {'Title-1': '5', 'Title-2': 'e', 'Title-3': '08/18/07'},
    {'Title-1': '6', 'Title-2': 'f', 'Title-3': '08/18/07'},
    {'Title-1': '7', 'Title-2': 'g', 'Title-3': '08/18/07'},
    {'Title-1': '8', 'Title-2': 'h', 'Title-3': '08/18/07'},
    {'Title-1': '9', 'Title-2': 'i', 'Title-3': '08/18/07'}
]

csv_filename = "data.csv"

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O Error")