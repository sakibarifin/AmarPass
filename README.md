
# AmarPass
#### Banglish Memorable Password Generator
#### Video Demo: https://youtu.be/5ngS6jiJ3dY

#### Description

AmarPass is a password generator and estimator for Bangla speakers. It can use wordlists of banglish words to generate passwords that are easier to remember for Bengalis.

It generates a password using a combination of the words in the list and separators which are numbers and special characters (the user can change the parameter to include uppercase letters as well).

Run the application using the following command:

$ python project.py

The app will prompt the user to input 1 or 2. If the user enters 1, than 1_avro_wordlist.txt would be selected as the banglish dictionary. And if the user input is 2, the 2_phonetic_wordlist.txt list would be selected.

Then the program will output the password. Example snap of the user's journey:

```
Hi, I will help you generate the password. First select the wordlist.

There are two wordlists available:
        1. avro_wordlist and 2. phonetic_wordlist

Enter 1 or 2. All other inputs will be ignored and the app will reprompt.
Input: 1

 = = = = = = = =
GENERATED PASSWORD
 = = = = = = = =

mongolbar#+[table_*~italiy1>#
```

### Project.db sqlite3 database schema
```
CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    times_used INTEGER NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
```

## So, why did I make it?

One major issue I face with modern password managers is that I am forced to always choose passwords that are in english or entirely random. Of course random passwords are the best but can you remember them?

I can't and I think most people are the same. Random passwords are ok if you always rely on a password manager. But even if you have 100s of passwords, you might still need to memorize 5-10 passwords or even more for increasing productivity or some other reason.

That's where my solution kicks in. It allows me or other Bangla speakers to use my own wordlist to generate a password. I want to use my own mother language for passwords that are easy to remember and secure.

### How it works

First there is the wordlist where I have listed 1000s of words that could be used like the bip 39 wordlist used in many systems. A function is used to pick 3 words. This is customizable using the word_count parameter of the bn_words() function.

The bn_words() function also can take another parameter that is the name of the wordlist. The defaults are:

```> bn_words(word_count=3, input_wordlist="1_avro_wordlist.txt")```

