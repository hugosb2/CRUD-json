import json

class excluir:
    def excluirDados():
        with open ("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        usuario = input("Digite o nome do usuário que deseja excluir: ")
        
        del dados[usuario]

        print("Usuário apagado com sucesso\n\n")

        with open ("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)