from tkinter import *

root = Tk()
click = 1
root.geometry('200x200')
root.resizable(width=False, height=False)
root['bg'] = 'black'
root.title(str(click))


def clickOnBtn():
    global click
    if click % 2 == 0:
        click += 1
        btn_click.config(text='Клікни', bg='blue', activebackground='yellow', font=(None, 10, 'bold'), fg='white')
        root.update()
    else:
        btn_click.config(text='Ти клікнув', bg='red', activebackground='lime', font=(None, 10, 'bold'), fg='white')
        click += 1
        root.update()
    root.title(str(click))
    root.update()


btn_click = Button(text='Клікни', bg='blue', activebackground='yellow', command=clickOnBtn, font=(None, 10, 'bold'), fg='white')
btn_click.place(x=75, y=80)

root.mainloop()