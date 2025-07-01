import json, os

class cadastro:
    def cadastrarDados():

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        usuario = input("Digite um nome de usuário: ")
        email = input("Digite seu email: ")


        if os.path.exists("dados.json"):
            with open ("dados.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
            
            if usuario in usuarios:
                print("Há um usuário com esse nome")
                return
        else:
            usuarios = {}
        
        usuarios[usuario] = {"nome": nome, "idade":idade, "email":email}

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

        print("Dados salvos com sucesso!")