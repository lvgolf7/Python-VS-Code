from tkinter import *
from words import *
import random

# Setup window in the center of screen
root = Tk()
root.title("Word Game!")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
scx = (screen_width // 2) - (600 // 2)
scy = (screen_height // 2) - (800 // 2)
root.geometry(f"600x800+{scx}+{scy}")
root.minsize(600, 800)
root.maxsize(600, 800)
root.iconbitmap("circle.ico")

# Variables
LETTERS1 = "QWERTYUIOP"
LETTERS2 = "ASDFGHJKL"
LETTERS3 = "ZXCVBNM"
BUTTON_COLOR = "Light Grey"
ALL_LETTERS = LETTERS1 + LETTERS2 + LETTERS3
current_guess = ""
letter_count = 0
word_list = WORDS
game_end = False


# get letter associated with the button pressed
def get_button_text(b):
    if not game_end:  # disable screen keyboard during game end, waiting for key press
        button_text = b.cget("text")
        check_letter(button_text)


# get letter associated with the key pressed
def get_key_pressed(event):
    key_pressed = event.keysym
    key_pressed = key_pressed.upper()
    check_letter(key_pressed)


# check the letter, see if it is a valid letter.
# If it is backspace, delete on screen and remove from guess.
# If it is enter and there are 5 letters in the word, first check to see if it is a valid word.
# If it is a valid word then check each letter to see if it is in the word and or placed right.


def check_letter(check_entry):
    global current_guess
    global letter_count
    if check_entry == "RETURN":
        check_entry = "ENTER"
    if check_entry == "BACKSPACE":
        check_entry = "BKSP"
    if check_entry in ALL_LETTERS and len(current_guess) != 5:
        current_guess += check_entry
        place_letter(check_entry)
        letter_count += 1
    elif (
        len(current_guess) == 5
        and check_entry == "ENTER"
        and current_guess.lower() in word_list
    ):
        check_guess(current_guess)
        current_guess = ""
    elif len(current_guess) != 0 and check_entry == "BKSP":
        letter_count -= 1
        current_guess = current_guess[:-1]
        erase_letter()


# Place letter on the grid
def place_letter(letter):
    grid_label[letter_count].config(text=letter)


# Remove letter from the grid
def erase_letter():
    grid_label[letter_count].config(text=" ")


# Check the guess to see if it is correct, has some letters right or has letters but not in right spot
def check_guess(guess):
    target = list("-----")
    temp_word = list(wordle)
    if guess == wordle:
        j = 0
        for i in range(letter_count - 5, letter_count):
            grid_label[i].config(bg="green", fg="white")
            keyboard_position = ALL_LETTERS.find(guess[j])
            letter_buttons[keyboard_position].config(bg="green", fg="white")
            j += 1
        win(True)
    else:
        n = 0
        for m in range(letter_count - 5, letter_count):
            if guess[n] == temp_word[n]:
                grid_label[m].config(bg="green", fg="white")
                keyboard_position = ALL_LETTERS.find(guess[n])
                letter_buttons[keyboard_position].config(bg="green", fg="white")
                temp_word[n] = "0"
            else:
                target[n] = guess[n]
            n += 1
        j = 0
        for i in range(letter_count - 5, letter_count):
            if target[j] in str(temp_word):
                grid_label[i].config(bg="yellow", fg="black")
                keyboard_position = ALL_LETTERS.find(guess[j])
                letter_buttons[keyboard_position].config(bg="yellow", fg="black")
            elif temp_word[j] != "0":
                grid_label[i].config(bg="light grey", fg="black")
                keyboard_position = ALL_LETTERS.find(guess[j])
                letter_buttons[keyboard_position].config(bg="grey", fg="white")
            j += 1
        if letter_count == 30:
            loss(True)


# any key to reset the game
def key_pressed(event):
    reset_game()


# Win scenario, wait for key press or menu
def win(end_game):
    global game_end
    game_end = end_game
    end_label.config(text=" " * 15 + "YOU WON!!!")
    root.bind("<Key>", key_pressed)


# Lose scenario, wait for key press or menu
def loss(end_game):
    global game_end
    game_end = end_game
    end_label.config(text=("YOU LOST!!  Word was " + wordle))
    root.bind("<Key>", key_pressed)


# Create grid and on screen keyboard
def reset_game():
    # clear variables
    global current_guess
    global grid_label
    global letter_count
    global letter_buttons
    global wordle
    global game_end
    game_end = False
    letter_buttons = []
    grid_label = []
    counter = 0
    current_guess = ""
    letter_count = 0
    end_label.config(text=" " * 30)
    root.bind("<Key>", get_key_pressed)
    # pull a random word from imported WORDS.py file
    wordle = random.choice(word_list).upper()
    # Place grid on screen
    for i in range(6):
        for j in range(5):
            grid_label.append(
                Label(
                    game,
                    text=" ",
                    borderwidth=1,
                    font=("Arial Bold", 36),
                    relief=GROOVE,
                    width=2,
                    height=1,
                )
            )
            grid_label[counter].place(x=j * 75 + 120, y=i * 80 + 50)
            counter += 1
    # Place keyboard buttons on the screen
    # first row
    for i in range(len(LETTERS1)):
        letter_buttons.append(
            Button(
                game,
                text=LETTERS1[i],
                font=("Arial Bold", 18),
                relief=FLAT,
                bg=BUTTON_COLOR,
                width=2,
                height=1,
            )
        )
    for i in range(len(LETTERS1)):
        letter_buttons[i].config(command=lambda b=letter_buttons[i]: get_button_text(b))
    for i in range(len(LETTERS1)):
        letter_buttons[i].place(x=i * 50 + 50, y=550)
    # second row
    for i in range(len(LETTERS2)):
        letter_buttons.append(
            Button(
                game,
                text=LETTERS2[i],
                font=("Arial Bold", 18),
                relief=FLAT,
                bg=BUTTON_COLOR,
                width=2,
                height=1,
            )
        )
    for i in range(len(LETTERS2)):
        letter_buttons[i + len(LETTERS1)].config(
            command=lambda b=letter_buttons[i + len(LETTERS1)]: get_button_text(b)
        )
    for i in range(len(LETTERS2)):
        letter_buttons[i + len(LETTERS1)].place(x=i * 50 + 75, y=625)
    # third row
    for i in range(len(LETTERS3)):
        letter_buttons.append(
            Button(
                game,
                text=LETTERS3[i],
                font=("Arial Bold", 18),
                relief=FLAT,
                bg=BUTTON_COLOR,
                width=2,
                height=1,
            )
        )
    for i in range(len(LETTERS3)):
        letter_buttons[i + len(LETTERS1) + len(LETTERS2)].config(
            command=lambda b=letter_buttons[
                i + len(LETTERS1) + len(LETTERS2)
            ]: get_button_text(b)
        )
    for i in range(len(LETTERS3)):
        letter_buttons[i + len(LETTERS1) + len(LETTERS2)].place(x=i * 50 + 65, y=700)
    # Place Backspace and ENTER buttons on screen
    letter_buttons.append(
        Button(
            game,
            text="BKSP",
            font=("Arial Bold", 14),
            relief=FLAT,
            bg=BUTTON_COLOR,
            width=4,
            height=1,
        )
    )
    letter_buttons[26].config(command=lambda b=letter_buttons[26]: get_button_text(b))
    letter_buttons[26].place(x=415, y=700)

    letter_buttons.append(
        Button(
            game,
            text="ENTER",
            font=("Arial Bold", 14),
            relief=FLAT,
            bg=BUTTON_COLOR,
            width=5,
            height=1,
        )
    )
    letter_buttons[27].config(command=lambda b=letter_buttons[27]: get_button_text(b))
    letter_buttons[27].place(x=480, y=700)


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="GAME OPTIONS", menu=file_menu)
file_menu.add_command(label="Play Again", command=reset_game)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Setup game frame
game = Frame(root, width=600, height=800)
game.grid(row=0, column=0)


# end label placement
end_label = Label(game, text=(" " * 30), font=("Arial Bold", 20))
end_label.place(x=100, y=510)

reset_game()


root.mainloop()
