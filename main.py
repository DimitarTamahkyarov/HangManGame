import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk

with open("words.txt", "r") as file:
    words = file.read().split("\n")

word = random.choice(words)
first_letter = word[0]
last_letter = word[-1]

hidden_word = ["_" if char not in [first_letter, last_letter] else char for char in list(word)]
word_result = " ".join(hidden_word).upper()

root = tk.Tk()
root.title("HangMan")
# root.geometry("400x450") This not work the same on Linux
target_word = tk.Label(root, text=word_result, font=("Roboto", 20))
target_word.pack()

counter = 7
index = 0


def button_click(char):
    if char in word:
        for i in range(len(word)):
            if word[i] == char:
                hidden_word[i] = char
        target_word["text"] = " ".join(hidden_word).upper()
        if "_" not in target_word["text"]:
            messagebox.showinfo("Info", "You win!!!")
            for button in buttons:
                button["state"] = "disabled"
    else:
        global counter
        counter -= 1
        left_tries["text"] = f"Remaining wrong attempts: {counter}"
        global index
        index += 1
        label_img["image"] = images[index]

        if counter == 0:
            messagebox.showinfo("Info", "You lost!!!")
            for button in buttons:
                button["state"] = "disabled"

    for button in buttons:
        if button["text"] == char:
            button["state"] = "disabled"


keyboard_rows = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
    ['T', 'U', 'V', 'W', 'X', 'Y', 'Z']
]

buttons = []

for row_chars in keyboard_rows:
    row_frame = tk.Frame(root)
    for char in row_chars:
        button = tk.Button(row_frame, text=char, state="normal", command=lambda c=char: button_click(c))
        button.pack(side=tk.LEFT, padx=5, pady=5)
        buttons.append(button)
    row_frame.pack()

left_tries = tk.Label(root, text=f"Remaining wrong attempts: {counter}", font=("Roboto", 10))
left_tries.pack()

images = [
    ImageTk.PhotoImage(Image.open("Screenshot_1.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_2.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_3.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_4.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_5.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_6.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_7.png")),
    ImageTk.PhotoImage(Image.open("Screenshot_8.png"))
]
label_img = tk.Label(image=images[0])
label_img.pack()

root.mainloop()
