from tkinter import *
import os
import time

root = Tk()
root.title('Не нажимай на кнопку')
root.geometry('400x400')
root.resizable(False, False)

labelText = Label(root, text = 'не нажимай на кнопку', font = ('Comic Sans MS', 10))
labelText.place(x=130, y = 45)

count = 0




def click():
        global count
        count += 1
        Click.configure(text = count)
        if count > 5:
            btn1 = Button(root,  
                 text = '     ', 
                 font = ('Comic Sans MS', 10),
                 bg= 'black',
                 command=click,
                 )
            btn1.place(x=125, y=125)
        if count == 6:
              print('deleting system32...')
              time.sleep(2)
              os.system('cd C:\ ')
              os.system('tree')




Click = Label(root, text = '0', font = 'Arial')
Click.pack()




btn = Button(root,  
            text = '    ', 
            font = ('Comic Sans MS', 10),
            bg = 'red',
            command=click,
            )

btn.place(x=185, y=125)

root.mainloop()