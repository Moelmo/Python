from tkinter import *

main = Tk()
ourMessage = "This is our message"
messageVar = Message(main, text=ourMessage)
messageVar.config(bg="aqua")
messageVar.pack()
main.mainloop()