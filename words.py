def print_uppercase(list_of_words):
    """ will print each word from list in upper case """
    for word in list_of_words:
        print(word.upper())

print_uppercase(['practice', 'words', 'for', 'testing'])



def print_e_words(list_of_words):
    """ will print only the words that start with the letter E from a list of words """
    for word in list_of_words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

print_e_words(["hello", "hey", "elephant", "goodbye", "yo", "eagle", "yes"])




def print_upper_words(list_of_words, must_start_with):
    """Will print an upper case version of each word that starts with a 
    given character 
    """
    for char in must_start_with:
        for word in list_of_words:
            if word[0] == char:
                print(word.upper())


# For example:
# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "elephant", "goodbye", "yo", "eagle", "yes"], 
                    must_start_with={"h", "y"})



