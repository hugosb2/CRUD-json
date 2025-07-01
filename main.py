from cadastro import cadastro
from ler import ler
from editar import editar
from excluir import excluir

class CRUD:
    def main():
        while True:
            print("BOAS VINDAS!\nO que deseja fazer?\n")
            print("1. Cadastrar Usuário\n2. Listar usuários\n3. Editar nome do usuário\n4. Apagar dados\n5. Sair")
            opcao = int(input("Digite a opção aqui: "))

            if opcao == 1:
                cadastro.cadastrarDados()
            elif opcao == 2:
                ler.lerDados()
            elif opcao == 3:
                editar.editarDados()
            elif opcao == 4:
                excluir.excluirDados()
            elif opcao == 5:
                print("Programa encerrado com sucesso!")
                break
            else:
                print("digite uma opção válida!")

CRUD.main()