from tkinter import *
import time

root = Tk()
root.resizable(0,0)
root.title('clock')
timeone = ''
label = Label(root,bg='blue',fg='white',font=('Tahoma',50))
label.pack(side = TOP)
def tick():
    global timeone
    timetwo = time.strftime("%H : %M : %S")
    if timeone != timetwo:
        timeone = timetwo
        label.config(text=timeone)
    label.after(200,tick)
tick()
root.mainloop()
