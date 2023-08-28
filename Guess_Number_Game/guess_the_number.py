import random
import math

number = random.randint(0,100)

chances = 10
correct = False

def check(guess): 
    global correct
    if(guess > 100 or guess < 0):
        print("Please pick a number in the range 0-100")
    else:
        if(guess == number):
            print("You have guessed the number!")
            correct = True
        elif (guess > number):
            print("Try guessing lower.")
            correct = False
        elif (guess < number):
            print("Try guessing higher.")
            correct = False
        else:
            print("Please enter a valid number")
            correct = False
        return correct    
            
def start():
    try:
        global guess
        guess = int(input("Guess the number...   "))
        print("") 
        return guess
    except ValueError:
        print("Please type an integer to continue.  ")
        start()
        
def play():
    answer = str(input("Would you like to play a guessing game?  "))

    if answer == "no" or answer == "No":
        print("Oh okay, Maybe some other time.")
        play()
    elif answer == "yes" or answer == "Yes":
        print("Lets go!")
        print("") 
        print("I have picked a number between 1 - 100, you have 10 attempts to guess the number. Hints will be provided if the number you typed in was higher or lower than my choice.")
        print("") 
        for x in range(chances):
            start()
            check(guess)
        
            if(x == 9 and correct == False):
                print("Game Over")
                break
            elif (x == 8):
                print("") 
                print("You have one more chance.")
            elif(x == 9 or correct == True):
                if(x == 0):
                    print("") 
                    print("Congrats, It only took you "+ str(x+1) + " attempt!")
                    break
                else:
                    print("") 
                    print("Congrats, It only took you "+ str(x+1) + " attempts!")
                    break
            else:
                print("")   
    else:
        print("Sorry, I didnt get it :(")
        play()        

name = str(input("Hello, whats your name?  "))
print("") 
print("Nice to meet you " + name + ".")
print("") 

play()