import json

class ler:
    def lerDados():
        with open ("dados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        print("Total de Usuários: ", len(usuarios), "\n\nLista de usuários: \n")

        for nome, dados in usuarios.items():
            print(f"Nome: {nome}, Idade: {dados['idade']}, Email: {dados['email']}")
        print("\n\n")