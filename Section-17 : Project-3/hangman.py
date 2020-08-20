import random


def word_beautify(word_guess_i, word_sol_i):
    print_data = ''
    for single in word_sol_i:
        if single in word_guess_i:
            print_data += single + ' '
        else:
            print_data += '_ '
    return print_data


def print_hangman(cnt):
    if cnt == 9:
        print("  ===============  ")
    if cnt == 8:
        print("  ===============  ")
        print("         0         ")
    if cnt == 7:
        print("  ===============  ")
        print("         0         ")
        print("         |         ")
    if cnt == 6:
        print("  ===============  ")
        print("         0         ")
        print("         |         ")
        print("       /           ")
    if cnt == 5:
        print("  ===============  ")
        print("         0         ")
        print("         |         ")
        print("       /   \\       ")
    if cnt == 4:
        print("  ===============  ")
        print("      \\  0         ")
        print("         |         ")
        print("       /   \\       ")
    if cnt == 3:
        print("  ===============  ")
        print("      \\  0  /      ")
        print("         |         ")
        print("       /   \\       ")
    if cnt == 2:
        print("  ===============  ")
        print("      \\  0  /|     ")
        print("         |         ")
        print("       /   \\       ")
    if cnt == 1:
        print("  ===============  ")
        print("      \\    /|     ")
        print("         |  o     ")
        print("       /   \\       ")
        print("  ===============  ")
    if cnt == 0:
        print("------ HANGED!!! ------")


word_list = ['programming', 'coding', 'python', 'algorithm', 'computer']
valid_letters = list("qwertyuiopasdfghjklzxcvbnm")
name = input('Please enter your name : ')
print('\n-----------------------')
print(f'Welcome {name}...')
print('-----------------------\n')
word_sol = list(word_list[random.randint(0, len(word_list) - 1)])
word_guess = list()
rejected_letters = list()
chance_count = 10

while chance_count > 0:
    if sorted(set(word_guess)) == sorted(set(word_sol)):
        data = ''.join([v for v in word_sol])
        print('\n-----------------------')
        print('YOU WON')
        print(f'You have successfully guessed the word : {data}')
        print('-----------------------\n')
        break
    print(f'You have {chance_count} attempts left...')
    print(f'Word : {word_beautify(word_guess, word_sol)}')
    letter_ip = input('Enter a letter : ').lower()
    if letter_ip in valid_letters:
        if letter_ip in word_sol:
            if letter_ip not in word_guess:
                word_guess.append(letter_ip)
            else:
                print(f'--> Letter \'{letter_ip}\' is already guessed')
        else:
            if letter_ip not in rejected_letters:
                rejected_letters.append(letter_ip)
                chance_count -= 1
                print_hangman(chance_count)
            else:
                print(f'--> Letter \'{letter_ip}\' is already guessed')
    else:
        print('--> Please enter a valid letter')
else:
    print('\n-----------------------')
    print('YOU LOST')
    print('-----------------------\n')
