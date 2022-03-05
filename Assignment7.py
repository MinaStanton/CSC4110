# Revision 1 3/4/2022
## Mina Stanton 3/4/2022
### Initial Commit Issue 1


# Work Item 1
names = ["joe", "tom", "barb", "sue", "sally"]

scores = [10, 23, 13, 18, 12]



def makeDictionary(names,scores):

    return dict(zip(names, scores))

 
scoreDict = makeDictionary(names, scores)

print(str(scoreDict))    

print()
print()

 
# Work Item 2
stillSearching = True
while stillSearching:

    searchName = input("Please enter a name to search: ")

    if searchName == "barb":

        stillSearching = False

searchScore = scoreDict[searchName]

print("The score for " + searchName + " is ", searchScore)

print()
print()



# Work Item 3
scoreDict2 = {}
def addNameAndScoresPerpetually():
    index = 0
    while True:
        scoreDict2[input("Enter a Name: ")] = int(input("Enter a Score: "))
        index+=1
        print(str(scoreDict2))

addNameAndScoresPerpetually()


print()
print()

# Work Item 4
sortedScoresList = sorted(scoreDict.values())

for x in sortedScoresList:

    print(x)

 
print()
print()


# Work Item 5
def studentUpdated():
    stillUpdating = True
    while stillUpdating:
        validate = True
        while validate:
            option = int(input("\nPlease enter 1 to Add, 2 to Delete 3 to Query, 4 to Print all students: "))
            if option in range(1,5):
                validate = False
    
        if option == 1:

            scoreDict.update({input("Enter the Name: "): int(input("Enter the Score: "))})

        elif option == 2:
            validate = True
            while validate:
                nameToDelete = input("Enter the name of the student you would like to delete: ")
                if nameToDelete in scoreDict:
                    validate = False

            del scoreDict[nameToDelete]

        elif option == 3:
            validate = True
            while validate:
                nameToQuery = input("Enter the name of the student you would like to query: ")
                if nameToQuery in scoreDict:
                    validate = False
            print("The score for ", nameToQuery, " is ", scoreDict[nameToQuery])
        elif option == 4: 
            print(scoreDict.items())

        userInput = input("\nWould you like to exit? (y/n):")
        if userInput.lower() == "y":
            stillUpdating = False

studentUpdated()