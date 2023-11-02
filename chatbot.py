#Chatbot Integrado com o ChatGPT
#Usei um ambiente virtual

import openai
# Biblioteca para o chatgpt

chave_api = "Escre aqui sua chave API"
openai.api_key = chave_api
# A chave API você gera no mesmo site do chatgpt

def enviar_mensagem(mensagem, lista_mensagens=[]):
    # Adiciona a mensagem do usuário à lista de mensagens
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    # Faz uma solicitação ao modelo de linguagem GPT-3.5 Turbo com as mensagens
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )
    
    # Retorna a resposta gerada pelo modelo
    return resposta["choices"][0]["message"]

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta["content"])
# print(enviar_mensagem("Em que ano Eistein publicou a teoria geral da relatividade?"))