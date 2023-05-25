from chalice import Chalice
import requests
import json
from deep_translator import GoogleTranslator
import boto3
from io import BytesIO
from faker import Faker


app = Chalice(app_name='image-extract')

@app.lambda_function()
def first_function(event, context):
    downloadImage = requests.get(event['URL'])

    # filename = "test.jpg"
    # data = {'file': open(filename, 'rb')}

    # dicionario json com o conteúdo do arquivo (USAMOS UMA VARIÁVEL DUPLA PARA NOMEAR O ARQUIVO)
    data = {'file': ("image.jpg", downloadImage.content)}
    
    # extraíndo o texto da imagem com a freeOCRapi
    sendImage = requests.post("https://freeocrapi.com/api", files=data)
    jsonTemp = json.loads(sendImage.content)
    texto_original = jsonTemp["text"]

    # traduzindo o texto para o inglês
    texto_em_ingles = GoogleTranslator(source='auto', target='en').translate(texto_original)

    #criar o client() para fazer a conexão s3
    s3_connection = boto3.client('s3', endpoint_url=("http://host.docker.internal:4566"))

    texto_em_ingles = texto_em_ingles.encode('utf-8')
    upload_bucket = BytesIO(texto_em_ingles)
    #criando um bucket
    s3_connection.create_bucket(Bucket='mybucket')
    s3_connection.upload_fileobj(upload_bucket, 'mybucket', Faker().uuid4())
    # s3_connection.Object('mybucket', upload_bucket).put(Body=upload_bucket)
    return {'Texto da imagem traduzido para o ingles': texto_em_ingles}

# Listar arquivos do bucket 
# awslocal s3 ls s3://mybucket

# awslocal s3 rm s3://mybucket/his.flac

# Ler conteúdo do arquivo
# awslocal s3 cp s3://mybucket/tradução - | cat
# awslocal s3 cp s3://mybucket/tradução teste.txt

#para listar os serviços buckets s3 rodados do AWS
# awslocal s3 ls

#criar o bucket

#subir para o bucket
# translated = GoogleTranslator(source='auto', target='en').translate(texto_original)

    #receber uma url através de um json valido usando alguma função
    #url_da_imagem=event['URL']
    # texto_da_imagem = extrair_texto_da_imagem(url_da_imagem)
    # return {'Texto da imagem': jsonTemp["text"]}

#Testar:
# chalice-local deploy
# echo "{\"URL\":\"https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg\"}" | chalice-local invoke -n first_function

# echo "{\"URL\":\"https://files.liveworksheets.com/def_files/2021/7/27/107272241171984590/107272241171984590001.jpg"}" | chalice-local invoke -n first_function

# echo "{\"URL\":\"https://files.liveworksheets.com/def_files/2021/7/27/107272241171984590/107272241171984590001.jpg\"}" | chalice-local invoke -n first_function

# echo "{\"URL\":\"https://cdn.pensador.com/img/frase/fe/rn/fernando_pessoa_o_mar_salgado_quanto_do_teu_sal_sao_lag_lk8r633.jpg\"}" | chalice-local invoke -n first_function

# chalice-local invoke -n first_function

# https://cdn.pensador.com/img/imagens/pe/ns/pensador_mensagens_de_bom_dia_21.jpg?auto_optimize=low&width=655


# Your deployment will continue but may not work correctly
# if missing dependencies are not present. For more information:
# http://aws.github.io/chalice/topics/packaging.html

# Updating policy for IAM role: image-extract-dev
# Updating lambda function: image-extract-dev-first_function
