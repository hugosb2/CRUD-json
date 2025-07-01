# Sistema de Cadastro de Usuários (CRUD) em Python

## 📝 Descrição

Este projeto é um sistema simples de **CRUD** (Create, Read, Update, Delete) de usuários desenvolvido em Python. Ele permite cadastrar, listar, editar e excluir informações de usuários, salvando os dados em um arquivo JSON.

O sistema é modularizado, com cada funcionalidade do CRUD (Cadastrar, Ler, Editar, Excluir) separada em seu próprio arquivo e classe, e um arquivo principal (`main.py`) que gerencia a interação com o usuário através de um menu no console.

## ✨ Funcionalidades

* **Cadastrar Usuário:** Adiciona um novo usuário com nome, idade e e-mail.
* **Listar Usuários:** Exibe todos os usuários cadastrados com seus respectivos dados.
* **Editar Nome do Usuário:** Permite alterar o nome de um usuário existente.
* **Excluir Usuário:** Remove um usuário do sistema.
* **Persistência de Dados:** As informações são salvas no arquivo `dados.json`, garantindo que os dados não sejam perdidos ao fechar o programa.

## 🛠️ Tecnologias Utilizadas

* Python 3
* Módulo `json`
* Módulo `os`

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:


CRUD Json/
├── main.py
├── cadastro.py
├── ler.py
├── excluir.py
└── dados.json

* `main.py`: Ponto de entrada da aplicação. Apresenta um menu de opções para o usuário e chama as funcionalidades correspondentes das outras classes.
* `cadastro.py`: Implementa a funcionalidade de **Criação (Create)**. Solicita os dados do usuário e os salva no arquivo `dados.json`.
* `ler.py`: Implementa a funcionalidade de **Leitura (Read)**. Lê os dados do arquivo `dados.json` e os exibe no console.
* `editar.py`: Implementa a funcionalidade de **Atualização (Update)**. Permite que o usuário renomeie um registro existente.
* `exluir.py`: Implementa a funcionalidade de **Exclusão (Delete)**. Remove um registro de usuário do arquivo `dados.json`.
* `dados.json`: Arquivo gerado para armazenar os dados dos usuários após a primeira execução.

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/hugosb2/CRUD-json.git](https://github.com/hugosb2/CRUD-json.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd CRUD-json
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```
4.  **Siga as instruções no console** para escolher uma das opções do menu:
    * `1` para cadastrar um novo usuário.
    * `2` para listar todos os usuários.
    * `3` para editar o nome de um usuário.
    * `4` para apagar um usuário.
    * `5` para sair do programa.

---

## 👨‍💻 Autor

Feito por **Hugo Barros**.