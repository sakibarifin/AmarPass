
# Import all relevant modules
# Always search for modules before working on a function
# Someone else may have done it before which will likely be better than your own implementation
import random
import string
import sqlite3
import os


def main():

    # Take user input and ask the user to select the wordlist they want to use
    while True:
        print("\nHi, I will help you generate the password. First select the wordlist.")
        print("\nThere are two wordlists available: \n\t1. avro_wordlist and 2. phonetic_wordlist")
        print("\nEnter 1 or 2. All other inputs will be ignored and the app will reprompt.")
        w = input("Input: ").strip()
        if w == "1":
            selected_list = "1_avro_wordlist.txt"
            break
        if w == "2":
            selected_list = "2_phonetic_wordlist.txt"
            break

    # Get words and initialize password as an empty str
    # The first parameter which is now set as 3 may be changed to get 4, 5 or more words
    words = bn_words(3, selected_list)
    password = ""

    # Add random chars() separator to words to make the password strong
    for i in words:
        sep = chars()
        word = i
        password += word + sep

    # Nicely formating the printed output
    print(f"\n = = = = = = = = \nGENERATED PASSWORD\n = = = = = = = = \n")
    print(f"{password}\n")

    # Save the historical usage data of how many times a specific word is used in password generation
    save(words)

def chars(length=3, alpha=False, special_chars=True):

    # Get the characters from the string module
    letters = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Remove less commonly used chars
    # To ensure the pass is easier to memorize
    remove_chars = "!\"',./:;\\^`|"
    # Update special
    special = ''.join(char for char in special if char not in remove_chars)

    # Debug print the allowed chars
    # print(letters, digits, special)

    # Create the character list that are allowed in the password
    allowed_chars = digits
    if alpha:
        allowed_chars += letters
    if special_chars:
        allowed_chars += special

    # Use the allowed chars to generate a password while considering function parameters
    pwd = ""
    while len(pwd) < length:
        rand_char = random.choice(allowed_chars)
        pwd += rand_char

    # Finally, return the password
    return pwd


def bn_words(word_count=3, input_wordlist="1_avro_wordlist.txt"):

    # Check the validity of word count argument
    if not word_count:
        raise ValueError("Missing parameter.")

    # Check if the file exists
    if not os.path.exists(input_wordlist):
        raise FileNotFoundError(f"The wordlist file was not found.")

    # IMPORTANT: This function chooses the words from the input_wordlist input file
    # Make sure that all words are of at least 3 chars to ensure security of the generated passwords
    with open(input_wordlist, 'r') as file:
        # Read the words from the file into a list
        words_list = [line.strip() for line in file]

        # Check if there are at least 4 words in the list
        if len(words_list) < 4:
            raise ValueError("Insufficient words to generate a 4-word password.")

        # Choose random words equal to word_count
        selected_words = random.sample(words_list, word_count)

        # Return the words
        return selected_words


def save(words_to_save):
    # Check for errors
    if not words_to_save or len(words_to_save) < 1:
        raise ValueError("No words returned.")

    # IMPORTANT: Establish a connection to the SQLite database
    c = sqlite3.connect('project.db')
    cursor = c.cursor()

    # Loop over the list of words
    for word in words_to_save:
        # Check if the word exists in the database
        cursor.execute("SELECT word FROM words WHERE word = ?", (word,))
        check_for_word = cursor.fetchone()

        # If the word doesn't exist, create a new entry
        if check_for_word is None:
            cursor.execute("INSERT INTO words (word, times_used) VALUES (?, ?)", (word, 1))

        else:
            # If the word exists, update the times_used
            existing_word = check_for_word[0] if check_for_word else None
            if existing_word == word:
                cursor.execute("UPDATE words SET times_used = times_used + 1 WHERE word = ?", (word,))
            else:
                # Handle the case where the fetched word is not equal to the expected word
                raise Exception("Unexpected case: Fetched word is not equal to the expected word.")

    # Commit the changes and close the connection
    c.commit()
    c.close()


if __name__ == "__main__":
    main()
