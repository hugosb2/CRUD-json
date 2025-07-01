import json

class ler:
    def lerDados():
        with open ("dados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        print("\nTotal de Usuários: ", len(usuarios), "\n\nLista de usuários: \n")

        for usuario, dados in usuarios.items():
            print(f"Nome: {usuario}, Nome: {dados['nome']}, Idade: {dados['idade']}, E-mail: {dados['email']}")
        print("\n\n")