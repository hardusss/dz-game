import _tkinter
from tkinter import *
from random import randint
from time import sleep

spr0ba = 5


def game(randNum):
    global sproba
    resNum = randNum
    root = Tk()
    root.geometry('300x220')
    root.title(f'Залишилось спроб {sproba}')
    root['bg'] = 'MediumPurple4'

    def restart():
        global sproba
        sproba = 5
        root.destroy()
        main()

    def exit():
        root.destroy()

    def valid(value):
        if len(value) <= 3:
            labelInfo.config(text='Задай діапазон числа')
            return True
        else:
            labelInfo.config(text='Максимальна довжина 3')
            return False

    def res(numRes):
        try:
            global sproba
            if entryGues.get() == str(numRes):
                labelResult.config(text='✅Ви вгадали', fg='green')
                root.update()
                sleep(2)
                for widget in root.winfo_children():
                    widget.destroy()
                root.title('Restart')
                label_info = (Label(text='Ви виграли', bg='MediumPurple4', font=('Comic Sans MS', 18, 'bold'), fg='green')
                              .pack(pady=10))
                btnRestart = (Button(text='Restart🔁', bg='MediumPurple4', font=('Comic Sans MS', 12, 'bold'), fg='white', command=restart)
                              .pack(pady=10))
                btnExit = (Button(text='Exit🔙', bg='MediumPurple4', font=('Comic Sans MS', 12, 'bold'), fg='white', command=exit)
                              .pack(pady=10))
            if len(entryGues.get()) == 0 and sproba > 0:
                labelResult.config(text='Ви нічого не ввели', fg='red')
            if sproba == 1:
                for widget in root.winfo_children():
                    widget.destroy()
                root.title('Restart')
                label_info = (Label(text='Ви програли', bg='MediumPurple4', font=('Comic Sans MS', 18, 'bold'), fg='red')
                              .pack(pady=10))
                btnRestart = (Button(text='Restart🔁', bg='MediumPurple4', font=('Comic Sans MS', 12, 'bold'), fg='white',
                                     command=restart)
                              .pack(pady=10))
                btnExit = (
                    Button(text='Exit🔙', bg='MediumPurple4', font=('Comic Sans MS', 12, 'bold'), fg='white', command=exit)
                    .pack(pady=10))
            else:
                if entryGues.get() < str(numRes):
                    labelResult.config(text='❎Число більше', fg='red')
                    sproba -= 1
                    root.title(f'Залишилось спроб {sproba}')
                else:
                    labelResult.config(text='❎Число менеше', fg='red')
                    sproba -= 1
                    root.title(f'Залишилось спроб {sproba}')
        except _tkinter.TclError:
            print('')

    labelInfo = Label(text='Вгадай число', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 14, 'bold'))
    labelInfo.pack(pady=12)
    labelResult = Label(text='Результат', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 14, 'bold'))
    labelResult.pack()
    labelGues = Label(text='Вгадайте число: ', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 11, 'bold'))
    labelGues.place(x=0, y=110)
    validation = root.register(valid)
    entryGues = Entry(fg='MediumPurple4', insertbackground='MediumPurple4', font=(None, 8, 'bold'), width=25, validate='key', validatecommand=(validation, '%P'))
    entryGues.place(x=135, y=117)
    btnResult = Button(text='Результат', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 12, 'bold'), width=12, command=lambda: res(resNum))
    btnResult.place(x=85, y=160)
    root.mainloop()


def main():
    root = Tk()
    root.geometry('260x220')
    root.title('Відгадай число')
    root['bg'] = 'MediumPurple4'

    gameNumber = ''
    diapazon = []

    def clear_window():
        global gameNumber, diapazon
        diapazon = []
        if entryNum2.get() != '' or entryNum1 != '':
            diapazon.append(entryNum1.get())
            diapazon.append(entryNum2.get())
            randNum = randint(int(diapazon[0]), int(diapazon[1]))
            gameNumber = str(randNum)
            root.destroy()
            diapazon = []
            game(randNum)

    def valid(value):
        if len(value) <= 3:
            labelInfo.config(text='Задай діапазон числа')
            return True
        else:
            labelInfo.config(text='Максимальна довжина 3')
            return False

    labelInfo = Label(text='Задай діапазон числа', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 14, 'bold'))
    labelInfo.pack(pady=12)

    labelRangeNum1 = Label(text='Старт діапазону: ', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 10, 'bold'))
    labelRangeNum1.place(x=-1, y=80)

    validation = root.register(valid)
    entryNum1 = Entry(fg='MediumPurple4', insertbackground='MediumPurple4', font=(None, 8, 'bold'), validate='key', validatecommand=(validation, '%P'))
    entryNum1.place(x=120, y=85)

    labelRangeNum2 = Label(text='Кінець діапазону: ', fg='white', bg='MediumPurple4', font=('Comic Sans MS', 9, 'bold'))
    labelRangeNum2.place(x=0, y=120)

    entryNum2 = Entry(fg='MediumPurple4', insertbackground='MediumPurple4', font=(None, 8, 'bold'), validate='key', validatecommand=(validation, '%P'))
    entryNum2.place(x=120, y=124)

    btnStart = (Button(text='Старт', bg='DarkOrchid4', fg='white', font=('Comic Sans MS', 12, 'bold'), width=12, command=clear_window)
                .place(y=165, x=65))
    root.mainloop()


main()