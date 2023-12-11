import tkinter
from tkinter import *

'''
def get_entry():
    heading = name.get()
    if heading:
        print(heading)
    else:
        print('Empty entry')
'''
'''
fg='#bfbfbf'
bg='#01018a'
'''

def get_entry():
    heading = int(name.get())
    if heading:
        if heading in range(1, 179):
            reversed_heading = heading + 200 - 20

        elif heading == 180:
            reversed_heading = 360

        elif heading == 0 or 360:
            reversed_heading = 180

        if heading in range(181, 359):
            reversed_heading = heading - 200 + 20

        #print(reversed_heading)
        label1 = Label(window, text=reversed_heading, font='AirbusDisp2 20', bg='black', fg='#48bcff', anchor='c')
        label1.place(x=175, y=80)
        #label1.pack()
    else:
        #print('Empty entry')
        label2 = Label(window, text='', bg='#01018a')
        label2.pack()


def clear_result():
    label3 = Label(window, text='', bg='black', width=10, height=20, justify='left')
    label3.place(x=170, y=75)


window = tkinter.Tk()
window.title('Reversed Heading')
window.geometry("400x300")
window.resizable(False, False)
window.minsize(350, 200)
window.maxsize(600, 600)
#window.config(bg='#01018a')
window.config(bg='black')

'''
buttn_border = tkinter.Frame(window, highlightbackground='green',
                    highlightthickness=1,
                    bd=0)
button1 = Button(window, text='calculate',
        font='AirbusDisp2',
        command=get_entry,
        fg='white',
        bg='black')
button1.pack()
buttn_border.pack()
'''

name = Entry(window, fg='white', bg='black', font='AirbusDisp2')
name.pack()

button1 = Button(window, text='calculate',
        font='AirbusDisp2',
        command=get_entry,
        fg='white',
        bg='black')
button1.pack()

button2 = Button(window, text='clear',
        font='AirbusDisp2',
        command=clear_result,
        fg='white',
        bg='black')
button2.pack()


window.mainloop()

'''
heading = int(input('Enter heading'))


if heading in range(1, 179):
    reversed_heading = heading + 200 - 20

elif heading == 180:
    reversed_heading = 360

elif heading == 0 or 360:
    reversed_heading = 180

if heading in range(181, 359):
    reversed_heading = heading - 200 + 20

print(reversed_heading)

'''
