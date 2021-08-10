import requests

def retorna_logradouro_complemento_estado(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    print("Logradouro: "+dados_cep['logradouro'] + "\n" + "Complemento: " + dados_cep['complemento'] + "\n" + "Estado: " + dados_cep['localidade'])
    return dados_cep

if __name__ =='__main__':
    retorna_logradouro_complemento_estado('01001000')