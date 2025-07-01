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
        print("1. Nome de usuário\n2. Nome\n3. Idade\n4. Email\n5. Voltar")

        escolha = int(input("Digite a opção aqui: "))

        if escolha == 1:
            print("Editar nome de usuário\n")
            novo_nome = input("Digite o novo nome: ")
            usuarios[novo_nome] = usuarios.pop(nome_atual)
            print("Nome atualizado com sucesso\n\n")

        elif escolha ==2:
            print("Editar nome\n")
            usuarios[nome_atual]["nome"] = input("Digite o novo nome: ")
            print("Nome atualizada com sucesso\n\n")

        elif escolha ==3:
            print("Editar idade\n")
            usuarios[nome_atual]["idade"] = input("Digite a nova idade: ")
            print("Idade atualizada com sucesso\n\n")

        elif escolha == 4:
            print("Editar e-mail\n")
            usuarios[nome_atual]["email"] = input("Digite o novo email: ")
            print("E-mail atualizado com sucesso\n\n")

        elif escolha == 5:
            return

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)