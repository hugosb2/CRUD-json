import json

class editar:
    def editarDados():
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        
        nome_atual = input("Digite o nome atual do usuário que deseja renomear: ")

        if nome_atual not in usuarios:
            print("Usuário não encontrado!")
            return

        print("USUÁRIO ENCONTRADO!\nO Que deseja editar?\n\n")
        print("1. Nome\n2. Idade\n3. Email\n4. Voltar")

        escolha = int(input("Digite a opção aqui: "))

        if escolha == 1:
            print("Editar nome\n")
            novo_nome = input("Digite o novo nome: ")
            usuarios[novo_nome] = usuarios.pop(nome_atual)
            print("Nome atualizado com sucesso\n\n")

        elif escolha ==2:
            print("Editar idade\n")
            usuarios[nome_atual]["idade"] = input("Digite a nova idade: ")
            print("Idade atualizada com sucesso\n\n")

        elif escolha == 3:
            print("Editar e-mail\n")
            usuarios[nome_atual]["email"] = input("Digite o novo email: ")
            print("E-mail atualizado com sucesso\n\n")

        elif escolha == 4:
            return

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)