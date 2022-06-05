import random, os, string, pyperclip

def generateRandomChar(): # Function that returns a random ascii character 
    return random.choice(string.ascii_letters)

def generateRandomNumber(): # Function that returns a random number
    return random.randint(0, 9)

def addNumberToPassword(totalLen): # Function that returns a random number between 0 and the length of the password, this will be used to insert a number in that index in the password
    return random.randint(0, totalLen)

if __name__ == "__main__":
    os.system("clear")
    print("Password Generator")
    passwordLength = int(input("Enter password length: ")) # Input for password length
    passwordNumbers = int(input("Enter the amount of numbers in the " + str(passwordLength) + " digits password: ")) # Input for the amount of numbers in the password

    password = str()
    print("Numbers:", passwordNumbers)
    print("Password length:", passwordLength)

    for i in range(passwordLength - passwordNumbers): # Generate the random ascii letters
        password += (generateRandomChar())
  
    while (len(password) < passwordLength): # Add the determinate amount of numbers in the password
        use = addNumberToPassword(len(password))
        password = password[:use] + str(generateRandomNumber()) + password[use:]

    print(password)

    pyperclip.copy(password) # The password is copied in the clipboard
    print("Your password:", password, "its on your clipboard, you can paste it where you need!")