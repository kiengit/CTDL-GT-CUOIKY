import tkinter as tk
from tkinter import messagebox, filedialog
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
        words = []
        self._view_all_recursive(self.root, words)
        return words

    def _view_all_recursive(self, node, words):
        if node:
            self._view_all_recursive(node.left, words)
            word_data = {'word': node.word, 'meanings': node.meanings.get_meanings()}
            words.append(word_data)
            self._view_all_recursive(node.right, words)

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
            if line.strip():
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

class DictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Dictionary App')
        self.dictionary = load_dictionary('N21DCDT051_BST.txt')

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        self.word_label = tk.Label(frame, text='Word:')
        self.word_label.grid(row=0, column=0, padx=5, pady=5)
        self.word_entry = tk.Entry(frame)
        self.word_entry.grid(row=0, column=1, padx=5, pady=5)

        self.type_label = tk.Label(frame, text='Type:')
        self.type_label.grid(row=1, column=0, padx=5, pady=5)
        self.type_entry = tk.Entry(frame)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        self.meaning_label = tk.Label(frame, text='Meaning:')
        self.meaning_label.grid(row=2, column=0, padx=5, pady=5)
        self.meaning_entry = tk.Entry(frame)
        self.meaning_entry.grid(row=2, column=1, padx=5, pady=5)

        self.example_label = tk.Label(frame, text='Example:')
        self.example_label.grid(row=3, column=0, padx=5, pady=5)
        self.example_entry = tk.Entry(frame)
        self.example_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_meaning_button = tk.Button(frame, text='Add Meaning', command=self.add_meaning)
        self.add_meaning_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.add_word_button = tk.Button(frame, text='Add Word', command=self.add_word)
        self.add_word_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.find_button = tk.Button(frame, text='Find Word', command=self.find_word)
        self.find_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(frame, text='Delete Word', command=self.delete_word)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.view_all_button = tk.Button(frame, text='View All Words', command=self.view_all)
        self.view_all_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.save_button = tk.Button(frame, text='Save Dictionary', command=self.save_dictionary)
        self.save_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.load_button = tk.Button(frame, text='Load Dictionary', command=self.load_dictionary)
        self.load_button.grid(row=10, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(self.root, width=80, height=20)
        self.output_text.pack(pady=20)

    def add_meaning(self):
        word = self.word_entry.get().strip()
        word_type = self.type_entry.get().strip()
        meaning = self.meaning_entry.get().strip()
        example = self.example_entry.get().strip()

        if not word or not word_type or not meaning or not example:
            messagebox.showerror('Input Error', 'All fields are required.')
            return

        node = self.dictionary.find_word(word)
        if node:
            node.meanings.add_meaning(word_type, meaning, example)
            messagebox.showinfo('Meaning Added', f'Added meaning to existing word "{word}".')
        else:
            messagebox.showerror('Word Not Found', f'Word "{word}" not found. Please add the word first.')

        self.clear_entries()

    def add_word(self):
        word = self.word_entry.get().strip()
        if not word:
            messagebox.showerror('Input Error', 'Word field is required.')
            return

        node = self.dictionary.find_word(word)
        if node:
            messagebox.showinfo('Word Exists', f'Word "{word}" already exists. You can add more meanings to it.')
        else:
            self.dictionary.add_word(word)
            node = self.dictionary.find_word(word)
            messagebox.showinfo('Word Added', f'New word "{word}" added. Now you can add meanings.')

        self.clear_entries()

    def find_word(self):
        word = self.word_entry.get().strip()
        if not word:
            messagebox.showerror('Input Error', 'Word field is required.')
            return

        node = self.dictionary.find_word(word)
        self.output_text.delete(1.0, tk.END)
        if node:
            self.output_text.insert(tk.END, f'Found word: {word}\n')
            for mean in node.meanings.get_meanings():
                self.output_text.insert(tk.END, f'    Type    : {mean[0]}\n')
                self.output_text.insert(tk.END, f'    Meaning : {mean[1]}\n')
                self.output_text.insert(tk.END, f'    Example : {mean[2]}\n\n')
        else:
            self.output_text.insert(tk.END, f'Word "{word}" not found in the dictionary.\n')

    def delete_word(self):
        word = self.word_entry.get().strip()
        if not word:
            messagebox.showerror('Input Error', 'Word field is required.')
            return

        node = self.dictionary.find_word(word)
        if node:
            self.dictionary.delete_word(word)
            messagebox.showinfo('Word Deleted', f'Word "{word}" has been deleted.')
        else:
            messagebox.showinfo('Word Not Found', f'Word "{word}" not found in the dictionary.')

    def view_all(self):
        words = self.dictionary.view_all()
        self.output_text.delete(1.0, tk.END)
        for word_data in words:
            self.output_text.insert(tk.END, f'Word: {word_data["word"]}\n')
            for mean in word_data['meanings']:
                self.output_text.insert(tk.END, f'    Type    : {mean[0]}\n')
                self.output_text.insert(tk.END, f'    Meaning : {mean[1]}\n')
                self.output_text.insert(tk.END, f'    Example : {mean[2]}\n\n')

    def save_dictionary(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_name:
            save_dictionary(file_name, self.dictionary)
            messagebox.showinfo('Dictionary Saved', f'Dictionary saved to {file_name}.')

    def load_dictionary(self):
        file_name = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_name:
            self.dictionary = load_dictionary(file_name)
            messagebox.showinfo('Dictionary Loaded', f'Dictionary loaded from {file_name}.')

    def clear_entries(self):
        self.word_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.meaning_entry.delete(0, tk.END)
        self.example_entry.delete(0, tk.END)

    def on_closing(self):
        save_dictionary('N21DCDT051_BST.txt', self.dictionary)
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
