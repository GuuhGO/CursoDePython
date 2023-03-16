from tkinter import *
from tkinter import ttk
window = Tk()  # Instancia um objeto de uma janela
window.minsize(1366,768)
window.state("zoomed")
window.title("Python Course GUI!")
label = Label(master=window, text="Hello World!", font=("Arial", 40, "bold"), bg="#007acc")
label.pack()
window.mainloop()
