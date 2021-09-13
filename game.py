from tkinter import *
import random


root=Tk()

root.geometry("600x680")

root["bg"]=("grey")

can=Canvas(root, width=500, height=500, bg="grey")
can.place(x=50, y=45)

x, y =10, 10
oval_x, oval_y = 0, 0
ready=False
print_status=True
points = 0

def clean_oval():
    can.create_oval(oval_x,oval_y,oval_x+30,oval_y+30, fill="red", outline="blue", width=4)


def try_create_oval():
    if oval_x != 0 and oval_y != 0:
        can.create_oval(oval_x,oval_y,oval_x+30,oval_y+30, fill="blue", outline="red", width=4)
        

def point_info():
    global points
    points += 1
    myLabel_intro = Label(root, text = f"(User: name )\n Points = {points}")
    myLabel_intro.place(x=250, y=0)


def clean_up_down():
    global x, y, print_status

    if oval_x+5 >= x and oval_x-5 <= x and oval_y-20 <= y and oval_y+30 >= y:
        clean_oval()
        print_status = True
        paint()
        point_info()

def clean_left_right():
    global x, y, print_status

    if oval_x+30 >= x and oval_x-20 <= x and oval_y-5 <= y and oval_y+5 >= y:
        clean_oval()
        print_status = True
        paint()
        point_info()


def paint():
    global oval_x, oval_y, x, y, ready, print_status

    while print_status:
        xr=random.randint(10,490)
        yr=random.randint(10,490) 
        can.create_oval(xr,yr,xr+30,yr+30, fill="blue", outline="red", width=4)
        ready = True
        print_status = False
        oval_y = yr
        oval_x = xr


def right():
    global x, y, print_status
    x=x+10
    can.create_rectangle(-5,-5, 505, 505, fill="#F0FFF0")
    can.create_rectangle(x, y, x+30, y+30, outline="#FF4500", width=5)
    try_create_oval()
    clean_left_right()


def left():
    global x, y, print_status
    x=x-10
    can.create_rectangle(-5,-5, 505, 505, fill="#F0FFF0")
    can.create_rectangle(x, y, x+30, y+30, outline="#FF4500", width=5)
    try_create_oval()
    clean_left_right()


def up():
    global x, y, print_status
    y=y-10
    can.create_rectangle(-5,-5, 505, 505, fill="#F0FFF0")
    can.create_rectangle(x, y, x+30, y+30, outline="#FF4500", width=5)
    try_create_oval()
    clean_up_down()


def down():
    global x, y, print_status
    y=y+10
    can.create_rectangle(-5,-5, 505, 505, fill="#F0FFF0")
    can.create_rectangle(x, y, x+30, y+30, outline="#FF4500",width=5)
    try_create_oval()
    clean_up_down()


def go():
    """"""
    paint()
    if ready == True:
        bs.place(x=-100,y=-100)
        can.create_rectangle(-5,-5, 505, 505, fill="#F0FFF0")
        can.create_rectangle(x, y, x+30, y+30, outline="#FF4500", width=5)

        bu=Button(root, text = "↑", width=3, height=2,bg="#FA8072", command=up)
        bd=Button(root, text = "↓", width=3, height=2,bg="#FA8072", command=down)

        b1=Button(root, text = "←", width=3, height=2,bg="#FA8072", command=left)
        br=Button(root, text = "→", width=3, height=2,bg="#FA8072", command=right)

        b1.place(x=220, y=570)
        br.place(x=300, y=570)

        bu.place(x=260, y=520)
        bd.place(x=260, y=620)
        if oval_x != 0 and oval_y != 0: 
            can.create_oval(oval_x,oval_y,oval_x+30,oval_y+30, fill="blue", outline="red", width=4)

bs= Button(root, text="start", width=8, height=4, bg="green", command=go)
bs.place(x=250, y=250)



root.mainloop()