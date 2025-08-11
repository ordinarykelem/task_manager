# Ask user to input their score as a number
score = int(input("Enter your score: "))
# If score is between 90 to 100 (inclusive) print grade A
if score >= 90 and score <= 100:
    print("Grade A")
# If Score is between 80 to 89 (inclusive) print grade B
elif score >= 80 and score <= 89:
    print("Grade B")
# If score is between 70 to 79 (inclusive) print grade C
elif score >= 70 and score <= 79:
    print("Grade C")
# If score is between 60 to 69 (inclusive) print grade D
elif score >= 60 and score <= 69:
    print("Grade D")
# If score is betweeen 0 to 59 (inclusive) print grade F
elif score >= 0 and score <= 59:
    print("Grade F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")
