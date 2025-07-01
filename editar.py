import json

class editar:
    def editarDados():
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        
        nome_atual = input("Digite o nome atual do usuário que deseja renomear: ")

        novo_nome = input("Digite o novo nome: ")

        usuarios[novo_nome] = usuarios.pop(nome_atual)

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
        
        print("Dados editados com sucesso!\n\n")