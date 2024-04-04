from CepApi import Endereco

class TestEndereco:
  def test_obter_endereco_cep_valido(self):
        endereco = Endereco()
        endereco.obter_endereco("13610350")
        assert endereco is not None

  def test_validar_cep_incorreto(self):
    endereco = Endereco()
    resultado = endereco.validar_cep("abc12345")
    assert resultado is False

  def test_formatar_endereco_valido(self):
    enderecoText = {'logradouro': 'Rua Teste', 'numero': '123', 'bairro': 'Centro', 'localidade': 'Cidade', 'uf': 'UF'}
    endereco = Endereco()
    resultado = endereco.formatar_endereco(enderecoText)
    assert resultado is not None

  def test_formatar_endereco_invalido(self):
    enderecoText = None
    endereco = Endereco()
    resultado = endereco.formatar_endereco(enderecoText)
    assert resultado == "Não foi possível encontrar o endereço para o CEP fornecido."


test = TestEndereco()
test.test_obter_endereco_cep_valido()
print("Teste obter enderecço CEP valido - OK")    
test.test_validar_cep_incorreto()
print("Teste validar CEP incorreto - OK")
test.test_formatar_endereco_valido()
print("Teste formatar endereço valido - OK")
test.test_formatar_endereco_invalido()
print("Teste formatar endereço inválido - OK")