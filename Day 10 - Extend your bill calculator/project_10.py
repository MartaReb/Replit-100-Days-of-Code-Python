bill = float(input("What is the bill?: "))
number_of_people = int(input("How many people?: "))
tip = int(input("What % of the tip would you like to leave?: "))

bill_with_tip= tip / 100 * bill + bill
final_amount = bill_with_tip / number_of_people
final_amount = round(final_amount, 2)
print("You all owe", final_amount)