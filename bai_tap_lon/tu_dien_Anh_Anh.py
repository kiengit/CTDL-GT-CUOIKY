import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

def input_word(prompt):
    while True:
        try:
            word = input('Enter {}: '.format(prompt)).strip()
            if all(char.isalpha() or char.isspace() for char in word):
                return word
            else:
                print('This is not a valid word. Please re-enter.')
        except Exception as err:
            print('Error:', err)

def input_number():
    while True:
        try:
            n = int(input('Select a function to perform (0-4): '))
            if 0 <= n <= 4:
                return n
            else:
                print('This is not a valid number between 0-4. Please re-enter.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as err:
            print('Error:', err)

def add_word(dictionary):
    print('\t1.- Add word')
    word = input_word('new word')
    meanings = []
    while True:
        word_type = input_word('word type (noun, verb, adjective, etc.)')
        meaning = input_word('meaning')
        example = input_word('example')
        meanings.append([word_type, meaning, example])
        if input('Add another meaning for this word? (Y/N): ').strip().upper() != 'Y':
            break
    dictionary.append([word, meanings])
    print('New word has been added.')

def find_word(dictionary):
    print('\t2.- Find word')
    word = input_word('word to find')
    found = False
    for item in dictionary:
        if item[0].lower() == word.lower():
            print('Found word: {}'.format(word))
            for mean in item[1]:
                print('    Type    : {}'.format(mean[0]))
                print('    Meaning : {}'.format(mean[1]))
                print('    Example : {}'.format(mean[2]))
            found = True
            break
    if not found:
        print('Word "{}" not found in the dictionary.'.format(word))

def delete_word(dictionary):
    print('\t3.- Delete word')
    word = input_word('word to delete')
    found = False
    for item in dictionary:
        if item[0].lower() == word.lower():
            print('Word to delete: {}'.format(item[0]))
            dictionary.remove(item)
            found = True
            print('Word has been deleted.')
            break
    if not found:
        print('Word "{}" not found.'.format(word))

def view_all(dictionary):
    print('\t4.- View all')
    if len(dictionary) == 0:
        print('Your dictionary currently has no words. You need to add new words.')
    else:
        print('Your dictionary:')
        for item in dictionary:
            print('Word: {}'.format(item[0]))
            for mean in item[1]:
                print('    Type    : {}'.format(mean[0]))
                print('    Meaning : {}'.format(mean[1]))
                print('    Example : {}'.format(mean[2]))
            print()

def menu():
    print('-' * 40)
    print('DICTIONARY PROGRAM'.center(40, '*'))
    print('-' * 40)
    print('\t1.- Add word')
    print('\t2.- Find word')
    print('\t3.- Delete word')
    print('\t4.- View all')
    print('\t0.- Press 0 to exit the program')

def save_dictionary(file_name, dictionary):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in dictionary:
            file.write(item[0] + ',')
            for mean in item[1]:
                file.write(','.join(mean) + '|')
            file.write('\n')

def load_dictionary(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        dictionary = []
        for line in lines:
            parts = line.strip().split(',')
            word = parts[0]
            meanings = []
            for mean in parts[1].split('|'):
                mean_parts = mean.split(',')
                if len(mean_parts) == 3:
                    meanings.append(mean_parts)
            dictionary.append([word, meanings])
        return dictionary

def main():
    file_name = "mãsinhviên_mang.txt"
    dictionary = load_dictionary(file_name)
    while True:
        menu()
        choice = input_number()
        if choice == 0:
            print('Dictionary program ended')
            save_dictionary(file_name, dictionary)
            break
        elif choice == 1:
            add_word(dictionary)
        elif choice == 2:
            find_word(dictionary)
        elif choice == 3:
            delete_word(dictionary)
        elif choice == 4:
            view_all(dictionary)

if __name__ == "__main__":
    main()
