"""Code generates random password of a given length consisting upper and lower case letters, numbers and special characters."""
### Sahil Islam ###
### 01/07/2020 ###


import numpy as np
import string

N_total = int(input("How long password do you want? "))


def main():
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
    print("The password you may use is : " + str(password))


def loop():
    main()
    a = str(input("\nDidn't like that? \nWant a new one? (y/n): "))
    if a == "y":
        loop()
    else:
        print("Thank You")


loop()
