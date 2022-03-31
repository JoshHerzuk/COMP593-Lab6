import requests
from sys import argv


def main():
    poke_name = argv[1]

    poke_info = get_poke_info(poke_name)
    

def get_poke_info(poke_name):
    print("Retrieving Pokemon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + poke_name)

    if response.status_code == 200:
        print("Success")
        return response.json()
    else:
        print('failed. Response code:', response.status_code)
        return
       
