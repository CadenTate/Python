import tkinter as tk

def on_submit():
    text = text_box.get("1.0", "end-1c")
    print("You entered:", text)

root = tk.Tk()
root.title("My GUI")

text_box = tk.Text(root)
text_box.pack()

submit_button = tk.Button(root, text="Submit",command=on_submit)
submit_button.pack()

root.mainloop()
