
import random

def HangmanDisplay(tries):
    dispaly = [  """
            ------
            |    |
            |    O
            |  /-+-/
            |    |
            |    |
            |   | |
            |   | |
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |  /-+-/
            |    |
            |    |
            |   |
            |   |
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |  /-+-/
            |    |
            |  
            |  
            |  
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |  /-+-/
            |  
            |  
            |  
            |  
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |  /-+-
            |  
            |  
            |  
            |  
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |   -+-
            |    
            |  
            |  
            |  
            |  
            ----------
        """,
        """
            ------
            |    |
            |    O
            |  
            |    
            |    
            |   
            |   
            |  
            ----------
        """,
        """
            ------
            |    |
            |    
            |  
            |    
            |    
            |   
            |   
            |  
            ----------
        """
    ]
    return dispaly[tries]

def get_word():
    options = [
    "Topic for your choice:", 
    "1 - musical instruments",
    "2 - film genres",
    "3 - sports",
    "4 - nature"
    ]
    for row in options:
        print(row)
    print("\n")
    choice = input("Please choose the word category you'd like to explore :")
    if int(choice) == 1:
        words = ['piano', 'flute', 'harp', 'accordion',
         'saxophone', 'drums', 'trumpet', 'bassoon',
         'cello', 'banjo', 'althorn', 'mandolin']
    if int(choice) == 2: 
        words = ['documentary', 'action', 'romance', 'western',
         'comedy', 'horror', 'thriller', 'biography',
         'historical', 'crime', 'adventure', 'crime']
    if int(choice) == 3: 
        words = ['tennis', 'volleyball', 'soccer', 'basketball',
         'badminton', 'cricket', 'golf', 'baseball',
         'archery', 'boxing', 'gymnastics', 'lacrosse']
    if int(choice) == 4:
        words = ['algae', 'birds', 'berries', 'fish',
         'flowers', 'fruits', 'insects', 'leaves',
         'minerals', 'mountains', 'sand', 'trees']
    print("The area is chosen ;)") 
    word = random.choice(words)
    return word.upper()

def game(word):
    word_length = "_" * len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("\n")
    print("Let's see how good you are at guessing")
    print(HangmanDisplay(tries))
    print(word_length)
    while not guessed and tries > 0: 
        guess = input("Give me a letter:").upper()
        if len(guess) == 1 and guess.isalpha(): 
            if guess in guessed_letters:
                print("You've guessed that letter already")
            elif guess not in word:
                print("How sad, this letter is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print("Hooray,", guess, "is in the word :)")
                guessed_letters.append(guess)
                word_list_format = list(word_length)
                indications = [i for i, letter in enumerate(word) if letter == guess]
                for index in indications:
                    word_list_format[index] = guess
                    word_length = "".join(word_list_format)
                    if "_" not in word_list_format:
                        guessed = True 
        else:
            print("This guess can not be interprited")
        print(HangmanDisplay(tries))
        print(word_length)
    if guessed:
        print("We have a WINNER!")
    else:
        print("Ops...you have no more tries left :( The word was, ", word)

def GameDisaplay():
    word = get_word()
    game(word)
    tryagain =  input("Would you like to try again?(yes/no):")
    if tryagain == "yes":
        print("\n")
        word = get_word()
        game(word)
    else: 
        print("Hope to see you soon! Goodbye :)")
        
print("\n")
name = input("Please enter your name:") 
if len(name) > 0: 
    start = print("Hi,", name, "let's play hangman!")
    print("\n")
    GameDisaplay()










