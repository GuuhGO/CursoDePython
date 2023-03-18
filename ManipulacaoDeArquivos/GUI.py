from tkinter import *
from tkinter import ttk
alunos = {}
window = Tk(className="Cadastro alunos")
window.minsize(940,470)
window.config(width=940,height=470)
titulo = Label(master=window, text="Cadastro de Alunos!", font=("Arial",16,"bold"), border=2, relief="solid", padx=4, pady=2)
titulo.pack(pady=5)
div_main = Frame(master=window, width=440, height=380, border=2, relief="solid")
div_main.pack(pady=5)
nomeAluno = Label(master=div_main, text="Nome", font=("Arial",14))
nomeAluno.place(x=5,y=5)
in_nomeAluno = Entry(master=div_main, font=("Arial", 12))
in_nomeAluno.place(x=240,y=10)

idadeAluno = Label(master=div_main, text="Idade", font=("Arial",14))
idadeAluno.place(x=5,y=50)
in_idadeAluno = Entry(master=div_main, font=("Arial", 12))
in_idadeAluno.place(x=240,y=50)

pesoAluno = Label(master=div_main, text="Peso", font=("Arial",14))
pesoAluno.place(x=5,y=95)
in_pesoAluno = Entry(master=div_main, font=("Arial", 12))
in_pesoAluno.place(x=240,y=95)

btn_register = Button(master=div_main, text="Cadastrar" , font=("Arial", 12))
btn_register.place(
    x=(div_main.winfo_reqwidth()-btn_register.winfo_reqwidth())/2,
    y=140
)

window.mainloop()