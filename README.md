
# :monkey_face: Automação de testes funcionais Financeiro :see_no_evil: :hear_no_evil: :speak_no_evil:

## Instalação/Configuração do projeto 

### Instalar o Python 3.8

Instalar bibliotecas de desenvolvimento:

````
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
````

Download do Python 3.8

````
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
sudo tar xzf Python-3.8.1.tgz
````

Compilar Python

````
cd Python-3.8.1
sudo ./configure --enable-optimizations
sudo make altinstall
````

Verificar versão do Python

````
python3.8 -V
````

> Python-3.8.1

Remover arquivo baixado
````
cd /opt
sudo rm -f Python-3.8.1.tgz
````

### Configurar

Baixar o driver do browser a ser utilizado na automação:

>https://selenium-python.readthedocs.io/installation.html#drivers

Mover o arquivo baixado para a pasta ***/usr/local/bin***

Criar um .env utilizando o exemplo do .env.exemplo:

* Informar qual driver será utilizado
* Senha e login para o acesso ao sistema
* Informar configurações do banco de dados a ser utilizado

venv — Criação de ambientes virtuais

````
python3.8 -m venv; python3.8 -m venv .venv; python3.8 -c "import site; print(site.getsitepackages()[0])"; source .venv/bin/activate; echo $VIRTUAL_ENV; python3.8 -c 'import sys; print("\n".join(sys.path))'; pip3.8 install --upgrade pip
````

  

Baixar os pacotes requeridos

````
pip3.8 install -r requirements.txt
````


## Executar testes com base de dados local

Para minimizar o problema de delay com bases de dados é possivel executar os testes com base de dados local. 
Para isso é nescessario configurar o BDD, ERP e as APIS com o mesmo banco.

````
DB_HOST={NOME HOST LOCAL}
DB_PORT={PORTA}
DB_NAME=vhsys_erp_test #NOME PADRAO DO BANCO 
DB_USER={USUARIO}
DB_PASS={SENHA}
````

## Fontes para composição deste README:

>https://selenium-python.readthedocs.io/

>https://behave.readthedocs.io/en/latest/

>https://docbehat.readthedocs.io/pt/v3.1/guides/1.gherkin.html

>https://tecadmin.net/install-python-3-8-ubuntu/
