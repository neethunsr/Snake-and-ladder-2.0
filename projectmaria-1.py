import time
import random
import sys
import os

def instr():
        print "\n WELCOME TO SNAKE AND LADDER"
        print "-----------------------------------------------------------"
        print "Rules\n1. Any number of players can play!"
        print "2.Take it in turns to roll the dice."
        print "3 Randomly roll the dice and try giving your lucky number"
        print "4. Beware of the snakes and ladders are a boon!\n5. The first person to reach 50 wins"
        print "------------------------------------------------------------"

        n = input("How many of you are playing? ")
        return n


def snake(t):
    snake = {}
    c = 6
    for i in range(5):
        snake[t[i]] = c
        c += 1
    return snake


def ladder(t):
    ladder = {}
    c = 6
    for i in range(5,10):
        ladder[t[i]] = c
        c += 1
    return ladder


def dice():
    n = random.randint(1, 6)
    time.sleep(1)
    return n
    

def trap(t,elem,snake,ladder):
    tr = 0
    
    for i in range(10):
        if t[i] == elem:
            break

    if i < 5:
        ar = snake[elem]
        print "You are @ ", elem
        elem -= ar
        print "Oops, it's a snake, decrement by", ar
    else:
        ar = ladder[elem]
        print "You are @", elem
        elem += ar
        print "Yay! It's a ladder, increment by",ar
        
    return elem


def turn(sc,pl,t,snake,ladder):
    if sc < 50 :
#        print "Its player", pl, "s turn"
        time.sleep(2)

        p=int(input("Rolling the dice..enter your lucky number"))
        throw=dice()

        if (throw == 6):
                    print "You have a 6,throw again"
                    p=dice()
                    print"it is a", p
                    throw += p
        else :
                    print"Its a", throw

        sc += throw
        if sc in t:
            sc = trap(t, sc, snake, ladder)
        return sc


def intro(n):
    player = {}
    print "your names"
    for i in range(n):
        print i+1,
        player[i]=raw_input()

    return player


os.system('cls')
n = instr()
player = intro(n)
s = []

for i in range(n):
    s.append(0)

t=[]
while(len(t) < 10):
    r = random.randint(1,50)
    if r not in t:
        t.append(r)

snake = snake(t)
ladder = ladder(t)

print "Lets start the game"
time.sleep(1)
print "Snakes are there @", snake
print "Ladders are there @", ladder

f = "y"
k = 1

while(f.lower() == "y"):

    for i in range(n):
        s[i]=turn(s[i], i+1, t, snake, ladder)
        if (s[i] < 50):
            print player[i], "is now @", s[i]
            if(i != n - 1):
                print "Its your turn now,", player[i+1]
        else:
            print player[i], "has won,congrats!"
            time.sleep(1)
            k = 0
            break;
            
    if (k):
        f = raw_input("Its fun right..DO YOU WANT TO CONTINUE(y/n)?")
    else:
        f = raw_input("Hope you had fun playing..Do you want to play again?(y\\n)")
        if (f.lower() == "y"):
            for i in range(n):
                s.append(0)
            os.system('clear')
        else:
            print "You have exited!"
            time.sleep(1)
            sys.exit()
        
