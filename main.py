"""
    Current File: main.py
    Author: Nicholas Blits

    Date: 3/19/2025

    Purpose: This file creates the user interface (UI) and helps in generating a password for the user.
"""

# Implementing functions from a file that limits the password and chooses each character 
from functions import determineArraySet
from functions import randomizeCharacter

# Importing the module being used for the UI
import tkinter as screen

# Creating a global variable for the window of the UI 
# The window's title is then set to "Random Password Generator"
window = screen.Tk()
window.title("Random Password Generator")

# Creating a constant for the size of all of the text in th UI
globalFontSize = 24

# Creating two input fields for the user's password generation preferences 
lengthTextField = screen.Entry(font=globalFontSize)
capitalCaseTextField = screen.Entry(font=globalFontSize)

# Setting intial text values for each text field
lengthTextField.insert(0, "10")
capitalCaseTextField.insert(0, "Yes")

# Creating initially blank labels 
# These will be used to display the password and any error messages
passwordLabel = screen.Label(text="", fg="blue", font=globalFontSize)
errorMessageLabel = screen.Label(text="", fg="red", font=globalFontSize)

# Adding the text fields and dynamic labels to the UI
lengthTextField.grid(row=1, column=2, stick=screen.W)
capitalCaseTextField.grid(row=2, column=2, stick=screen.W)
passwordLabel.grid(row=3, column=2, stick=screen.W)
errorMessageLabel.grid(row=4, column=1, columnspan=2, stick=screen.W + screen.E)

# A method used to set the text of the errorMessageLabel Object
# This method takes in 1 string as a parameter, which is the error message
def printErrorMessage(errorMessage: str) -> None:
    errorMessageLabel["text"] = errorMessage

# A method used to make the individual prompt Labels for the UI 
# The method has 1 parameter: An integer used to keep track of what 
# the Label needs to say
# The Label is returned to the method that makes a call to it
def makeLabel(labelNumber: int) -> screen.Label:
    # Set the future Label's text to initially be an empty string
    message = ""

    # Check the value of the method's parameter
    # Depending on the value of the parameter, 
    # change the value of message to reflect what each future Label needs to say
    if labelNumber == 1:
        message = "How long do you want your password to be?: "
    elif labelNumber == 2:
        message = "Do you want capital letters in the password?: "
    else:
        message = "New password: "

    # Create a new Label element with the appropriate phrase and font size
    newLabel = screen.Label(text=message, font=globalFontSize)

    return newLabel # Return the newly created Label element

# A method that creates a new password for the user
def generatePassword() -> None:

    try: # Prevent the program from crashing due to bad input

        # Set the text for the error message's Label to an empty string
        errorMessageLabel["text"] = ""

        # Reset the value of the password variable
        password = ""

        # Create a boolean indicating if capital letters should be allowed in the password
        # Initially, capital letters are not set to appear in the password
        allowCapitals: bool = False
        
        # Check if the user wants capital letters to appear in the password
        # Set the original boolean value to match the user's input
        if capitalCaseTextField.get() == "Yes":
            allowCapitals = True
        elif capitalCaseTextField.get() == "No":
            allowCapitals = False
        else:
            # Call the method that creates error messages informing the user
            # That they used an invalid input to allow/disallow capital letters from the password
            printErrorMessage("ERROR: Only the words \"Yes\" and \"No\" are allowed in the second textbox.")

        # Create a local list of all the possible characters that can appear n the password
        charactersAllowed = determineArraySet(allowCapitals)

        # Get the input from the text field for the password's length
        # The input is cast to an object of type Integer 
        # The value of the casted input is then stored in the length variable
        length = int(lengthTextField.get())

        if length > 0: # Check if the user entered a valid value for password length

            i = 0 # Create a counter variable for the while loop

            # Run the following block of code 
            # until as many characters as the user wanted have been generated
            while i < length: 
                # Select a random index of the list of allowed characters
                letterSelector = randomizeCharacter(charactersAllowed) 
                # Concatenate the letter at the index to the password 
                password += charactersAllowed[letterSelector]
                # Increment the counter
                i += 1

            # After all of the letters have been added to the password
            # Set the passwordLabel's text attribute equal to the newly generated password
            passwordLabel["text"] = password      
        else:
            # Call the method to print out a new error message to the console
            # The error message indicates that the length value was incorrect.
            printErrorMessage("ERROR: A password of length " + str(length) + " cannot be created.")

    except ValueError:
        # Call the method to print out a new error message to the console
        # The error message indicates that they did not enter a number for the password's length.
        printErrorMessage("ERROR: A length must be a number.")

# A method that starts adding all the static elements to the UI
# The functionality of this method works the same as the main method 
# that is seen in programs built in Java and the C family languages.
def main():
    # Create a counter for the row of each new Label
    i = 1

    while i < 4: # Four Labels are made
        # Make a new Label through the makeLabel method, using i as the stand-in
        # for the method's Integer parameter
        labelToAdd = makeLabel(i)

        if i > 3: # Check which Label just got created
            # Put the fourth Label in a specific position
            labelToAdd.grid(row=3, column=2, stick=screen.W)
        else:
            # Put the first, second, and third labels in the first column
            # setting each row equal to the value of i (the counter variable)
            labelToAdd.grid(row=i, column=1, stick=screen.E)

        i += 1 # Increment i to avoid an infinite loop

    # Make the button that, when clicked, starts the process for generating a new password
    passwordButton = screen.Button(text="Generate Password", command=generatePassword, font=globalFontSize)

    # Add the button to the UI
    passwordButton.grid(row=5, column=1, columnspan=2, stick=screen.W + screen.E)

if __name__ == "__main__": # Check that a main method exists
    main() # Call main() and begin the execution of the password generator program
