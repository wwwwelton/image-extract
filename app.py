from chalice import Chalice
# from botocore.vendored import requests
import pytesseract
# from PIL import Image
# from io import BytesIO


app = Chalice(app_name='image-extract')

@app.lambda_function()
def first_function(event, context):
    #receber uma url através de um json valido usando alguma função
    # url_da_imagem=event['URL']
    # texto_da_imagem = extrair_texto_da_imagem(url_da_imagem)

    return(print(pytesseract.image_to_string(Image.open('pensador_mensagens_de_bom_dia_21.jpg'))))
    # return {'Url da imagem': texto_da_imagem,
    #         'Texto da image': texto_da_imagem}


# Função para extrair o texto da imagem na URL
# def extrair_texto_da_imagem(url):
#     # Faz o download da imagem da URL
#     texto = requests.get(url)
#     # Abre a imagem usando a PIL
#     #imagem = Image.open(BytesIO(response.content))
#     # Extrai o texto da imagem usando o pytesseract
#     #texto = pytesseract.image_to_string(imagem)
#     return texto

# chalice-local deploy

# echo "{\"URL\":\"https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg?auto_optimize=low&width=655\"}" | chalice-local invoke -n first_function

# https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg?auto_optimize=low&width=655


# Could not install dependencies:
# pillow==9.5.0
# You will have to build these yourself and vendor them in
# the chalice vendor folder.

# Your deployment will continue but may not work correctly
# if missing dependencies are not present. For more information:
# http://aws.github.io/chalice/topics/packaging.html

# Updating policy for IAM role: image-extract-dev
# Updating lambda function: image-extract-dev-first_function

# Package,Package Version,arn
# Pillow,9.5.0,arn:aws:lambda:ap-south-1:770693421928:layer:Klayers-p38-Pillow:7