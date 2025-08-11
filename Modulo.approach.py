# Ask user to input an integer
integer = int(input("Enter an integer: "))
# Find the integer modulo 2
modulo = integer % 2
# If the remainder is equal to 0 print Even
if modulo == 0:
    print("Even")
# Else print odd
else:
    print("Odd")

