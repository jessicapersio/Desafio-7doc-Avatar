# 🌊 Desafio Avatar API - 7 Days of Code (Python Web)

Este projeto é uma solução para um dos desafios do programa [#7DaysOfCode](https://7daysofcode.io/matricula/python-web), focado em requisições HTTP com Python. Aqui, usamos a API pública de *Avatar: The Last Airbender* para explorar dados dos personagens da série.

##  Descrição do desafio

O objetivo é fazer uma requisição GET para a API do universo Avatar e listar informações como:
- Nome do personagem
- Afiliação
- Inimigos e aliados
- Imagem do personagem

A API utilizada é pública e pode ser acessada em:  
[https://last-airbender-api.fly.dev](https://last-airbender-api.fly.dev)

---

## Tecnologias usadas

- Python 3
- Biblioteca [`requests`](https://pypi.org/project/requests/) para fazer requisições HTTP

---

## ▶ Como executar

1. Clone este repositório:
```bash
git clone https://github.com/jessicapersio/Desafio-7doc-Avatar?tab=readme-ov-file
cd avatar-api-desafio
```
2. Instale o módulo requests (caso ainda não tenha):
pip install requests

3. Execute o Script:
python avatar.py

Exemplo de retorno:
{
  "name": "Aang",
  "affiliation": "Air Nomads",
  "allies": ["Team Avatar", "Zuko"],
  "enemies": ["Azula"],
  "photoUrl": "https://link-da-imagem.jpg"
}
##  Autora

Desenvolvido por [Jéssica Persio](https://www.linkedin.com/in/jessicapersio)  
📬 Email: [jepersio@hotmail.com](mailto:jepersio@hotmail.com)