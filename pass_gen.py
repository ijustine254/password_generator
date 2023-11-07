import random as ran

limit = None
password = ""

length = input("Password Length:")
aas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spe = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", ",", "<", ">", ".", "?", "|"]


count = 0
try:
    length = int(length)
    while count < length:
        ran1 = ran.choice([1,2,3])
        if ran1 == 1:
            ran2 = aas
        elif ran1 == 2:
            ran2 = num
        else:
            ran2 = spe
        password += ran.choice(ran2)
        count += 1
except:
    print("Not a Number")
    

print(password)
