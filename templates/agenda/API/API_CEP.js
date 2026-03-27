import requests

def buscar_cep(cep):
    # Remove caracteres não numéricos (hífens, espaços, etc)
    cep_limpo = "".join(filter(str.isdigit, cep))

    if len(cep_limpo) != 8:
        return {"erro": "CEP inválido. Deve conter 8 dígitos."}

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        response = requests.get(url)
        # Verifica se a requisição HTTP foi bem-sucedida (Status 200)
        response.raise_for_status()
        
        dados = response.json()

        if "erro" in dados:
            return {"erro": "CEP não encontrado na base de dados."}
            
        return dados

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro de conexão: {e}"}

# Testando a função
meu_cep = "01001-000"
resultado = buscar_cep(meu_cep)

if "erro" in resultado:
    print(f"Ops! {resultado['erro']}")
else:
    print(f"Rua: {resultado['logradouro']}")
    print(f"Bairro: {resultado['bairro']}")
    print(f"Cidade: {resultado['localidade']} - {resultado['uf']}")