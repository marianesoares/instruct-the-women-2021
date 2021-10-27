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
    
    package_name = package["name"]
    version = package["version"]
    
    if 'version' not in package:

        response = requests.get(f"https://pypi.python.org/pypi/{package_name}/{version}/json")
        
        if response.status_code == 400: 
            response.data = {
                "error": "One or more packages doesn't exist"
            }
        elif response.status_code == 201: 
            response.data = {
                'name': response.json()["info"]['name'],
                'version':
                    response.json()["info"]['name']
            }
    else: 
        response = requests.get(f"https://pypi.python.org/pypi/{package_name}/{version}/json")
        versions = data.json()["releases"].keys()

    return versions


def latest_version(package_name):
    # TODO
    # Fazer requisição na API do PyPI para descobrir a última versão
    # de um pacote. Retornar None se o pacote não existir.
    package_name = package["name"]
    versions = version_exists(package_name, versions)
    
    if "version" not in package.keys(): 
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        
        if response.status_code == 400:
            response.data = {
                "error": "One or more packages doesn't exist"
            }
        else: 
            package["version"] = list(versions).pop()

    return package
