import datetime
import time
import random
import termcolor
from termcolor import colored

#welcome user


def nam():  # name of player is entered..
    name = input("What is your name? ")
    if name.isalpha():  # condition checked for accurate name input


        print("Hello," + name, "lets have some brain storm and play hangman!")



    else:
        print(
            colored("enter your correct name sir/madam!", "blue"))  # in case of wrong choice nameis entered again..
        nam()



def level():
    print(colored("Select your level of dificulty:","red"))
    print(colored("1.Beginner","blue"))
    print(colored("2.Intermediate", "magenta"))
    print(colored("3.High", "yellow"))
    x=input("choice->")
    if x.isdigit():
        x = int(x)
        if x == 1:
            beg()


        elif x==2:
            menu2()
            med()

        elif x==3:
            menu3()
            high()

        else:
            print("enter correct choice")
            level()




def inp1():
    print(colored("you wanna try again ?enter y or Y  and to exit press any key.." ,"magenta"))  # asking player to play again.
    x = input()
    if x == "y" or x == "Y":
        menu1()  # if condition satisfied then name is asked again to start new game..

    else:
        print(colored("Thanks for playing.. see you again!!","red","on_cyan"))  # in case player wants to exit..
        exit()

def inp2():
    print(colored("you wanna try again ?enter y or Y  and to exit press any key.." ,"magenta"))  # asking player to play again.
    x = input()
    if x == "y" or x == "Y":
        menu2()  # if condition satisfied then name is asked again to start new game..

    else:
        print(colored("Thanks for playing.. see you again!!","red","on_cyan"))  # in case player wants to exit..
        exit()


def inp3():
    print(colored("you wanna try again ?enter y or Y  and to exit press any key.." ,"magenta"))  # asking player to play again.
    x = input()
    if x == "y" or x == "Y":
        menu3()  # if condition satisfied then name is asked again to start new game..

    else:
        print(colored("Thanks for playing.. see you again!!","red","on_cyan"))  # in case player wants to exit..
        exit()


def exit():  # exit function to quit the game..
    print(colored("Have a gud day !","red","on_cyan"))



def menu1():
    print("HANGMAN-The word guessing game:)-designed and developed by Gayatri(would be DECIDER!)")
    print("")
    print(colored("-----","yellow"))
    print(colored("|   |","red"))
    print(colored("|   0","red"))
    print(colored("| /-+-\ ","red"))
    print(colored("|   |","red"))
    print(colored("|   |","red"))
    print(colored("|  | |","red"))
    print(colored("|  | |","red"))
    print(colored("|","red"))
    print(colored("--------","yellow"))
    print("")

    print("Are You Ready ??")
    for x in range(1, 4):
        print(colored(x,"blue"))
        time.sleep(1)
    print(colored("Enter your choice !","green"))
    print(colored("<-------MENU------>","red"))
    print(colored("1.Movie ","magenta"))
    print(colored("2.Place","cyan"))
    print(colored("3.Spritual","magenta"))
    print(colored("4.Country","cyan"))
    print(colored("5.Exit","magenta"))
    print(colored("easy level...here you go rocking!", "magenta", "on_yellow"))
    x = input("choice->")
    if x.isdigit():
        x = int(x)
        if x == 1:
            movhang()
        elif x == 2:

            plhang()
        elif x == 3:

            sphang()
        elif x == 4:

            cohang()
        elif x == 5:
            exit()
        else:
            print("enter choice again..")
            menu1()
    else:
        print("enter choice again..")
        menu1()

def menu2():
    print("HANGMAN-The word guessing game:)-designed and developed by Gayatri(would be DECIDER!)")
    print("")
    print(colored("-----","yellow"))
    print(colored("|   |","red"))
    print(colored("|   0","red"))
    print(colored("| /-+-\ ","red"))
    print(colored("|   |","red"))
    print(colored("|   |","red"))
    print(colored("|  | |","red"))
    print(colored("|  | |","red"))
    print(colored("|","red"))
    print(colored("--------","yellow"))
    print("")

    print("Are You Ready ??")
    for x in range(1, 4):
        print(colored(x,"blue"))
        time.sleep(1)
    print(colored("Enter your choice !","green"))
    print(colored("<-------MENU------>","red"))
    print(colored("1.Movie ","magenta"))
    print(colored("2.Place", "cyan"))
    print(colored("3.Spritual", "magenta"))
    print(colored("4.Country", "cyan"))
    print(colored("5.Exit", "magenta"))
    print(colored("hope you enjoying,lets raise some level..", "magenta", "on_yellow"))
    x = input("choice->")
    if x.isdigit():
        x = int(x)
        if x == 1:

            movhang2()
        elif x == 2:

            plhang2()
        elif x == 3:

            sphang2()
        elif x == 4:

            cohang2()
        elif x == 5:
            exit()
        else:
            print("enter choice again..")
            menu2()
    else:
        print("enter choice again..")
        menu2()



def menu3():
    print("HANGMAN-The word guessing game:)-designed and developed by Gayatri(would be DECIDER!)")
    print("")
    print(colored("-----","yellow"))
    print(colored("|   |","red"))
    print(colored("|   0","red"))
    print(colored("| /-+-\ ","red"))
    print(colored("|   |","red"))
    print(colored("|   |","red"))
    print(colored("|  | |","red"))
    print(colored("|  | |","red"))
    print(colored("|","red"))
    print(colored("--------","yellow"))
    print("")

    print("Are You Ready ??")
    for x in range(1, 4):
        print(colored(x,"blue"))
        time.sleep(1)
    print(colored("Enter your choice !","green"))
    print(colored("<-------MENU------>","red"))
    print(colored("1.Movie ","magenta"))
    print(colored("2.Place","cyan"))
    print(colored("3.Spritual","magenta"))
    print(colored("4.Country","cyan"))
    print(colored("5.Exit","magenta"))
    print(colored("toughest level with only 7 chances..","magenta","on_yellow"))
    x = input("choice->")
    if x.isdigit():
        x = int(x)
        if x == 1:

            movhang3()
        elif x == 2:

            plhang3()
        elif x == 3:

            sphang3()
        elif x == 4:

            cohang3()
        elif x == 5:
            exit()
        else:
            print("enter choice again..")
            menu3()
    else:
        print("enter choice again..")
        menu3()






#1
def movhang():  # this function includes actual game to be played
    print(colored("Start guessing...", "yellow"))
    time.sleep(0.5)

    # here we set the
    list = ["raja", "darpan", "bazigar", "judva", "neerja", "sanju", "padmaavat"]
    word = random.choice(list)

    # creates an variable with an empty value
    guesses = ''

    # determine the number of turns
    turns = 10

    # Create a while loop

    # check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        fail = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char)

            else:

                # if not found, print a dash
                print("_")

                # and increase the failed counter with one
                fail += 1

                # if fail is equal to zero

        # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "magenta", "on_white"))
            inp1()

            # exit the script
            break

        print("")

        # ask the user go guess a character
        guess = input("guess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

            # turns counter decreases with 1 (now 9)
            turns -= 1

            # print wrong
            print(colored("Wrong guess", "green", attrs=["reverse"]))

            # how many turns are left
            print("You have", + turns, 'more guesses left !')

            # if the turns are equal to zero
            if turns == 0:
                # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "red", "on_yellow"))
                print("word was=", word)
                inp1()
#2
def plhang():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

    # here we set the
    list = ["kullumanali", "haridwar", "nainital", "maclodganj", "niagrafalls"]
    word = random.choice(list)

    # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                     # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "cyan", "on_grey"))
            inp1()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print("Wrong guess")

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "yellow", "on_grey"))
                print("word was=", word)
                inp1()


#3
def sphang():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

    # here we set the
    list = ["krishna", "ramayan", "vishnu", "bhagvatgita", "mahabharat"]
    word = random.choice(list)

    # creates an variable with an empty value
    guesses = ''

    # determine the number of turns
    turns = 10

    # Create a while loop

    # check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        fail = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char)

            else:

                # if not found, print a dash
                print("_")
                # and increase the failed counter with one
                fail += 1

                # if fail is equal to zero

        # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "blue", "on_yellow"))
            inp1()

            # exit the script
            break

        print("")

        # ask the user go guess a character
        guess = input("guess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

            # turns counter decreases with 1 (now 9)
            turns -= 1

            # print wrong
            print(colored("Wrong guess", "cyan"))

            # how many turns are left
            print("You have", + turns, 'more guesses left !')

            # if the turns are equal to zero
            if turns == 0:
                # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_cyan"))
                print(colored("Better luck next time..", "cyan", "on_red"))
                print("word was=", word)
                inp1()

#4
def cohang():  # this function includes actual game to be played
    print(colored("Start guessing...","blue"))
    time.sleep(0.5)

        # here we set the
    list = ["america", "india", "england", "russia", "turkey"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!","yellow","on_grey"))
            inp1()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess","yellow"))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose","red","on_grey"))
                print(colored("Better luck next time..","blue","on_yellow"))
                print("word was=", word)
                inp1()


#1
def movhang2():  # this function includes actual game to be played
    print(colored("Start guessing...", "yellow"))
    time.sleep(0.5)

        # here we set the
    list = ["angoor", "sanju", "padmaavat","anand","veerZara","october","raees","rangoon"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "magenta", "on_white"))
            inp2()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess", "green", attrs=["reverse"]))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "red", "on_yellow"))
                print("word was=", word)
                inp2()





# 2
def plhang2():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

        # here we set the
    list = ["manali", "haridwar", "gulmarg", "maclodganj", "niagrafalls","tajmahal","amerfort","hawamahal","goldentemple"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "cyan", "on_grey"))
            inp2()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print("Wrong guess")

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "yellow", "on_grey"))
                print("word was=", word)
                inp2()


#3
def sphang2():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

        # here we set the
    list = ["gayatri", "ramayan", "vishnu", "bhagvatgita", "ramazaan","guru","ibaadat","laxmi","allah","jesus"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_",end="")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "blue", "on_yellow"))
            inp2()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess", "cyan"))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_cyan"))
                print(colored("Better luck next time..", "cyan", "on_red"))
                print("word was=", word)
                inp2()


#4
def cohang2():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

        # here we set the
    list = ["scotland", "europe", "england", "pakistan", "turkey","canada","israel","italy","belgium","france"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 10

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "yellow", "on_grey"))
            inp2()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess", "yellow"))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "blue", "on_yellow"))
                print("word was=", word)
                inp2()


# 1
def movhang3():  # this function includes actual game to be played
    print(colored("Start guessing...", "yellow"))
    time.sleep(0.5)

        # here we set the
    list = ["albela","anari","devdas","dastak","namakharaam","humdono","pakeezah","guddi","sholay","junoon","anuradha"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 7

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "magenta", "on_white"))
            inp3()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess", "green", attrs=["reverse"]))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "red", "on_yellow"))
                print("word was=", word)
                inp3()


#2
def plhang3():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

        # here we set the
    list = ["machupicchu","santorini","petra","morocco","galacia","iceland","tahiti","oman","cuba"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 7

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "cyan", "on_grey"))
            inp3()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print("Wrong guess")

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time..", "yellow", "on_grey"))
                print("word was=", word)
                inp3()


#3
def sphang3():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

        # here we set the
    list = ["aesthetic","faith","cognitive","bible","ganesh","murari","anaya","devadidev","vishwamurti"]
    word = random.choice(list)

        # creates an variable with an empty value
    guesses = ''

        # determine the number of turns
    turns = 7

        # Create a while loop

        # check if the turns are more than zero
    while turns > 0:

            # make a counter that starts with zero
        fail = 0

            # for every character in secret_word
        for char in word:

                # see if the character is in the players guess
            if char in guesses:

                    # print then out the character
                print(char)

            else:

                    # if not found, print a dash
                print("_")

                    # and increase the failed counter with one
                fail += 1

                    # if fail is equal to zero

            # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "blue", "on_yellow"))
            inp3()

                # exit the script
            break

        print("")

            # ask the user go guess a character
        guess = input("guess a character:")

            # set the players guess to guesses
        guesses += guess

            # if the guess is not found in the secret word
        if guess not in word:

                # turns counter decreases with 1 (now 9)
            turns -= 1

                # print wrong
            print(colored("Wrong guess", "cyan"))

                # how many turns are left
            print("You have", + turns, 'more guesses left !')

                # if the turns are equal to zero
            if turns == 0:
                    # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_cyan"))
                print(colored("Better luck next time..", "cyan", "on_red"))
                print("word was=", word)
                inp3()



#4
def cohang3():  # this function includes actual game to be played
    print(colored("Start guessing...", "blue"))
    time.sleep(0.5)

    # here we set the
    list = ["vietnam", "syria", "cambodia", "taiwan", "qatar", "oman", "macau", "cocos"]
    word = random.choice(list)

    # creates an variable with an empty value
    guesses = ''

    # determine the number of turns
    turns = 7

    # Create a while loop

    # check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        fail = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char)

            else:

                # if not found, print a dash
                print("_", end="")

                # and increase the failed counter with one
                fail += 1

                # if fail is equal to zero

        # print You Won
        if fail == 0:
            print(colored("You won this game wohoo!!!", "yellow", "on_grey"))
            inp3()

            # exit the script
            break

        print("")

        # ask the user go guess a character
        guess = input("guess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

            # turns counter decreases with 1 (now 9)
            turns -= 1

            # print wrong
            print(colored("Wrong guess", "yellow"))

            # how many turns are left
            print("You have", + turns, 'more guesses left !')

            # if the turns are equal to zero
            if turns == 0:
                # print "You Loose"
                print(colored("Ohh ! You Loose", "red", "on_grey"))
                print(colored("Better luck next time.." , "blue", "on_yellow"))
                print("word was=",word)
                inp3()



def beg():

    menu1()

def med():

    menu2()

def high():

    menu3()



nam()
level()
