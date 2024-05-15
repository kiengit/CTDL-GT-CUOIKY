import tkinter as tk
from tkinter import simpledialog, messagebox
import os

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("English-English Dictionary")

        self.dictionary = {}
        self.load_dictionary("mãsinhviên_mang.txt")

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        self.add_button = tk.Button(self.menu_frame, text="Add Word", command=self.add_word)
        self.add_button.pack(pady=5)

        self.find_button = tk.Button(self.menu_frame, text="Find Word", command=self.find_word)
        self.find_button.pack(pady=5)

        self.delete_button = tk.Button(self.menu_frame, text="Delete Word", command=self.delete_word)
        self.delete_button.pack(pady=5)

        self.view_button = tk.Button(self.menu_frame, text="View All", command=self.view_all)
        self.view_button.pack(pady=5)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=5)

    def add_word(self):
        word = simpledialog.askstring("Add Word", "Enter new word:")
        if word:
            meanings = []
            while True:
                word_type = simpledialog.askstring("Add Word", f"Enter word type for '{word}':")
                meaning = simpledialog.askstring("Add Word", f"Enter meaning for '{word}':")
                example = simpledialog.askstring("Add Word", f"Enter example sentence for '{word}':")
                meanings.append([word_type, meaning, example])
                if not messagebox.askyesno("Add Word", "Add another meaning for this word?"):
                    break
            self.dictionary[word] = meanings
            messagebox.showinfo("Add Word", f"New word '{word}' has been added.")

    def find_word(self):
        word = simpledialog.askstring("Find Word", "Enter word to find:")
        if word in self.dictionary:
            meanings = self.dictionary[word]
            messagebox.showinfo("Find Word", f"Found word '{word}':\n\n" + "\n".join(
                f"Type: {m[0]}\nMeaning: {m[1]}\nExample: {m[2]}\n" for m in meanings))
        else:
            messagebox.showwarning("Find Word", f"Word '{word}' not found in the dictionary.")

    def delete_word(self):
        word = simpledialog.askstring("Delete Word", "Enter word to delete:")
        if word in self.dictionary:
            del self.dictionary[word]
            messagebox.showinfo("Delete Word", f"Word '{word}' has been deleted.")
        else:
            messagebox.showwarning("Delete Word", f"Word '{word}' not found.")

    def view_all(self):
        if self.dictionary:
            all_words = "\n".join(f"Word: {word}\n" + "\n".join(
                f"    Type: {m[0]}\n    Meaning: {m[1]}\n    Example: {m[2]}\n" for m in meanings)
                                  for word, meanings in self.dictionary.items())
            messagebox.showinfo("View All Words", "Your dictionary:\n\n" + all_words)
        else:
            messagebox.showinfo("View All Words", "Your dictionary is empty.")

    def exit_program(self):
        self.save_dictionary("mãsinhviên_mang.txt")
        self.master.destroy()

    def load_dictionary(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    word = parts[0]
                    meanings = []
                    for mean in parts[1].split('|'):
                        mean_parts = mean.split(',')
                        if len(mean_parts) == 3:
                            meanings.append(mean_parts)
                    self.dictionary[word] = meanings

    def save_dictionary(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for word, meanings in self.dictionary.items():
                file.write(word + ',')
                for mean in meanings:
                    file.write(','.join(mean) + '|')
                file.write('\n')

def main():
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

