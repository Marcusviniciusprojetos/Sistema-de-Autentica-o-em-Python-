import sqlite3

# Usando 'with' para a criação da tabela
with sqlite3.connect('banco_de_dados_Usuários.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            cpf TEXT PRIMARY KEY,
            nome_usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

def cadastro_usuario():
    Pergunta_Cadastro = input('Pronto para se Cadastrar?, Digite:(sim/não):')
    if Pergunta_Cadastro.lower().strip() == 'sim':
        print('Começando...\n')

    elif Pergunta_Cadastro.lower().strip() == 'não'or Pergunta_Cadastro.lower().strip() == 'nao': 
        print('sem problemas, nos vemos in outra hora.')
        quit()
    else:
         print('❌ Erro: Resposta inválida! Digite apenas "sim" ou "não"\n')

def nomeação_cpf():

    while True:
        cpf_usuario = input("QUAL É O SEU CPF?:").strip()

        if len(cpf_usuario) != 11 or not cpf_usuario.isdigit():
            print("❌ Erro: O CPF deve conter exatamente 11 números!, sem pontos, traços ou letras! \n")
        
        else:
            with sqlite3.connect('banco_de_dados_Usuários.db') as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT cpf FROM usuarios WHERE cpf = ?', (cpf_usuario,))
                resultado = cursor.fetchone()

            if resultado is None:
                print("✅ CPF disponível e registrado! Pode continuar...")
                return cpf_usuario
            else:
                print("❌ Erro: Este CPF já está cadastrado! Tente outro.\n")

def nomeação_usuario():
    nome_usuario = input("QUAL É O SEU NOME?:")
    print(f"Olá, {nome_usuario}")
    return nome_usuario

def nomeação_senha():
    senha_usuario = input("QUAL SERÁ SUA SENHA?:")
    print("senha criada com sucesso!\n")
    return senha_usuario

def tela_de_login():
    print("\n=== AGORA FAÇA SEU LOGIN ===")

    with sqlite3.connect('banco_de_dados_Usuários.db') as conexao:
        cursor = conexao.cursor()
        while True:
            login_cpf = input("Digite Cpf: ")
            login_user = input("Digite Usuário: ")
            login_senha = input("Digite Senha: ")
        
            cursor.execute('SELECT * FROM usuarios WHERE cpf = ? AND nome_usuario = ? AND senha = ?', 
                           (login_cpf, login_user, login_senha))
            usuario_encontrado = cursor.fetchone()

            if usuario_encontrado is not None:
                print("🎉 Logado com sucesso!")
                break  
            else:
                print("❌ Incorreto! Tente digitar os dados de novo.\n")

def iniciar_sistema_cadastro():
    cadastro_usuario()

    dados_cpf = nomeação_cpf()
    dados_nome = nomeação_usuario()
    dados_senha = nomeação_senha()
    
    with sqlite3.connect('banco_de_dados_Usuários.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (cpf, nome_usuario, senha) 
            VALUES (?, ?, ?)
        ''', (dados_cpf, dados_nome, dados_senha))
    
    print("🎉 Usuário salvo no banco de dados com sucesso!")

    tela_de_login()

print('Bem Vindo ao Marcus tech')
Pergunta_Start = input("Você possui um Cadastro?, Digite:(sim/não):")

if Pergunta_Start.lower().strip() == 'sim':
    tela_de_login()

elif Pergunta_Start.lower().strip() == 'não' or Pergunta_Start.lower().strip() == 'nao':
    iniciar_sistema_cadastro()
else:
    print('❌ Erro: Resposta inválida! Digite apenas "sim" ou "não".')
