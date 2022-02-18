# Revision 1 2/17/2022
## Mina Stanton
### Initial Commit

# Work ticket 1
# 1-4


import datetime

firstName = input("Please enter your first name: ").lower()
lastName = input("Please enter your last name: ").upper()
print("Hello, " + firstName.upper() +" " + lastName.lower()) 
print()
print()

# 5
firstAndLastName = firstName + " " + lastName

# 6
print(firstAndLastName.split(" ")[1])

# 7
firstAndLastName = firstAndLastName.replace(lastName, lastName + ", Walsh College Student")
print(firstAndLastName)

#8
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# 9
number1 = float(input("Please enter a decimal number: "))
number2 = float(input("Please enter another decimal number: "))

#10
numberAddition = number1 + number2
numberSubtraction = number1 - number2
numberMultiplication = number1 * number2
numberDivison = number1 / number2

# 11
print(number1, " plus ", number2, " equals ", numberAddition)
print(str(number1) + " minus " + str(number2) + " equals " + str(numberSubtraction))
print("{} multiply {} equals {}".format(number1, number2, numberMultiplication))
stringDivision = str(number1), " divided by ", str(number2), " equals ", numberDivison
printDivision = f'{stringDivision}'
print(printDivision)

# 12
sq_root = numberMultiplication**(1/2)
print("The square root of " + str(numberMultiplication) + " equals " + str(sq_root))

#13
currentMonth = datetime.datetime.now().strftime("%B")
dayOfMonth = datetime.datetime.today().day

# 14
print("Today is day", currentMonth, "\n\t\t", dayOfMonth)

# Revision 1: 2-17-2022
## Mina Stanton
### Final Revision