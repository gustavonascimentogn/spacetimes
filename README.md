# spacetimes
Projeto baseado nos conceitos de micro serviços, utilizando Python3, Django, Django Rest Framework, Celery, Redis e SQLLite (podendo ser trocado para qualquer outro SGBD Relacional).

As funcionalidades baseiam-se no recebimento de arquivos de texto (txt ou csv) e processamento destes, visando saber a quantidade de palavras iniciadas com cada letra do alfabeto (case insensitive). 
O sistema recebe o arquivo do usuário via API ou HTTP e processa de forma assíncrona, gerenciando o processamento através de uma fila de execução. Através da interface do usuário (logado), o sistema permite consultar o status dos processamentos em fila, em execução ou já concluídos. 
O sistema armazena, para cada processamento, o tempo de execução e o tempo de espera na fila de processamento, além do resultado gerado.

####################
#### INSTALAÇÃO ####

### Criar venv para o projeto (Python3)
python3 -m venv spacetime

### Ativar venv criada
. spacetime/Scripts/activate 


### Clonar repositório do Github
https://github.com/gustavonascimentogn/spacetimes.git

### Acessar diretório do projeto clonado chamado "spacetimes"
cd spacetimes


### Instalar os requisitos necessários dentro da venv criada
pip install -r requirements.txt


### Baixar Redis do link a seguir (versão especificamente utilizada para os fins deste projeto)
https://drive.google.com/drive/folders/1TMe9EXkJqgFI0yEiP75N1OyYE0Em0XI_?usp=sharing

Após download, descompacte o arquivo em qualquer diretório e execute o arquivo "redis-server.exe". Ele criará uma instância do Redis em seu ambiente Windows.
Caso esteja em ambiente Linux, instale o Redis via comandos Linux e altere a configuração CELERY_BROKER_URL, no arquivo "[raiz_projeto]/spacetimes/local_settings.py" e no arquivo "[raiz_projeto]/spacetimes/celery.py"


# ---> ARQUIVO local_settings.py


CELERY_RESULT_BACKEND = 'django-db'

CELERY_BROKER_URL = 'redis://localhost:6379' 

CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_SERIALIZER = 'json'


# ---> ARQUIVO celery.py

app = Celery('spacetimes',broker='redis://localhost:6379')


### Execute o Redis (No Windows)

Execute o arquivo "redis-server.exe". Ele criará uma instância do Redis em seu ambiente Windows.


### Execute o Celery (esteja certo que a venv esteja ativa)
# No windows

celery -A spacetimes worker --pool=solo -l INFO


# No Linux

celery -A spacetimes worker -l INFO


### Abra outro terminal e execute a aplicação Spacetime

#Ative a venv no novo terminal
. spacetime/Scripts/activate 

#Execute o comando runserver para rodar a aplicação
python manage.py runserver


### Video rápido mostrando o start da aplicação

https://drive.google.com/drive/folders/1TMe9EXkJqgFI0yEiP75N1OyYE0Em0XI_?usp=sharing


###################
#### NAVEGAÇÃO ####

### HTTP 

http://127.0.0.1:8000/
user: django
senha: django

Nesta visualização (Web) o usuário consegue acompanhar o processamento dos arquivos que ele próprio enviou via HTTP ou via API REST. 


#######################
#### ADMINISTRADOR ####

http://127.0.0.1:8000/admin
user: django
senha: django

Como Administrador é possível criar novos usuários, criar novos tokens de autorização para o envio de arquivos via API REST e visualizar os dados a respeito dos arquivos (Arquivos) e da fila de processamento (Task results).

OBSERVAÇÃO: No layout para usuário (não para Administrador), a visualização dos processamentos é mais amigável.


##################
#### API REST ####


# URL para navegação obtenção dos Endpoints - API REST (URL Endpoint)
http://127.0.0.1:8000/api




#---------------------------------------------------------
# O arquivo Spacetimes.postman_collection.json é uma Collection do Postman
#---------------------------------------------------------

Utilize este arquivo para enviar arquivo via Postman. Ele já possui toda a configuração necessária, basta importa-lo como Collection.




#---------------------------------------------------------
# Exemplo de código Python para envio de arquivo via API REST 
#---------------------------------------------------------

O BD SQLite utilizado no projeto já contém o Token informado no exemplo


import requests
url = "http://127.0.0.1:8000/api/arquivos/"

payload={'nome': 'nome_amigavel_arquivo'}
files=[
  ('arquivo',('arquivo_grande.txt',open('/C:/Users/gusta/Downloads/arquivo_grande.txt','rb'),'text/plain'))
]
headers = {
  'Authorization': 'Token 2efbc435f13109037e466c7031bbea459d99c3ba'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)




