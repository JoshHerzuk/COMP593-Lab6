#
#
# Description:
#   This scripts uses the poke API to gather the name and abilites of a selected pokemon
#
# Usage:
#   python Comp593 lab6.py poke_name
#
# Parameters:
#   poke_name = the pokemon you want the information for
#
#
##########################################################################################################################


import requests
from sys import argv


def main():
    poke_name = argv[1]   
    
    #gathers the information of the selected pokemon in to a json library
    poke_info = get_poke_info(poke_name)

    if poke_info:
        #creates the string from the library that contains the pokemon's name and abilitied
        pb_strings = poke_name_and_abilities(poke_info)
        #pastes the pokemon's information to pastebin
        pb_url = post_to_pastebin(pb_strings[0], pb_strings[1])

        print(pb_url)

 

def get_poke_info(poke_name): 
    #queries the poke API for information related to the pokemon specified in the command line param
    print("Retrieving Pokemon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + poke_name)

    if response.status_code == 200:
        print("Success")
        return response.json()

    else:
        print('failed. Response code:', response.status_code)
        return
          
def poke_name_and_abilities(poke_dict):
    #builds the string that will be posted to pastebin from the pokemon's library
    name = poke_dict['name'] + "'s Abilities."
    abilities = ""
    for i in poke_dict['abilities']:
        abilities += i['ability']['name'] + '\n'
        
    return(name, abilities)

def post_to_pastebin(name, abilities):
    #posts the pokemon's information to pastebin
    print("Posting to Pastebin...", end='')

    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': abilities,
        'api_paste_name': name
    }

    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)

    if response.status_code == 200:
        print("Success")
        return response.text

    else:
        print('failed. Response code:', response.status_code)
        return response.status_code



main()
