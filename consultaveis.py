import requests
import json
from colorama import init, Fore, Style

# Inicializa a biblioteca colorama
init()

# Define a função para imprimir a arte ASCII colorida
def print_ascii_art():
    print(Fore.BLUE + Style.BRIGHT + """

██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗     ██╗     ███████╗ █████╗ ██╗  ██╗███████╗
██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗    ██║     ██╔════╝██╔══██╗██║ ██╔╝██╔════╝
██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝    ██║     █████╗  ███████║█████╔╝ ███████╗
██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗    ██║     ██╔══╝  ██╔══██║██╔═██╗ ╚════██║
╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║    ███████╗███████╗██║  ██║██║  ██╗███████║
 ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

""" + Style.RESET_ALL)

# Exibe a arte ASCII
print_ascii_art()

# Solicita o endereço de e-mail a ser consultado
email = input("AH MALANDRO, QUER CONSULTAR UNS LEAKS? DIGITE O ENDEREÇO DE EMAIL: ")

# Faz a consulta na API
url = f"https://beta.snusbase.com/v2/combo/{email}"
response = requests.get(url)

# Verifica se a consulta foi bem sucedida
if response.status_code == 200:
    # Exibe os resultados da consulta
    results = response.json()
    print(f"Foram encontrados {len(results)} resultados para o e-mail {email}:")
    print(json.dumps(results, indent=4, sort_keys=True))
else:
    # Exibe uma mensagem de erro
    print(Fore.RED + f"Não foi possível consultar o e-mail {email}. Código de status: {response.status_code}" + Style.RESET_ALL)
