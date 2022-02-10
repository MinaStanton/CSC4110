# Revision 1 2/10/2022
## Mina Stanton
### Initial Commit 

# Issue 1: Customer needs a program written in Python that is consistent with the following output
userString = input("Please enter a string: ")
print("\nYou entered " + userString + "and its type is: ", type(userString))
userInteger = int(input("\nPlease enter an integer: "))
print("\nYou entered ", userInteger, "and its type is: ", type(userInteger))

print()
print()

# Issue 2: Write a Python program to print the following string in a specific format 
songString = """Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,\n\tHow I wonder what you are"""
print(songString)

print()
print()

# Issue 3: Write a Python program which accepts the radius of a circle from the user and compute the area.
PI = 3.14159265359
userRadius = float(input("Please enter the radius: "))
areaOfCircle = PI * userRadius * userRadius
print("r = ", userRadius, "\nA = ", areaOfCircle)


# Write a Python program to test whether an inputted letter is a vowel or not.
print()
print()

vowels = ["a", "e", "i", "o", "u"]
isVowel = False
userLetter = input("Enter a letter: ").lower()
if userLetter in vowels:
    isVowel = True
print("You entered " + userLetter + ". Is it a vowel? ", isVowel)

print()
print()

# Issue 5: Use “list comprehension” to produce the specified output:   
dataList = [0,1,16,81,256,625,1296,2401,4096,6561,10000,14641,20736,28561,38416,50625,65536,83521,104976]
newList = [x for x in dataList]
print(newList)

print()
print()

# Issue 6: Create a list of Roulette wheel slots and randomly select a slot then add it to a list call Log
import random
LOG = []
rouletteSlots = ["GREEN 0", "RED 1", "RED 3", "RED 5", "RED 7", "RED 9", "RED 12", "RED 14", "RED 16", "RED 18", 
"RED 19", "RED 21", "RED 23", "RED 25", "RED 27", "RED 30", "RED 32", "RED 34", "RED 36", "BLACK 2", "BLACK 4", 
"BLACK 6", "BLACK 8", "BLACK 10", "BLACK 11", "BLACK 13", "BLACK 15", "BLACK 17", "BLACK 20", "BLACK 22", "BLACK 24", 
"BLACK 26", "BLACK 28", "BLACK 29", "BLACK 31", "BLACK 33", "BLACK 35", "GREEN 00"]

index = 0
while index <= 10:
    userRandomSelection = random.choice(rouletteSlots)
    LOG.append(userRandomSelection)
    print("\nYou randomly selelected: " + userRandomSelection)
    index+=1
print("\nHere is a list of all your selections:")
for userSelection in LOG:
    print(userSelection)


print()
print()

# Issue 7: Make a list of people you’d like to invite to dinner. Add them using the following design
dinnerGuests = []
dateGuestsWereInvited = ["1-25-2022", "1-05-2022", "1-13-2022", "2-2-2022", "2-7-2022","2-4-2022", "2-8-2022"]
index = 0
while index < 6:
    dinnerGuests.append(input("Please enter the first and last name of a guest\n"))
    index+=1
print()
newListZip = zip(dinnerGuests, dateGuestsWereInvited) # combiing the name of guest with the date invited
for guest, date in newListZip:
    print(guest, date)
print()
for guest in dinnerGuests:
    if len(guest) < 10: # if the guest name is less than 10 character then it will get a small tag
        print(guest + " goes on a small tag")
    else:
        print(guest, " goes on a big tag")

# Revision 1: 2-10-2022
## Mina Stanton
### Final Revision