import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

class LinkedListNode:
    def __init__(self, word_type, meaning, example):
        self.word_type = word_type
        self.meaning = meaning
        self.example = example
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_meaning(self, word_type, meaning, example):
        new_node = LinkedListNode(word_type, meaning, example)
        if not self.head or self.head.word_type > word_type:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.word_type <= word_type:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def get_meanings(self):
        meanings = []
        current = self.head
        while current:
            meanings.append((current.word_type, current.meaning, current.example))
            current = current.next
        return meanings

class BSTNode:
    def __init__(self, word):
        self.word = word
        self.meanings = LinkedList()
        self.left = None
        self.right = None

class BSTDictionary:
    def __init__(self):
        self.root = None

    def add_word(self, word):
        self.root = self._add_word_recursive(self.root, word)

    def _add_word_recursive(self, node, word):
        if node is None:
            return BSTNode(word)
        if word < node.word:
            node.left = self._add_word_recursive(node.left, word)
        elif word > node.word:
            node.right = self._add_word_recursive(node.right, word)
        return node

    def find_word(self, word):
        return self._find_word_recursive(self.root, word)

    def _find_word_recursive(self, node, word):
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self._find_word_recursive(node.left, word)
        return self._find_word_recursive(node.right, word)

    def delete_word(self, word):
        self.root = self._delete_word_recursive(self.root, word)

    def _delete_word_recursive(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete_word_recursive(node.left, word)
        elif word > node.word:
            node.right = self._delete_word_recursive(node.right, word)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.word = temp.word
            node.meanings = temp.meanings
            node.right = self._delete_word_recursive(node.right, temp.word)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def view_all(self):
        self._view_all_recursive(self.root)

    def _view_all_recursive(self, node):
        if node:
            self._view_all_recursive(node.left)
            print('Word: {}'.format(node.word))
            for mean in node.meanings.get_meanings():
                print('    Type    : {}'.format(mean[0]))
                print('    Meaning : {}'.format(mean[1]))
                print('    Example : {}'.format(mean[2]))
                print('\n')
            self._view_all_recursive(node.right)

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
            n = int(input('Select a function to perform (0-6): '))
            if 0 <= n <= 6:
                return n
            else:
                print('This is not a valid number between 0-6. Please re-enter.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as err:
            print('Error:', err)

def add_word(dictionary):
    print('\t1.- Add word')
    word = input_word('new word')
    node = dictionary.find_word(word)
    if node:
        print('Word already exists.')
    else:
        dictionary.add_word(word)
        node = dictionary.find_word(word)
    while True:
        word_type = input_word('word type (noun, verb, adjective, etc.)')
        meaning = input_word('meaning')
        example = input_word('example')
        node.meanings.add_meaning(word_type, meaning, example)
        if input('Add another meaning for this word? (Y/N): ').strip().upper() != 'Y':
            break
    print('New word has been added.')

def find_word(dictionary):
    print('\t2.- Find word')
    word = input_word('word to find')
    node = dictionary.find_word(word)
    if node:
        print('Found word: {}'.format(word))
        for mean in node.meanings.get_meanings():
            print('    Type    : {}'.format(mean[0]))
            print('    Meaning : {}'.format(mean[1]))
            print('    Example : {}'.format(mean[2]))
    else:
        print('Word "{}" not found in the dictionary.'.format(word))

def delete_word(dictionary):
    print('\t3.- Delete word')
    word = input_word('word to delete')
    node = dictionary.find_word(word)
    if node:
        dictionary.delete_word(word)
        print('Word has been deleted.')
    else:
        print('Word "{}" not found.'.format(word))

def view_all(dictionary):
    print('\t4.- View all')
    if dictionary.root is None:
        print('Your dictionary currently has no words. You need to add new words.')
    else:
        print('Your dictionary:')
        dictionary.view_all()

def menu():
    print('-' * 40)
    print('DICTIONARY PROGRAM'.center(40, '*'))
    print('-' * 40)
    print('\t1.- Add word')
    print('\t2.- Find word')
    print('\t3.- Delete word')
    print('\t4.- View all')
    print('\t5.- Save dictionary to file')
    print('\t6.- Load dictionary from file')
    print('\t0.- Press 0 to exit the program')

def save_dictionary(file_name, dictionary):
    with open(file_name, 'w', encoding='utf-8') as file:
        _save_recursive(file, dictionary.root)

def _save_recursive(file, node):
    if node:
        file.write(node.word + '|')
        meanings = node.meanings.get_meanings()
        for mean in meanings:
            file.write('{},{},{}|'.format(mean[0], mean[1], mean[2]))
        file.write('\n')
        _save_recursive(file, node.left)
        _save_recursive(file, node.right)

def load_dictionary(file_name):
    dictionary = BSTDictionary()
    if not os.path.exists(file_name):
        return dictionary
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Ensure it's not an empty line
                parts = line.strip().split('|')
                word = parts[0]
                dictionary.add_word(word)
                node = dictionary.find_word(word)
                for mean in parts[1:]:
                    if mean:
                        mean_parts = mean.split(',')
                        if len(mean_parts) == 3:
                            node.meanings.add_meaning(mean_parts[0], mean_parts[1], mean_parts[2])
    return dictionary

def main():
    file_name = "N21DCDT051_BST.txt"
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
        elif choice == 5:
            save_file_name = input('Enter file name to save the dictionary: ')
            save_dictionary(save_file_name, dictionary)
            print(f'Dictionary saved to {save_file_name}')
        elif choice == 6:
           
            load_file_name = input('Enter file name to load the dictionary: ')
            dictionary = load_dictionary(load_file_name)
            print(f'Dictionary loaded from {load_file_name}')

if __name__ == "__main__":
    main()
