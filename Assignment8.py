# Revision 1 3/7/2022
## Mina Stanton 3/7/2022
### Initial Commit Issue 1

import tkinter as tk 
import os 
import turtle
import random

t = turtle.Turtle()

# Create display window
window = tk.Tk()
window.geometry('300x400')
window.title('Words, Shapes and more!')

def madlib():
    person = input('\n\nEnter a person name: ')
    color = input('Enter a color: ')
    foods = input('Enter a food name: ')
    adjective = input('Enter an adjective name: ')
    thing = input('Enter a thing name: ')
    place = input('Enter a place: ')
    verb = input('Enter a verb: ')
    adverb = input('Enter an adverb: ')
    food = input('Enter food name: ')
    things = input('Enter thing name: ')
    print("\n\nLast night I dreamed I was a " + adjective + " unicorn with " + color + " spots that looked like " + thing + "! I flew into space with " + person + " who is a " + verb + " that was always eating " + food + " we went to " + place + " and had second breakfast which was " + foods + " that tasted like " + adverb + " " + things)

# random polygon
def RandomPolygon():
    sides =  random.randrange(3,10)
    sideLength =  random.randrange(20, 45)
    colors = ["Green", "Red", "Blue", "Yellow", "Black"]
    polyColor = random.choice(colors)
    angle = 360/(sides)

    t.begin_fill()
    t.color(polyColor)
    for x in range(sides):
        t.forward(sideLength)
        t.right(angle)
    t.end_fill()

 
# user input polygon
def UserPolygon():
    sides =  int(input("\nEnter the number of sides for the polygon: "))
    sideLength =  int(input("Enter the side lengths: "))
    polyColor = input("Enter the color you would like: ")
    angle = 360/(sides)

    t.forward(100)
    t.begin_fill()
    t.color(polyColor)
    for x in range(sides):
        t.forward(sideLength)
        t.right(angle)
    t.end_fill()

# quit function to exit 
def Quit_program():
    os._exit(0)

# add and place buttons
madLib = tk.Button(window, text='Mad Lib Go', font='ariel 15', command=madlib, bg= 'ghost white')
randomPolygon = tk.Button(text="Create Random Polygon", font=("Helvetica 13 bold"), foreground="blue", background="ghost white", command=RandomPolygon)
userPolygon = tk.Button(text="Create Your Own Polygon", font=("Helvetica 13 bold"), foreground="green", background="ghost white", command=UserPolygon)
quitProgram = tk.Button(window, text='QUIT', font=('Helvetica 13 bold'), foreground='Green', background='Yellow', command=Quit_program)

madLib.pack()
randomPolygon.pack()
userPolygon.pack()
quitProgram.pack()

window.mainloop()

# end of commit 1

