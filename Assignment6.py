# Revision 1 2/22/22
## Mina Stanton
### Initial Commit



# Work Item 1
print(""" "insert quote here" """)
print("James O'leary")
print("""Here is a string
    that spans multiple lines
        and will have whitespace in it! """)
singleLineString = ("Here is "
                    "a string written on "
                    "on multiple lines but will "
                    "only print on one line")
print(singleLineString)
print()
print()

# Work Item 2
string1 = "This is the song that never ends...oh wait it ended!"
print(len(string1))
stringX = "A string that will"
stringY = "be concatenating them together"
stringZ = stringX + stringY
print(stringZ)
stringA = "Part one of string"
stringB = "connecting to part two of string"
stringC = stringA + " " + stringB
print(stringC)
stringZing = "bazinga"
print(stringZing[2:6])

print()
print()

# Work Item 3
stringsToConvert = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
for x in stringsToConvert:
    print(x.lower())
print()

for x in stringsToConvert:
    print(x.upper())
print()

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.strip())
print(string2.strip())
print(string3.strip())
print()

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))
print()
print()

# Work Item 4
stringInt = "42"
intA = int(stringInt)
intB = intA * 2
print(intB)

stringFloat = "42.5"
floatA = float(stringFloat)
floatB = floatA * 3.4
print(floatB)
print()

stringObj = "Forty Two"
intObj = 42
print(stringObj + " " + str(intObj))

userInput1 = int(input("Please enter the first number you would like to multiply: "))
userInput2 = int(input("Please enter the second number you would like to multiply: "))
productOfInput = userInput1 * userInput2
print("The product of", userInput1, "and", userInput2, "is", "%.1f" % productOfInput)

stringToFind = "Hello World! It's nice to meet you!"
stringFound = stringToFind.find("!")
print(stringFound)

# Revision 1: 2-22-2022
## Mina Stanton
### Final Revision