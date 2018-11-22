import time
import random
import sys
import os

def instr():
    print "\n WELCOME TO SNAKE AND LADDER"
    print "-----------------------------------------------------------"
    print "Rules\n1. Any number of players can play!"
    print "2. Take it in turns to roll the dice."
    print "3. Randomly roll the dice and try giving your lucky number"
    print "4. Beware of the snakes and ladders are a boon!\n5. The first person to reach 50 wins"
    print "------------------------------------------------------------"

    numberOfPlayers = input("How many of you are playing? ")
    return numberOfPlayers


def snake(t):
    snake = {}
    for i in range(5):
        snake[t[i]] = random.randint(1, min(10, t[i]))
    return snake


def ladder(t):
    ladder = {}
    for i in range(5,10):
        ladder[t[i]] = random.randint(1, min(10, 50 - t[i]))
    return ladder


def dice():
    time.sleep(1)
    return random.randint(1, 6)
    

def trap(t, position, snake, ladder):
    tr = 0
    
    for i in range(10):
        if t[i] == elem:
            break

    if i < 5:
        ar = snake[position]
        print "You are @ ", position
        position -= ar
        print "Oops, it's a snake, decrement by", ar
        print "You are currently @", position
    else:
        ar = ladder[position]
        print "You are @", position
        position += ar
        print "Yay! It's a ladder, increment by",ar
        print "You are currently @", position

    return position


def turn(sc, pl, t, snake, ladder):
    if sc < 50 :
        time.sleep(2)

        p = int(input("Rolling the dice.. Enter your lucky number "))
        throw = dice()

        if (throw == 6):
            print "You have a 6,throw again"
            p = dice()
            print "It's a", p
            throw += p
        else :
            print "It's a", throw

        sc += throw
        if sc in t:
            sc = trap(t, sc, snake, ladder)
        return sc


def intro(n):
    player = {}
    print "Your names:"
    for i in range(n):
        print i+1,
        player[i] = raw_input().title()

    return player


os.system('cls')

numberOfPlayers = instr()
player = intro(numberOfPlayers)
positions = []

for i in range(numberOfPlayers):
    positions.append(0)

randomList = []
while(len(randomList) < 10):
    r = random.randint(1, 50)
    if r not in randomList:
        randomList.append(r)

snake = snake(randomList)
ladder = ladder(randomList)

print "Lets start the game"

time.sleep(1)

print "Snakes are there @", snake
print "Ladders are there @", ladder

f = "y"
k = 1

while(f.lower() == "y"):

    for i in range(numberOfPlayers):
        positions[i] = turn(positions[i], i+1, randomList, snake, ladder)
        if (positions[i] < 50):
            print player[i], "is now @", positions[i]
            if(i != numberOfPlayers - 1):
                print "Its your turn now,", player[i+1]
        else:
            print player[i], "has won, congrats!"
            time.sleep(1)
            k = 0
            break;
            
    if (k):
        f = raw_input("Its fun, right? DO YOU WANT TO CONTINUE(y\\n)? ")
    else:
        f = raw_input("Hope you had fun playing.. Do you want to play again?(y\\n)")
        if (f.lower() == "y"):
            for i in range(numberOfPlayers):
                positions.append(0)
            os.system('clear')
        else:
            print "You have exited!"
            time.sleep(1)
            sys.exit()
