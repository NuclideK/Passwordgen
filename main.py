import random


while True:
    save = input("Wanna Save Code In A Txt File (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        print("Enter Valid Choice")
choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","'","{","}","/","|",",","<",">",".","?",";",":"]


code_save = ""
for i in range(40):
    code_save += random.choice(choices)
print(code_save)
print("Done")


if save == "y":
    the_file = open("Password.txt", "a")
    the_file.write(f"{str(code_save)}\n")
    the_file.close()
input()
