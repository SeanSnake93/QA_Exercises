# Python 3.8

# Notes -> Start <-
    # Create a new python file.
    # In that file create a program that works out a grade based on marks with the use of functions.

    # The program should give the students name and an ICT grade based on...
        # Homework(/25),
        # Assessment(/50),
        # Final Exam(/100).
# Notes <- End->

# Global Variables -> Start <-
Name = str
Mark = int
Res = int
Tests = ["Homework", "Assessment", "Final Exam"]
Results = [0, 0, 0]
Max_Marks = [25, 50, 100]
Percent = [0, 0, 0]
# Global Variables <- End ->

# Functions -> Start <-
def fracCalc(number1, number2):
    answer = number1 / number2 * 100
    return answer
# Functions <- End ->

# Body -> Start <-
print() # ---------- Spacer ----------

Name = str(input("Enter Name: "))

for i in range(3):
    print(Tests[i])
    Mark = Max_Marks[i]
    print("Max Mark:", Mark)
    Res = int(input("Enter your Mark: "))
    Results[i] = Res
    Percent[i] = fracCalc(Res,Mark)

print() # ---------- Spacer ----------
print("*" * 50)
print() # ---------- Spacer ----------
print(Name)
print() # ---------- Spacer ----------
for i in range(3):
    print(Tests[i] + "(" + str(Results[i]) + "/" + str(Max_Marks[i]) + ")" + str(Percent[i]) + "%")

print()
# Body <- End->