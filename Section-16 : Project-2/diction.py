import json
from difflib import get_close_matches


def print_pretty(word, from_dict):
    if type(from_dict) == list:
        print(f'word: {word}')
        for index, single in enumerate(from_dict):
            print(f'{index + 1}: {single}')
    else:
        print(f'word: {word}, meaning: {from_dict}')


data = json.load(open('data.json'))
input_word = input('Enter the word you want to search : ')

if input_word.lower() in data:
    print_pretty(input_word, data[input_word.lower()])
elif input_word.title() in data:
    print_pretty(input_word, data[input_word.title()])
elif input_word.upper() in data:
    print_pretty(input_word, data[input_word.upper()])
elif len(get_close_matches(input_word, data.keys())) > 0:
    matched_word = get_close_matches(input_word, data.keys())[0]
    cont = input(f'Did you mean \'{matched_word}\', press y to continue... ')
    if cont == 'y':
        print_pretty(matched_word, data[matched_word])
    else:
        print(f'Meaning for word \'{input_word}\' not found.')
else:
    print(f'Meaning for word \'{input_word}\' not found.')

exit('Program Terminated...')
