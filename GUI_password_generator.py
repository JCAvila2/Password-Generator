from tkinter import *
import tkinter.font as font
import random, string, pyperclip


# Color variables
gray = "#333"
yellow = "#e2b714"
letters_color = "#d1d0c5"


# Window settings
window = Tk()
window.title("Password Generator")
window.geometry("780x640")
window.minsize(400, 400)
window.configure(bg=gray)


# Global variables
answer_font = font.Font(family = 'Impact', size = 20)
label_font = font.Font(family = 'Poppins', size = 15, weight = 'bold')
buttons_font = font.Font(family = 'Roboto', size = 15, weight = 'bold')
random_button = Button()
chosen_characters_button = Button()
password_label = Label()
password_label_input = Label()
copy_button = Button()
copy_button_input = Button()


# Functions
def generate_random_char(list_of_characters): # Function that returns a random character from a list
    return random.choice(list_of_characters)

def generate_random_number(): # Function that returns a random number
    return random.randint(0, 9)

def add_number_to_password(total_len): # Function that returns a random number between 0 and the length of the password, this will be selected_indexd to insert a number in that index in the password
    return random.randint(0, total_len)


# Functions for buttons
def add(unit, max, addition_amount, number_type): # Function to add
    actual_value = number_type(unit.get())
    if actual_value < max:
        actual_value += addition_amount
    else:
        actual_value = 0
    unit.delete(0, 'end')
    unit.insert(END, number_type(actual_value))


def sub(unit, max, addition_amount, number_type): # Function to subtract 
    actual_value = number_type(unit.get())
    if actual_value > 0:
        actual_value -= addition_amount
    else:
        actual_value = max
    unit.delete(0, 'end')
    unit.insert(END, number_type(actual_value))


def copy(password):
    pyperclip.copy(password)
    print("The password", password, "was copied into your clipboard")


# Functions to create passwords with the diferent methods
def generate_without_input_characters(password_letters, password_numbers): # Function to generate a password without determinate characters
    password_length = password_letters + password_numbers
    password = str()
    print("Amount of numbers:", password_numbers)
    print("Amount of letters:", password_letters)
    print("Total password length:", password_length)
    for i in range(password_length - password_numbers): # Fill the password with the random ascii characters
        password += (generate_random_char(string.ascii_letters))
    while (len(password) < password_length): # Add the determinate amount of numbers in the password
        selected_index = add_number_to_password(len(password))
        password = password[:selected_index] + str(generate_random_number()) + password[selected_index:]
    return password


def generate_with_input_characters(input_characters): # Function to generate a password with determinate characters
    input_characters = list(input_characters)
    password = ""
    for i in range(len(input_characters)):
        char = generate_random_char(input_characters)
        input_characters.remove(char)
        password += char
    return password


def generate_password(generate_method, pool, amount_of_letters, amount_of_numbers):
    print(generate_method, pool, amount_of_letters, amount_of_numbers)
    if generate_method == "Random":
        password_generated = generate_without_input_characters(int(amount_of_letters), int(amount_of_numbers))
        password_label.configure(text = password_generated)
    elif generate_method == "Input":
        password_generated = generate_with_input_characters(pool)
        password_label_input.configure(text = password_generated)
    print(password_generated)
    copy_button.config(text = "Copy")
    copy_button_input.config(text = "Copy")


# Generate password with random characters
random_frame = Frame(window, height = 500, width = 500, bg = gray)

amount_of_letters_label = Label(random_frame, text = "Amount of letters:", bg = gray, font = label_font, foreground = letters_color)
button_amount_of_letters_add = Button(random_frame, command = lambda : add(amount_of_letters_entry, 99, 1, int), text = "+", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)
amount_of_letters_entry = Entry(random_frame, width = 4, justify = "center", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)
amount_of_letters_entry.insert(END, "0") 
button_amount_of_letters_sub = Button(random_frame, command = lambda : sub(amount_of_letters_entry, 99, 1, int), text = "-", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)

amount_of_numbers_label = Label(random_frame, text = "Amount of numbers:", bg = gray, font = label_font, foreground = letters_color) 
button_amount_of_numbers_add = Button(random_frame, command = lambda : add(amount_of_numbers_entry, 99, 1, int), text = "+", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow) 
amount_of_numbers_entry = Entry(random_frame, width = 4, justify = "center", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow) 
amount_of_numbers_entry.insert(END, "0")
button_amount_of_numbers_sub = Button(random_frame, command = lambda : sub(amount_of_numbers_entry, 99, 1, int), text = "-", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow) 

button_generate_random = Button(random_frame, command = lambda : generate_password("Random", None, amount_of_letters_entry.get(), amount_of_numbers_entry.get()), text = "Generate", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)
password_label = Label(random_frame, text = "", bg = gray, foreground = yellow, font = answer_font)
copy_button = Button(random_frame, command = lambda: copy(password_label.cget("text")), text = "", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)

def random_frame_show(): # Place the elements in the window
    amount_of_letters_label.grid(row = 2, column = 0)
    button_amount_of_letters_add.grid(row = 1, column = 1)
    amount_of_letters_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
    button_amount_of_letters_sub.grid(row = 3, column = 1)

    amount_of_numbers_label.grid(row = 2, column = 2, padx = 10)
    button_amount_of_numbers_add.grid(row = 1, column = 3)
    amount_of_numbers_entry.grid(row = 2, column = 3, padx = 5, pady = 5)
    button_amount_of_numbers_sub.grid(row = 3, column = 3)

    password_label.grid(row = 5, column = 0, columnspan = 4, pady = 5)
    button_generate_random.grid(row = 4, column = 0, pady = 20, columnspan = 4) 
    copy_button.grid(row = 6, column = 0, pady = 5, columnspan = 4)

    random_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

def random_frame_hide(): # Hide the elements in the window
    random_frame.place_forget()


# Generate password with input characters
input_frame = Frame(window, height = 500, width = 500, bg = gray)

input_characters_label = Label(input_frame, text = "Characters:", bg = gray, font = label_font, foreground = letters_color)
input_characters_entry = Entry(input_frame, width = 15, justify = "center", font = buttons_font, highlightbackground = yellow, highlightcolor = "green", highlightthickness = 2, bd = 0, bg = gray, foreground = yellow)

button_generate_input = Button(input_frame, command = lambda : generate_password("Input", str(input_characters_entry.get()), None, None), text = "Generate", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)
password_label_input = Label(input_frame, text = "", bg = gray, foreground = yellow, font = answer_font)
copy_button_input = Button(input_frame, command = lambda: copy(password_label_input.cget("text")), text = "", font = buttons_font, highlightthickness = 0, bd = 0, bg = gray, foreground = yellow)

def input_frame_show():
    input_characters_label.grid(row = 2, column = 0, padx = 5, pady = 5)
    input_characters_entry.grid(row = 2, column = 1, padx = 5, pady = 5, columnspan = 2)

    button_generate_input.grid(row = 3, column = 1, padx = 5, pady = 5)
    password_label_input.grid(row = 4, column = 1, padx = 5, pady = 5)
    copy_button_input.grid(row = 5, column = 1, padx = 5, pady = 5)

    input_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

def input_frame_hide():
    input_frame.place_forget()




def onCheck(option): # Check which option was selected and show his frame
    copy_button.config(text = "")
    copy_button_input.config(text = "")
    if option == "Random":
        print("Selected random")
        random_button.config(bg = yellow, font = buttons_font, foreground = "black")
        chosen_characters_button.config(bg = gray, font = buttons_font, foreground = letters_color)
        input_frame_hide()
        random_frame_show()
    elif option == "Chosen characters":
        print("Selected Chosen characters")
        random_button.config(bg = gray, font = buttons_font, foreground = letters_color)
        chosen_characters_button.config(bg = yellow, font = buttons_font, foreground = "black")
        random_frame_hide()
        input_frame_show()
       

random_button = Button(window, text = "Random", command = lambda : onCheck("Random"), highlightthickness = 0, bd = 0, bg = gray, font = buttons_font, foreground = letters_color)
random_button.place(relx = 0.3, rely = 0.1, anchor = "center")

chosen_characters_button = Button(window, text = "Chose characters", command = lambda : onCheck("Chosen characters"), highlightthickness = 0, bd = 0, bg = gray, font = buttons_font, foreground = letters_color)
chosen_characters_button.place(relx = 0.7, rely = 0.1, anchor = "center")





window.mainloop()