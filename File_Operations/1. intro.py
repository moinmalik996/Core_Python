# file = open('text.txt', 'r')
# print(file.mode)
# file.close()

# copying one file to another

with open('text.txt', 'r') as read_file:
    with open('text-copy.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)
    # content = myfile.read(100)   # it will print only 100 characters
    # print(content, end='')
    # for line in myfile:
    # print(line, end='\n')
