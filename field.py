import tkinter as tk

#LeftClick to discover field
def leftClick(event):
    print("leftClick")
    return

#RighClick to set flag
def rightClick(event):
    b["image"] =  bomb

root = tk.Tk()

#import images
bomb = tk.PhotoImage(file="/Users/thomas/Documents/Programmierung/GitHub/minesweeper/images/flag.png")

b = tk.Button(root, image = bomb)
b.bind("<Button-1>", leftClick)
b.bind("<Button-2>", rightClick)
b.pack()

root.mainloop()
