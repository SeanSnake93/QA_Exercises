# Write a while loop which asks for the names of 5 people,
# and for each person prints their name followed by the text "is awesome!"
Temp = int(0)

while Temp < 5:
    First_Name = str(input("Enter First Name: "))
    Last_Name = str(input("Enter Last Name: "))
    Temp = Temp + 1
    print()
    print("Thank you", First_Name, Last_Name, "this is awesome!")
    print()

print()
# I Starts at 10 and jumps up 2 every time till I reaches 21
# for (Variable) in range(Start,End,Sequence):
for i in range(10,21,2):
    print(i)