score1 = float(input("Enter the first test score: "))
score2 = float(input("Enter the second test score: "))
score3 = float(input("Enter the third test score: "))

average = (score1 + score2 + score3) / 3

print("\nYour average test score is:", average)

if average > 95:
    print("Congratulations!")