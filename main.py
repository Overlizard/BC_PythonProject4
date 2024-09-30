'''define the function that I'll use to take the strings and reverse them'''
def concat_strings_in_reverse(string1, string2, string3):
    new_string = string3 + string2 + string1
    return new_string

if __name__ == __main__:
    string1 = input('type in a string: ')
    string2 = input('give me a 2nd string: ')
    string3 = input('give me a 3rd string: ')

'''output the three inputs and then call the function'''
    print(f'The threes strings given are \'{string1}\', \'{string2}\', and \'{string3}\'.\n'
          f'Concatenated and reversed, they look like {concat_strings_in_reverse(string1, string2, string3)}')