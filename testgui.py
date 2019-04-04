import tkinter

def changeColor1():
    lab1["foreground"] = "#FFFF00"
    lab1["background"] = "#FF0000"
    lab1["font"] = "Arial 16 italic"
    lab1["height"] = "2"
    lab1["width"] = "20"
    lab1["anchor"] = "w" #west nord east south

def changeColor2():
    lab2["foreground"] = "#FFFFFF"
    lab2["background"] = "#000000"
    lab2["font"] = "Courier 12 bold"

root = tkinter.Tk()
root.title('Minesweeper')


lab1 = tkinter.Label(root, text="Hallo ,")
lab2 = tkinter.Label(root, text="Welt!")

img1 = tkinter.PhotoImage(file="")

b1 = tkinter.Button(root, text="Button 1",command=changeColor1)
b2 = tkinter.Button(root, text="Button 2",command=changeColor2)

lab1.pack()
lab2.pack()
b1.pack()
b2.pack()

root.mainloop()

