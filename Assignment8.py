# Revision 1 3/7/2022
## Mina Stanton 3/7/2022
### Initial Commit Issue 1

from tkinter import *
import os 

# Create display window
window = Tk()
window.geometry('300x400')
window.title('Mad Gen')
Label(window, text='Mad Libs Story Teller', font='Helvectica 20 bold').pack()
Label(window, text='Click Any One :', font='ariel 15 bold').place(x=40, y=80)

#Madlib one

def madlib():
    person = input('enter a person name: ')
    color = input('enter a color: ')
    foods = input('enter a food name: ')
    adjective = input('enter an adjective name: ')
    thing = input('enter a thing name: ')
    place = input('enter a place: ')
    verb = input('enter a verb: ')
    adverb = input('enter an adverb: ')
    food = input('enter food name: ')
    things = input('enter thing name: ')
    print('Last night I dreamed I was a ' + adjective + ' unicorn with ' + color + ' with spots that looked like ' + thing + "! I flew into space with " + person + " who is a " + verb + " that was always eating " + food + " we went to " + place + " and had second breakfast which was " + foods + " that tasted like " + adverb + " " + things)

def quit_program():
    os._exit(0)

# add and place buttons
Button(window, text='Mad Lib Go', font='ariel 15', command=madlib, bg= 'ghost white').place(x=70, y=180)
Button(window, text='QUIT', font=('Helvetica 13 bold'), foreground='Green', background='Yellow', command=quit_program).place(x=80, y=280)


window.mainloop()

# end of commit 1