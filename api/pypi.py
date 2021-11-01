import requests
import json

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content

def version_exists(package_name, version):
    # TODO
    # Fazer requisição na API do PyPI para checar se a versão existe
    
    #package_name = package["name"]
    #version = package["version"]
    
    response = requests.get(f"https://pypi.python.org/pypi/{package_name}/{version}/json")
        
    if response.status_code == 400: 
        False
    else: 
        return True


def latest_version(package_name):
    # TODO
    # Fazer requisição na API do PyPI para descobrir a última versão
    # de um pacote. Retornar None se o pacote não existir.
    #package_name = package["name"]
    #versions = version_exists(package_name, versions)
    
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        
    if response.status_code == 400:
        return None
        
    else: 
        response = response.json()
        version = response['info']['version']
        return version
