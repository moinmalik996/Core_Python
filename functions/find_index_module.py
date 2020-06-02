print('Module Imported Successfuly')

test_import = "\nFunctions are Working Nicely"


def find_index(mylist, target):
    for i, value in enumerate(mylist):
        if value == target:
            return i
    return "The Target is not in the list"
