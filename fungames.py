##Program to simulate two games: Cornhole and Guessing Medals

from random import randint

def main():
    play = True
    while play:                                                             #iterates until user doesn't quit
        print("Choose 1 or 2 to play one of the following games, or 3 to quit playing\n1. Cornehole\n2. Guessing Medals\n3. Quit")
        choice = input("Enter your  choice: ")
        if choice == '1':
            cornhole()
        elif choice == '2':
            guessMedal()
        elif choice == '3':
            print("Goodbye. Hope you enjoyed playing!")
            play = False
        else:
            print("Please enter the valid choice")

            
#cornhole function to play cornhole            
def cornhole():
    userPoint = 0                                                               #@userPoint calculates points of the user
    for i in range(0,4):
        color = input("Enter the coolour of the baggie you are throwing\n(red/yellow/blue/green): ")
        hole = randint(0,4)                                                     #@hole generates random number from 0 to 4 to know landing area of the bag
        userPoint = computerTossPoints(color, hole) + userPoint                 #invokes computerTossPoints and updates points of the user 
    printWinner(userPoint)                                                      #invokes printWinner funtion

#computerTOssPoints function calcutes the points of the user    
def computerTossPoints(color, hole):
    if color == 'red' and hole == 1:
        point = 10
    elif color != 'red' and hole == 1:
        point = 8
    elif color != 'yellow' and hole == 2:
        point = 3
    elif color == 'yellow' and hole == 2:
        point = 6
    elif color != 'blue' and hole == 3:
        point = 2
    elif color == 'blue' and hole == 3:
        point = 4
    elif color != 'green' and hole == 4:
        point = 1
    elif color == 'green' and hole == 4:
        point = 2
    else:
        point = 0
    return point

#printWinner function prints the winner of game cornHole
def printWinner(userPoint):
    computerPoint = randint(0,34)       #@computerPoint generates the random number from 0 to 34 
    gap = computerPoint - userPoint     #@gap calculates difference in computerPoint and userPoint
    print("User point:",userPoint)
    print("Computer point:",computerPoint)
    if gap > 0:
        print("Sorry, you lost the game by",gap,"points.")
    elif gap < 0:
        print("Congratulation! You won the game by",abs(gap),"points.")
    else:
        print("The game was a draw with",userPoint,"points each.")

#guessMedal function to play guessMedal game 
def guessMedal():
    guessNum = int(input("Please enter your guess as a number between 0 and 200: "))
    randomNum = randint(50,150)         #@randomNum generates random number form 50 to 150
    numdif = abs(guessNum - randomNum)  #@numif takes absolute value of differenc in guessNum and randomNum
    if guessNum in range(0,201):        #check if guessNum is from 0 to 200 and executes if it return True
        if numdif >= 50:
            medal = 'Bronze'
        elif numdif >=20:
            medal = 'silver'
        elif numdif >=5:
            medal = 'gold'
        else:
            medal = 'platinum'
        print("You were off by", numdif,"hence you have obtained", medal,".")    
    else:
        print("Error! please enter your guess number within 0-200.")
main()                                  #invoke main funtion