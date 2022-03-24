# Revision 1 3/7/2022
## Mina Stanton 3/24/2022
### Initial Commit Issue 1
# 1

import math

def sphere_volume(r):
    v = (4/3) * math.pi * (r*r*r)
    return v

 
# create a main program

if __name__=="__main__":

    volume = sphere_volume(5)

    print("\nThe volume of the sphere with a radius of 5 is %.2f" %volume)
print()
print()
 

# 2
def print_range(start, end):
    if start == end:
        print(start)
    elif start < end:
        print(start)
        print_range(start + 1, end)
    else:
        print(start)
        print_range(start -1, end )


print_range(10, 5)
print()
print()
 
# 3
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

 
print("\nThe GCD of 12 and 8 is:", gcd(12,8))
print("The GCD of 20 and 24 is:", gcd(20,24))
print()
print()
 
# 4

import csv
import json

sales_data = []
filename = "SalesJan2009.csv"

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        key = row[0]
        valuesList = [row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
        dictRow = {}
        dictRow[key] = valuesList
        sales_data.append(dictRow)

 
print(sales_data)
# converting the list data to json daa
jsonData = json.dumps(sales_data)

print()
print()

print(jsonData)

 # writing the json data to a json file
with open('transaction_data.json', 'w') as jsonfile:

    json.dump(jsonData, jsonfile)

# end of commit