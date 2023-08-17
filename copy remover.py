import os
import tkinter as tk
from tkinter import filedialog


def delete_files():
    # Get the selected directory path
    directory_path = directory_path_var.get()
    # Get the search word
    search_word = search_word_var.get()
    # Loop through all the files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file name contains the search word
        if search_word in filename:
            # If it does, delete the file
            os.remove(os.path.join(directory_path, filename))
    # Show a message box when the deletion is complete
    tk.messagebox.showinfo("Deletion Complete", "All files containing '" + search_word + "' have been deleted.")


def select_directory():
    # Open a file dialog to select a directory
    directory_path = filedialog.askdirectory()
    # Update the directory path variable
    directory_path_var.set(directory_path)


# Create the GUI window
window = tk.Tk()
window.title("File Deletion Tool")

# Create a label and entry box for the directory path
directory_path_label = tk.Label(window, text="Directory Path:")
directory_path_label.grid(row=0, column=0)
directory_path_var = tk.StringVar()
directory_path_entry = tk.Entry(window, textvariable=directory_path_var)
directory_path_entry.grid(row=0, column=1)
directory_path_button = tk.Button(window, text="Select Directory", command=select_directory)
directory_path_button.grid(row=0, column=2)

# Create a label and entry box for the search word
search_word_label = tk.Label(window, text="Search Word:")
search_word_label.grid(row=1, column=0)
search_word_var = tk.StringVar()
search_word_entry = tk.Entry(window, textvariable=search_word_var)
search_word_entry.grid(row=1, column=1)

# Create a button to delete the files
delete_button = tk.Button(window, text="Delete Files", command=delete_files)
delete_button.grid(row=2, column=1)

# Run the GUI loop
window.mainloop()
