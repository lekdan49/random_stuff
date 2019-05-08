import requests
import sys
import json

id_nums = []


class var_1:
    #query_search = input("GAMES-PC, GAMES, thats about it!  enter which one u want! ")
    query_search = "PC-GAMES"
    response = requests.get("https://predb.ovh/api/v1/?q={}".format(query_search)).json()
    f = open("check_ids.txt", "a")
    data = response


def api_alive():
    predb_status = var_1.data["status"]
    if predb_status == "success":
        print("api is alive")
        main_script()
    else:
        print("its offline")
        sys.exit()

def main_script():
    numbers = var_1.data["data"]["rows"][0]['id']
    for number in var_1.data:
        asd = number["data"]["rows"][0]['id']
        print(asd)


api_alive()  #check if api is online

