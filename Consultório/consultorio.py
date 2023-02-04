infoCliente = {
		"nome": "Kevin Bruno Aragão",
		"idade": 36,
		"cpf": "670.673.096-38",
		"rg": "49.655.670-8",
		"data_nasc": "02/02/1987",
		"sexo": "Masculino",
		"signo": "Aquário",
		"mae": "Antônia Aurora Fabiana",
		"pai": "Henry Carlos Eduardo Aragão",
		"email": "",#"kevin_aragao@ligananet.com.br",
		"senha": "",#"MiUJ4DnN72",
		"cep": "79321-065",
		"endereco": "Alameda Catarina",
		"numero": 297,
		"bairro": "Popular Nova",
		"cidade": "Corumbá",
		"estado": "MS",
		"telefone_fixo": "(67) 3893-8351",
		"celular": "(67) 99337-5920",
		"altura": 2.00,
		"peso": 74,
		"tipo_sanguineo": "A+",
		"cor": "roxo"
}
consultasAgendadas = {
    infoCliente["nome"]: {
		"Data": "",#"08/12/2023",
        "Especialista": ""#"Neurologista"
	}
}
def login(email, senha):
    if(email != infoCliente["email"] or senha != infoCliente["senha"]):
        print("Dados inseridos estão incorretos, verifique as informações de login")
        return False
    else:
        print("Logando...")
        return True
def verificaAgenda():
    for consulta in consultasAgendadas[infoCliente["nome"]]:
        
        pass
def verificaPlano():

    pass
def agendarConsulta():
    pass
def cancelarConsulta():
    pass
def encerrarAtendimento():
    print("Encerrando atendimento...")
    return False
def menu():
    print(f"""
Olá, {infoCliente['nome']}, escolha o que deseja fazer:
1 - Verificar consultas agendadas
2 - Verificar planos da clínica
3 - Agendar uma consulta
4 - Cancelar uma consulta
5 - Encerrar atendimento
    """)
    resposta = int(input("Sua resposta: "))
    match resposta:
        case 1:
            verificaAgenda()
        case 2:
            verificaPlano()
        case 3:
            agendarConsulta()
        case 4:
            cancelarConsulta()
        case 5:
            encerrarAtendimento()
    
		
print(f"{'Clínica Guimars Health':-^50}")
print(f"{'LOGIN':^50}")
while True:
    email = input("Insira o seu email: ")
    senha = input("Insira a sua senha: ")
    if(login(email, senha)):
        if(menu()):
            pass
        else:
            break