print("Secure Login")
print("--"*6)
name = input("What's your name? ")
password = input("What's your password? ")

if name == "Marta" and password == "admin1":
  print("Hello Marta!")
elif name == "Janne" and password == "admin2":
  print("Welcome Janne!")
elif name == "John" and password == "admin3":
  print("Hi John!")
else:
  print("You don't have an account here...sorry!")