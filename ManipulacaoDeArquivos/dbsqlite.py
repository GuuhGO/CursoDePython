import sqlite3

connection = sqlite3.connect(r"ManipulacaoDeArquivos\pessoas.db")
cursor = connection.cursor()
try:
    cursor.execute("create table pessoas (id integer primary key autoincrement, nome text, idade integer, peso real)")
except sqlite3.OperationalError:
    print("Tabela já existe")
pessoasList = [
    ("Ana",22,60.0),
    ("Bruno",28,85.0),
    ("Carla",35,70.0 ),
    ("Diego",26,75.0),
    ("Eduarda",19,55.0),
    ("Felipe",31,90.0),
    ("Gustavo",21,70.0),
    ("Hugo",27,80.0),
    ("Isabela",30,75.0),
    ("João",23,72.0),
    ("Karina",26,68.0),
    ("Lucas",33,85.0),
    ("Mariana",30,70.0),
    ("Natália",21,58.0),
    ("Oliver",25,82.0),
    ("Paulo",30,75.0),
    ("Quiteria",28,70.0),
    ("Rafaela",27,68.0),
    ("Silvia",24,62.0),
    ("Tiago",30,85.0),
    ("Péricles",48,110),
    ("Jorge",48,110),
]

cursor.executemany("insert into pessoas (nome, idade, peso) values (?,?,?)", pessoasList)

cursor.execute("insert into pessoas (nome,idade,peso) values (?,?,?)", ("Fernanda", 50, 80))

for row in cursor.execute("select * from pessoas where id >= 15"):
    print(row)
connection.close()