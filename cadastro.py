import json, os

class cadastro:
    def cadastrarDados():
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        email = input("Digite seu email: ")


        if os.path.exists("dados.json"):
            with open ("dados.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
        else:
            usuarios = {}
        
        usuarios[nome] = {"idade":idade, "email":email}

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

        print("Dados salvos com sucesso")
