import csv

name = "Moin Malik"
age = 45
email = "moin.malik996@gmail.com"

my_dict = {
    'NAME': name,
    'AGE': age,
    'EMAIL': email
}

field_names = ['NAME', 'AGE', 'EMAIL']

with open(r'C:\Users\moinm\PycharmProjects\Core_Python\CSV Operations\info.csv', 'w', newline='') as fileObj:
    file_writer = csv.DictWriter(fileObj, fieldnames=field_names)
    file_writer.writeheader()
    for i in range(1, 10):
        file_writer.writerow(my_dict)
    fileObj.close()
