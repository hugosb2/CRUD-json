import json

class excluir:
    def excluirDados():
        with open ("dados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        
        print("\nTotal de Usuários: ", len(usuarios), "\n\nLista de usuários: \n")

        for usuario, dados in usuarios.items():
            print(f"Nome: {usuario}, Nome: {dados['nome']}, Idade: {dados['idade']}, E-mail: {dados['email']}")
        print("\n\n")
        
        usuario = input("Digite o nome do usuário que deseja excluir: ")
        
        del usuarios[usuario]

        print("Usuário apagado com sucesso!\n\n")

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)