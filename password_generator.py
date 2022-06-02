import random, os, string, pyperclip

def generateRandomChar():
    return random.choice(string.ascii_letters)

def generateRandomNumber():
    return random.randint(0, 9)

def addNumberToPassword(totalLen):
    return random.randint(0, totalLen)

if __name__ == "__main__":
    os.system("clear")
    print("Password Generator")
    passwordLength = int(input("Enter password length: "))
    passwordNumbers = int(input("Enter the amount of numbers in the " + str(passwordLength) + " digits password: "))

    password = str()
    print("Numbers:", passwordNumbers)
    print("Password length:", passwordLength)

    for i in range(passwordLength - passwordNumbers):
        password += (generateRandomChar())
  
    while (len(password) < passwordLength):
        use = addNumberToPassword(len(password))
        password = password[:use] + str(generateRandomNumber()) + password[use:]

    print(password)

    pyperclip.copy(password)
    print("Your password:", password, "its on your clipboard, you can paste it where you need!")