import random, os, string, pyperclip

def generate_random_letter(): # Function that returns a random ascii character between a-z in lowercase or uppercase
    return random.choice(string.ascii_letters)

def generate_random_number(): # Function that returns a random number
    return random.randint(0, 9)

def add_number_to_password(total_len): # Function that returns a random number between 0 and the length of the password, this will be selected_indexd to insert a number in that index in the password
    return random.randint(0, total_len)

def generate_with_input_characters():
    password = ""
    input_characters = input("Characters to use:")
    input_characters = list(input_characters)
    for i in range(len(input_characters)):
        selected = random.choice(input_characters)
        input_characters.remove(selected)
        password += selected
    return password

def generate_without_input_characters():
    password_length = int(input("Enter password length: ")) # Input for password length
    password_numbers = int(input("Enter the amount of numbers in the " + str(password_length) + " digits password: ")) # Input for the amount of numbers in the password
    password = str()
    print("Amount of numbers:", password_numbers)
    print("Password length:", password_length)
    for i in range(password_length - password_numbers): # Fill the password with the random ascii characters
        password += (generate_random_letter())
    while (len(password) < password_length): # Add the determinate amount of numbers in the password
        selected_index = add_number_to_password(len(password))
        password = password[:selected_index] + str(generate_random_number()) + password[selected_index:]
    return password


if __name__ == "__main__":
    os.system("cls")
    print("Password Generator")

    letters = input("Do you want to introduce the characters for the password? (Y/N)").upper()
    if letters == "Y":
        password = generate_with_input_characters()
    else:
        password = generate_without_input_characters()
    print(password)
    pyperclip.copy(password) # The password is copied in the clipboard
    print("Your password:", password, "its on your clipboard, you can paste it where you need!")