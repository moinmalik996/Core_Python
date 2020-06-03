import csv

html_output = ""
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # skip 1st and 2nd line of CSV File
    next(csv_data)
    next(csv_data)
    for lines in csv_data:
        if lines[0] == "No Reward":
            break
        names.append("{}  \t{}".format(lines[0], lines[1]))

html_output += "<p>There are currently {} public contributors </p>".format(len(names))

html_output += "\n<ul>"

for name in names:
    html_output += "\n\t<li> {} </li>".format(name)

html_output += "\n</ul>"

print(html_output)
















