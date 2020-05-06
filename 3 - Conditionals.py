# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "distinction"
# If the mark is between 65 and 85 "pass"
# Anything else print "Fail"
# Try to do it both with and without elif statements.

Paper_Marks = int(100)
Result = int(0)
Percent = int
Grade = str
Message = str

print()
print("Please enter your results from the test, Score should be no bigger than '" + str(Paper_Marks) + "'.")
print()

while Result > 100 or Result < 1:
    Result = int(input("Results: "))
    if Result > 100 or Result < 1:
        print("Please enter a valid Number.")
        print()
print()

Percent = Result / Paper_Marks * 100

if Percent > 85:
    Grade = "Distinction"
    Message = "Smashed it!"
elif Percent >= 65:
    Grade = "Pass"
    Message = "You did it!"
else:
    Grade = "Fail"
    Message = "Try again!"

print("*" * 30)
print()

print("My Score:", Result)
print("Posible Marks:", Paper_Marks)
print("Percent:", str(Percent) + "%")
print("Grade:", Grade)
print("Message:", Message)