# Python (Verson) ------------

# Notes -> Start <-
    # Create a Python file which does the following:
    # Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
    # Reads and displays the names of the 1st and 4th team in the file.
    # Create a new Python file which does the following:
    # Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
    # Print out the edited file line by line.
# Notes <- End ->

# Global Variables -> Start <-
Nav = str
Names = []
Teams = []
outfile = str
# Global Variables <- End ->

# Functions -> Start <-
# Functions <- End ->

# Body -> Start <-

file = open("teams.txt", "r")

Name_print = file.readline()
Names.append(Name_print)
Team_print = file.readline()
Teams.append(Team_print)

file.close()

while Nav != "C":
    Nav = str.upper(input("What to do? "))
    if Nav == "N":
        Name = str(input("Enter Name: "))
        Club = str(input("Enter Club: "))
        Names.append(Name)
        Teams.append(Club)
        
        file = open("teams.txt", "w")
        print(Names)
        Name_print = str(Names)
        print(Teams)
        Team_print = str(Teams)
        file.write(Name_print + "\n" + Team_print)
        file.close()
        print()
    elif Nav == "P":
        print("Names: " + str(Names))
        print("Teams: " + str(Teams))
    elif Nav == "C":
        print("Close.....................")
        break
    else:
        print("please enter 'N' for New, 'C' for close")






#for line in range(10):
#    if line % 2 == 0:
#        outfile += file.readline()
#    else:
#        file.readline()

#file = open("filename.txt", "w")
#file.write(outfile)
#file.close()
# Body <- End ->