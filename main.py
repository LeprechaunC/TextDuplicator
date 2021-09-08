from tkinter import *
import pyautogui
import keyboard

root = Tk()
root.title('Sentence Duplicator')
root.configure(background='#955251')

e = Entry(root, width=60, font=('Arial', 24))
e.get()
e.grid(row=2, column=6, pady=25)

e2 = Entry(root, width=2, font=('Arial', 24,))
e2.grid(row=2, column=2, pady=25)

#e3 = Entry(root, width=2, font=('Arial',24,))
#e3.grid(row=4,column=2,pady=25)

def myClick():
    amount = e2.get()  # the amount it has to be duplicated
    print(amount)
    amount = int(amount)
    root.after(3000)

    for x in range(amount):
        amount -= 1
        root.after(1000) #Waits 1 second
        pyautogui.write(e.get())
        keyboard.press('enter')


b = Button(root, text="Duplicate", width=25, font=('Arial', 24), command=myClick)

b.grid(row=3, column=2, pady=1)

root.mainloop()
