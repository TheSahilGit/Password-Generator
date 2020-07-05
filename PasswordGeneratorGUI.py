import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import string


def main(N_total):
    uc = string.ascii_uppercase
    lc = string.ascii_lowercase

    uppercase = list(uc)
    lowercase = list(lc)
    numbers = np.linspace(0, 9, 10)
    specialCh = ['@', '#', '$', '%', '&', '*', '?', '/', '<', '>', '!', '/', '+']
    passwordList = []

    for i in range(N_total):
        lup = np.random.choice(uppercase)
        ldn = np.random.choice(lowercase)
        n = np.random.choice(numbers)
        s = np.random.choice(specialCh)
        passwordList.append(str(lup))
        passwordList.append(str(ldn))
        passwordList.append(str(int(n)))
        passwordList.append(str(s))

    password = ''.join(passwordList[0:N_total])
    return str(password)


def on_change(e):
    a = e.widget.get()
    fact = main(int(a))
    return tk.Label(root, text="The password you may use is: \n \n \n" + str(
        fact) + "\n \n \n Didn't like that? Press 'Enter' "
                "again. ", font=fontStyle1).pack()


root = tk.Tk()
root.geometry("500x100")
root.title("Password Generator")
fontStyle1 = tkFont.Font(family="Times New Roman", size="14")
fontStyle2 = tkFont.Font(family="Kalpurush", size="8")
tk.Label(root, text="Enter the length of the password and press 'Enter': ", font=fontStyle1).pack()
e = tk.Entry(root, width=30)
e.pack()

e.bind("<Return>", on_change)  # <Return> is the 'Enter' in keyboard.

tk.Label(root, text="Created by The Sahil", font=fontStyle2).pack(side='bottom')
root.mainloop()
