import requests

class Endereco:
    def obter_endereco(self, cep):
        try:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except:
            return None
    
    def validar_cep(self, cep):
        if len(cep) == 8 and cep.isdigit():
            return True
        else:
            return False

    def formatar_endereco(self, endereco):
        if endereco['erro'] == False:
            formatted_address = f"Endereço encontrado: {endereco['logradouro']}, {endereco['bairro']}\nCidade: {endereco['localidade']}-{endereco['uf']}"
            return formatted_address
        else:
            return "Não foi possível encontrar o endereço para o CEP fornecido."

def main():
    
    while True:
        cep = input("Digite o CEP (somente números): ")
        endereco = Endereco()
        if endereco.validar_cep(cep):
            endereco_obtido = endereco.obter_endereco(cep)

            if (endereco_obtido is None):
                print("não foi possível comunicar com a API")
                return
            
            endereco_formatado = endereco.formatar_endereco(endereco_obtido)
            print(endereco_formatado)
            break
        else:
            print("CEP inválido. Certifique-se de inserir um CEP com 8 dígitos numéricos.")

if __name__ == "__main__":
    main()