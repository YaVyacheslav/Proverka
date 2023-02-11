from tkinter import *
import time

root = Tk()

root['bg'] = '#fafafa'
root.wm_attributes('-alpha', 0.95)
root.title('Таймер')
root.geometry('300x200')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

timeField = Entry(frame, font=100)
timeField.pack()



def btn_clickoff():
    if root.overrideredirect(0):
        root.overrideredirect(1)

def btn_click():
    if root.overrideredirect(1):
        root.overrideredirect(0)
        time.sleep(1)

def get_time():
    timer = timeField.get()
    print('Через сколько времени вам напомнить?')
    hours, min, sec = timer.split()
    hours, min, sec = int(hours), int(min), int(sec)
    while hours + min + sec != 0:
        hours, min, sec = str(hours), str(min), str(sec)
        if len(hours) != 2:
            hours0 = str('0' + hours)
        else:
            hours0 = str(hours)
        if len(min) != 2:
            min0 = str('0' + min)
        else:
            min0 = str(min)
        if len(sec) != 2:
            sec0 = str('0' + sec)
        else:
            sec0 = str(sec)
        info['text'] = (hours0, ':', min0, ':', sec0)
        print(hours0, min0, sec0, sep=':')
        hours, min, sec = int(hours), int(min), int(sec)
        time.sleep(1)
        if sec != 0:
            sec -= 1
        else:
            if min != 0:
                min -= 1
                sec = 59
            else:
                if hours != 0:
                    hours -= 1
                    min = 59
                    sec = 59
    info['text'] = 'Конец!'


button1 = Button(frame, text="Начать", font=40, command=get_time)
button1.pack()
button = Button(frame, text="Закрепить", font=1, command=btn_click)
button.pack()
buttonoff = Button(frame, text="Открепить", font=1, command=btn_clickoff)
buttonoff.pack()
info = Label(frame, font=40)
info.pack()


root.mainloop()