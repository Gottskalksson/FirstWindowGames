from tkinter import *
import random

t = Tk()
t.title("Choose the button")
t.geometry("300x350")


def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "You won!")
    etykieta.pack(fill=BOTH, expand=YES)
    t.after(3000, restart)

def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Not even close!")
    etykieta.pack(fill=BOTH, expand=YES)
    t.after(3000, restart)

def wstaw_przyciski():
    ile_przyciskow = 4
    global przyciski
    przyciski = []
    dobry = random.randint(0,ile_przyciskow-1)
    for i in range (ile_przyciskow):
        if i ==  dobry:
            przyciski.append(Button(t, text = "Click!", command=trafiony))
        else:
            przyciski.append(Button(t, text = "Click!", command=pudlo))
            
    for i in przyciski:
        i.pack(fill=BOTH, expand=YES)

def restart():
    etykieta.destroy()
    wstaw_przyciski()


wstaw_przyciski()




