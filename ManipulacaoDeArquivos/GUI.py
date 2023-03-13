from tkinter import *
windows = Tk()  # Instancia um objeto de uma janela
windows.minsize(1366,768)
windows.title("Python Course GUI!")
label = Label(windows, text="Hello World!", font=("Arial", 40, "bold"), bg="#00ff00")
label.pack()
windows.mainloop()  # Abre a janela na tela aguardando por eventos
