# ---- String - text
# ---- Int - number (full number)
# ---- Float - number (number with decimal)
# ---- Boolean - True / False

number1 = float(input("Enter any number: "))

integer_number = int(number1)
float_number = float(number1)
round_number = int(round(float_number))

print("A 'float' is able to hold decimal places in its value...")
print(float_number)
print()
print("When you turn a 'float' into an 'int' it will always round down...")
print(integer_number)
print()
print("When you turn a 'float' into an 'int' and use the 'round' command it will round up or down...")
print(round_number)

# ---------------------------------------------------
# --- End ---