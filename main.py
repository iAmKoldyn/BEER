from curses import beep
import requests
import json
from bs4 import BeautifulSoup

headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "bx-ajax": "true"
        }

url_beer = "https://beerkontora.ru/beer/page-1/"
url_sidr = "https://beerkontora.ru/sidr/page-1/"
url_shoc = "https://beerkontora.ru/shocolate/page-1/"
url_water = "https://beerkontora.ru/water/page-1/"
url_napitki = "https://beerkontora.ru/napitki/page-1/"
url_coffee = "https://beerkontora.ru/kofe/page-1/"
s = requests.Session()

dict = {}


def get_all_beer():
    """doesn`t work correctly, ошибка после натыкания на отсутствие цены, добавить обработчик ошибок| Beer"""
    response = s.get(url=url_beer, headers=headers)
    for page in range(1, 70):
        response = s.get(url=f"https://beerkontora.ru/beer/page-{page}/",headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")

        for i in container:
            try:
                beer_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                beer_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                beer_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
                dict[title] = (beer_hrefs,beer_image,beer_price)
            except: pass

        # with open("data/beer.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False)


def get_all_shocolateie():
    """works correctly| Shocolate"""
    response = s.get(url=url_shoc, headers=headers)
    for page in range(1, 4):
        response = s.get(url=f"https://beerkontora.ru/shocolate/page-{page}/",headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")

        for i in container:
            try:
                shoc_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                shoc_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                shoc_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
                dict[title] = (shoc_hrefs, shoc_image, shoc_price)
            except: pass


        # with open("data/shocolate.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False)

            
def get_all_sidr():
    """works correctly| Sidr"""
    response = s.get(url=url_sidr, headers=headers)
    for page in range(1, 7):
        response = s.get(url=f"https://beerkontora.ru/sidr/page-{page}/",headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")

        for i in container:
            try:
                sidr_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                sidr_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                sidr_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
                dict[title] = (sidr_hrefs, sidr_image, sidr_price)
            except: pass
        # with open("data/sidr.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False)    


def get_all_water():
    """works correctly| Watter"""
    response = s.get(url=url_water, headers=headers)
    for page in range(1, 8):
        response = s.get(url=f"https://beerkontora.ru/water/page-{page}/",headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")
    
        for i in container:
            try:
                water_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                water_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                water_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
                dict[title] = (water_hrefs, water_image, water_price)
            except: pass

        # with open("data/water.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False)    


def get_all_napitki():
    """works correctly| Naptiki"""
    response = s.get(url=url_napitki, headers=headers)
    for page in range(1, 6):
        response = s.get(url=f"https://beerkontora.ru/napitki/page-{page}/",headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")
        
        for i in container:
            try:
                napitki_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                napitki_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                napitki_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
                dict[title] = (napitki_hrefs, napitki_image, napitki_price)
            except: pass

        # with open("data/napitki.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False) 


def get_all_coffee():
    """works correctly| Coffe"""
    response = s.get(url=f"https://beerkontora.ru/kofe/page-0/",headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    container = soup.find_all("div", class_="ty-column5")
    for i in container:
        try:
            coffee_hrefs = i.find("a", class_="product-title").get("href")
            title = i.find("a", class_="product-title").text
            coffee_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
            coffee_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0","")
            dict[title] = (coffee_hrefs, coffee_image, coffee_price)
        except: pass

        # with open("data/kofe.json", "w", encoding='utf-8') as f:
        #     json.dump(dict, f, indent=4, ensure_ascii=False)

def main():
    get_all_beer()
    get_all_shocolateie()
    get_all_sidr()
    get_all_water()    
    get_all_napitki()
    get_all_coffee()

    
if __name__ == "__main__":
    main()