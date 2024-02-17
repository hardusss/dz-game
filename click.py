from tkinter import *
from time import sleep

text_colors = ['green', 'red', 'blue', 'purple', 'yellow',
               'lime', 'orange', 'gold', 'silver', 'teal',
               'brown', 'pink', 'turquoise']
root = Tk()
click = 0
stop = 0
root.geometry('300x190')
root.resizable(width=False, height=False)
root['bg'] = 'white'
root.title(f'Кліки = {str(click)}')
root.attributes('-alpha', 0.7)


def clickOnBtn():
    global click, stop
    if click % 2 == 0:
        while stop != len(text_colors):
            for i in text_colors:
                label.config(text='Button', fg=i)
                root.update()
                stop+=1
                sleep(0.05)
    else:
        while stop != len(text_colors):
            for i in text_colors:
                label.config(text='Кнопка', fg=i)
                root.update()
                stop+=1
                sleep(0.05)
    click += 1
    root.title(f'Кліки = {click}')
    stop = 0
    label.config(fg='black')

label = Label(text='Кнопка', fg='black', font=(None, '15', 'bold'), bg='white')
btn_click = Button(text='Клікни', bg='black', activebackground='yellow', command=clickOnBtn, font=(None, 10, 'bold'), fg='white')
btn_click.place(x=125, y=80)
label.place(x=117, y=30)
pls = Label(text='Між кожним натисканням на кнопку'
                 '\nтрішки зачикайте',fg='black',
                 font=('Comic Sans MS', 12, 'bold'),
                 bg='white')
pls.place(y=120, x=5)
while True:
    for i in text_colors:
        btn_click.config(fg=i)
        root.update()
        sleep(0.05)

root.mainloop()