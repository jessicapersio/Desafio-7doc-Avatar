from googletrans import Translator
# from API_AVATAR.dia_1.requisicao import avatar_api
import requests
import json

def avatar_api ():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"

    response = requests.get(url)

    return response.json()
    

def traduzir_texto(texto): # declara uma função que recebe um texto 
    tradutor = Translator() # iniicio um tradutor
    return tradutor.translate(text=texto, dest='pt_BR').text # retorno o texto traduzido para pt_br

def traduzir_api():
    response = avatar_api() # declaro como a respota da api
    response_1_afi = response[1].get('affiliation') 
    
    print(traduzir_texto(response_1_afi))

traduzir_api()
