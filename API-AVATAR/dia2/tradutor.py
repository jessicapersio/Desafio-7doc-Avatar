from googletrans import Translator
from requisicao import avatar_api

def traduzir_personagens(lista_original):
    tradutor = Translator()
    lista_traduzida = []
   
   for character in lista_original:
        nome_en = personagem.get("name", "")
        afiliacao_en = personagem.get("affiliation", "")
        nome_pt = translator.translate(nome_en, src="en", dest="pt").text if nome_en else ""
        afiliacao_pt = translator.translate(afiliacao_en, src="en", dest="pt").text if afiliacao_en else ""
         personagem_traduzido = {
            "nome": nome_pt,
            "afiliacao": afiliacao_pt
     }
             lista_traduzida.append(personagem_traduzido)

    return lista_traduzida
    from dados_avatar import dados_api  

personagens_em_portugues = traduzir_personagens(dados_api)


for p in personagens_em_portugues[:5]:  
    print(p)