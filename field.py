import tkinter as tk

class field():
    def __init__(self):

        #LeftClick to discover field
        def leftClick(event):
            print("leftClick")
            return

        #RighClick to set flag
        def rightClick(event):
            b["image"] =  flag

        root = tk.Tk()

        #import images
        flag = tk.PhotoImage(file="FlagScale.png")
        #bomb = tk.PhotoImage(file="Bomb.png")

        b = tk.Button(root, image = flag, height = 5, width = 5)
        b.bind("<Button-1>", leftClick)
        b.bind("<Button-2>", rightClick)
        b.pack()

        root.mainloop()
