"""
    Current File: main.py
    Author: Nicholas Blits

    Date: 3/19/2025

    Purpose: This file determines the limits and contents of a randomly generated password.
"""

# Importing the libraries used for randomization and the manipulation of strings
import random as rand
import string as alphabet

# A method that populates a list of characters
# The method takes in a string of the letetrs allowed in a password
# The method returns the list that it populates
def initializeArray(letters: str) -> list:
    # Create an initially empty list to store all the allowed characters in
    charSet = []

    # Create and initialize a counter variable used for the method's while loop to 0
    i = 0

    while i < len(letters):
        charSet += letters[i] # Add each letter in the letters string to the list
        i += 1 # Increment the counter variable by 1

    return charSet # Return the newly populated list of characters

# A method used to determine what letters are allowed in any particular password
# THe method takes in a boolean value which determines 
# if the password should/shouldn't contain capital letters
# The method returns a list of valid characters for a password, based on user input
def determineArraySet(caps: bool) -> list:  
    # Creating an array of all the characters not allowed in the password
    # Note: All of these characters are special characters
    bannedCharacters = ["<", ">", "{", "}", "|", "/", "\\", "\'", "\"", "^", " ", ":", ";"]
    
    # Create a string variable for all the punctuation on a standard QWERTY keyboard
    specialCharacters = alphabet.punctuation
    # Creating an empty string to be used to store all special characters allowed by the program
    validCharacters = ""

    # Initialize a counter variable
    i = 0

    while i < len(specialCharacters): # Loop through each character in the punctuation string
        if bannedCharacters.__contains__(specialCharacters[i]): # Check if the letter is/isn't allowed
            i += 1 # Only increment the counter variable if it is banned
        else:
            # If it is a valid character, add it to the validCharacters string variable
            validCharacters += specialCharacters[i]   
            i += 1 # Increment the counter variable to avoid an infinite loop

    # Check if the user wants capital letters to be allowed or not
    # If allowed, add alphabet.ascii_uppercase to the string that contains valid letters
    # If capitals are not allowed, do not add the alphabet.ascii_uppercase to the string of valid letters
    if (caps == False):
        validLetters = alphabet.ascii_lowercase + alphabet.digits + validCharacters
    else:
        validLetters = alphabet.ascii_lowercase + alphabet.ascii_uppercase + alphabet.digits + validCharacters

    # Initialize a list of all the characters that the passwords can use
    passwordLetterOptions = initializeArray(validLetters)
    
    # Return the newly initialized list
    return passwordLetterOptions

# A method that creates a random index for each character in a password
# The method takes in a list of allowed characters as a parameter
# The randomly created index is returned to the method that calls this one
def randomizeCharacter(charactersList) -> int:
    # Set the final index equal to the length of the provided list minus 1
    maxIndex = len(charactersList) - 1

    # Create and return a random number between the range of the lowest possible idnex (0)
    # and the highest possible index (which is always equal to maxIndex)
    index = rand.randint(0, maxIndex)
    return index    