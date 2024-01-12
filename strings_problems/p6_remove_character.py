def remove_character(string, target):
    new_str = ''
    for i in string:
        if i != target:
            new_str += i
    return new_str


string = 'ABCCADCHC'

string = remove_character(string, 'C')
print(string)
