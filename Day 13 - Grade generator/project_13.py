print("Exam Grade Calculator")
print()
test_name = input("Enter the name of the test: ")
max_score = int(input("Enter the maximum score: "))
score_received = int(input("Enter the score received: "))
print()
percentage = int((round((score_received / max_score), 2)) * 100)

print("You got", percentage, "% in", test_name, "test.")
if percentage >= 90:
  print("You got an A+. Cogratulations!")
elif percentage >= 80:
  print("You got an A. Good job!")
elif percentage >= 70:
  print("You got an B. Nice!")
elif percentage >= 60:
  print("You got an C. You can do better!")
elif percentage >= 50:
  print("You got an D. You need to study more!")
elif percentage <= 49:
  print("You got an U. You need to study more!")
else: 
  print("Try again!")