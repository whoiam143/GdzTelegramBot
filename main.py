import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}


def get_number_png(subject, klass, number, autor, images="", new="", check=""):
    if new == "new":
        req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}/images{images}/new/{number}.png",
                           headers=headers)
    elif new == "2":
        req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}2/images{images}/{number}.png",
                           headers=headers)
    elif new == "part2":
        req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}/images{images}/part2/{number}.png",
                           headers=headers)
    elif new == "clear":
        list_of_numbers = [32, 567, 633, 644]
        if int(number) in list_of_numbers:
            req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}/images4/{number}.png",
                               headers=headers)
        else:
            req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}/{number}.png",
                           headers=headers)
    elif check == "check":
        pass
    else:
        req = requests.get(f"https://reshak.ru/reshebniki/{subject}/{klass}/{autor}/images{images}/{number}.png",
                           headers=headers)
    return req.content





#https://gdz.pub/content/reshebnik-9-class/russkiy-jazyk/russkiy-9kl-Bystrova/exercise/u/187.jpg
#https://gdz.ltd/content/9-class/russkiy/russkiy-9kl-Bystrova/exercise/u/187.jpg