# Revision 1 2/2/2022
## Mina Stanton 2/2/2022
### Initial Commit Issue 1

# Issue 1: the user will input a number  and the same number will print back after some math
userNumber = float(input("Please enter a number: "))
newNumber = (((userNumber + 2) * 3) - 6) / 3
print(newNumber)

# Revision 1 2/2/2022
## Mina Stanton


# Revision 2 2/3/2022
## Mina Stanton 2/3/2022

print()
print()
#Issue 2: the client wants to know what the output is of each group
# the output will print along with which group it is
#Group one:
print("Group one: ")
my_var1 = 7.0
my_var2 = 5
print(my_var1 % my_var2)

print("Group two: ")
#Group two:
x = 4
y = 5
print(x//y)

print("Group 3: ")
#Group three:
print(30-3**2+8//3**2*10)


# Issue 3: client would like to know the output 
userInput = input("Please enter something: ")
# printing input as a string
print("Your input as a string: " + str(userInput))
# printing input as an int
print("Your input as an integer: ", int(userInput))
# printing input as a float
print("Your input as a string: ", float(userInput))


# Issue 4: client would like to know the difference
print("A: ", 2**2**3) #prints 256
print("B: ", 2**(2**3))#prints 256
print("C: ", (2**2)**3) #prints 64


# Issue 5: create a game of chance
import random

# ask user how many items to add to the chest
print("Welcome to Pirates Treasure! How many items can you collect before the money runs out?!\n")
numberOfChestItems = int(input("How many items would you like inside the treasure chest? "))
treasures = ["Gold", "Silver", "Copper"]
treasureChest = []
while numberOfChestItems > 0:
    treasureChest.append(random.choice(treasures))
    numberOfChestItems-= 1
print("The treasure chest is filled with: \n", treasureChest)
bank = 50.00
while bank > 0:
    wager = random.randint(1,50) # randomly selects wager value
    while wager > bank:
        wager = random.randint(1,50) # randomly selects wager again if wager si greater than bank
    print("Your wager is: ", wager)
    bank -= wager
    print("You have $%.2f" %bank + " left in the bank for your next wager and spin!")
print("You have nothing left in the bank! Thanks for playing!")

# Revision 2: 2/3/2022
# Mina Stanton

# Revision 3: 2/4/2022
# Mina Stanton

# Issue 6: password simulator
import  random

acceptablePasswords = []
dictionaryList = []
# open file with list of passwords alredy in use
with open('rockYouPartialList.txt', 'r') as f:
    dictionaryList = f.readlines()

specialSymbols = ["!", "@", "#" , "$", "%", "^", "&", "*", ".", "?"]
characterList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&&*.?"
count = 1
while count < 45:
    randomCharacters = [random.choice(characterList) for i in range(3,9)] # get up to 9 random characters
    randomPassword = "".join(randomCharacters) # creates a string out of the cahracters
    print(str(count) + ": Random Password Generated: " + randomPassword)

    if any(char in randomPassword for char in specialSymbols): #if the random password contains a special symbol
        if not any(randomPassword for randomPassword in dictionaryList): #check if the password is already in the dictionay
             print(randomPassword + " is unaccepted")
        else: # if not in dictionary but has a special character then password is accepted
            print(randomPassword + " is accepted and will be archived")
            acceptablePasswords.append(randomPassword)
    else:
        print(randomPassword + " is unaccepted")
    count+=1
    print()

# Revision 3 2/4/2022
# Mina Stanton

