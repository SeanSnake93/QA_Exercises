# Python (Verson) ------------

# Notes -> Start <-
    # ***** Part 6A *****

    # Create 2 new python files.
    # In one file, write a function that will generate a number between 1 and 6.
    # Make this a module called dice.

    # In the second file, use the dice module to simulate throwing 2 dice and
    # return the values you get from the dice.
# Notes <- End ->

# Imports -> Start <-
import random
import DoingMyNutt
# Imports <- End ->

# Global Variables -> Start <-
Nflash = int
Players = []
Entry = str
Dice = int
Movment = int
# Global Variables <- End ->

# Functions -> Start <-
# Functions <- End ->

# Body -> Start <-
print() # ---------- Spacer ----------

Nflash = int(input("Please enter number of players: "))

print() # ---------- Spacer ----------

for i in range(Nflash):
    Player = str(input("Please Enter your Name: "))
    Players.append(Player)

print() # ---------- Spacer ----------

Dice = int(input("Please enter how many Dice to play with: "))

print() # ---------- Spacer ----------

while Entry != "W":
    for i in range(Nflash):
        Move = int(0)
        Entry = str(input("What do you want to do " + Players[i] + "? (R/W)"))
        if Entry == "W":
            break
        elif Entry == "R":
            for d in range(Dice):
                Rolls = DoingMyNutt.Rolling
                print(Rolls)
                Move = Move + Rolls
            print("You Move:", Move)
        else:
            print("Error")
            continue
# Body <- End ->