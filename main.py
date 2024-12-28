#color memory game
import random
from colorama import Fore
#a list of colors that can be expanded
colors=["red","blue","yellow"]
guesses=[]
correctColors=[]
numCorrect=0
total=0
def chooseDifficulty():
    global numCorrect,total,guesses,correctColors
    # resetting all the variables
    numCorrect=0
    total=0
    guesses=[]
    correctColors=[]
    #user chooses difficulty
    difficulty=int(input("Do you want to do level 1,2, or 3:"))
    if difficulty==1:
        colorGuess(3,False)
        check(guesses,correctColors,total)
        chooseDifficulty()
    elif difficulty==2:
        colorGuess(3,True)
        check(guesses,correctColors,total)
        chooseDifficulty()
    elif difficulty==3:
        colorGuess(6,True)
        check(guesses,correctColors,total)
        chooseDifficulty()
def colorGuess(length,colorText):
    global total,guesses,correctColors
    for i in range(length):
        total += 1
        ranNum = random.randint(0, 2)
        correctColors.append(colors[ranNum])
        if colorText:
            #random text color
            ranColor = random.randint(0, 2)
            #Fore is a library i found for changing text color
            #i found it on https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
            #only used to add a unique feature into my code and i didnt copy any code
            if ranColor == 0:
                print(f"Color {i + 1}:" + Fore.RED + f"{colors[ranNum]}")
            elif ranColor == 1:
                print(f"Color {i + 1}:" + Fore.BLUE + f"{colors[ranNum]}")
            elif ranColor == 2:
                print(f"Color {i + 1}:" + Fore.YELLOW + f"{colors[ranNum]}")
        else:
            # the f allows me to put variables in my text using {}
            #found when i was coding in the past
            print(f"Color {i + 1}: {colors[ranNum]}")
        move = False
        while move == False:
            choice = input(Fore.LIGHTWHITE_EX + "Are you ready to move on (y or n)")
            if choice == "y":
                move = True
                #adds a space in between the displayed colors isnt able to see the correct answer unless the cheat and scroll up
                for i in range(50):
                    print("")
    for i in range(len(correctColors)):
        guesses.append(input(f"What was color {i + 1}:"))
#used to check if the guess is correct
def check(guess,correct,max):
    global numCorrect
    for i in range(len(guess)):
        if guess[i]==correct[i]:
            numCorrect+=1
    #prints the results
    print("You got", numCorrect, "correct out of",max)
    print("Percent:",numCorrect/max*100,"%")
def main():
    chooseDifficulty()
main()


