# CEP Busca

Este é um programa simples para buscar informações de endereços usando o CEP, utilizando a API do ViaCEP.

## Configuração do Ambiente

1. **Criação e Ativação do Ambiente Virtual**:

   - Crie um novo ambiente virtual na pasta do projeto:
     ```
     python -m venv env
     ```
   - Na pasta do projeto, ative o ambiente virtual:
   
       ```
       .\env\Scripts\activate
       ```
     

2. **Instalação de Dependências**:
   - Instale o pacote `requests`:
     ```
     py -m pip install requests
     ```
   - Exporte as dependências para o arquivo `requirements.txt`:
     ```
     py -m pip freeze > requirements.txt
     ```

## Utilização da Aplicação

- Execute o programa Cep.py para buscar informações de endereço usando o CEP:
    ```
    py Cep.py
    ```

- Siga as instruções fornecidas para inserir o CEP desejado.
- O programa irá mostrar as informações do endereço correspondente ao CEP inserido.

## Execução dos Testes

- Execute o arquivo TestCep.py para executar os testes unitários:
    ```
    py TestCep.py
    ```