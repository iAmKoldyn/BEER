import requests
import json
import lxml
from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "bx-ajax": "true"
}

url_beer = "https://beerkontora.ru/beer/page-1/"
url_sidr = "https://beerkontora.ru/sidr/page-1/"
url_shoc = "https://beerkontora.ru/shocolate/page-1/"
url_water = "https://beerkontora.ru/water/page-1/"
url_napitki = "https://beerkontora.ru/napitki/page-1/"
url_coffee = "https://beerkontora.ru/kofe/page-1/"
s = requests.Session()



def get_all_beer():
    """works correctly| Beer"""
    dict1 = {}
    response = s.get(url=url_beer, headers=headers)
    for page in range(1, 70):
        response = s.get(url=f"https://beerkontora.ru/beer/page-{page}/", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        x = soup.find(class_="grid-list")
        container = x.find_all("div", class_="ty-column5")

        for i in container:
            try:
                beer_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                beer_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                beer_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
                dict1[title] = {'beer_hrefs':beer_hrefs, 'beer_image':beer_image, 'beer_price':beer_price}
            except:
                pass

    with open("data/beer.json", "w", encoding='utf-8') as f:
            json.dump(dict1, f, indent=4, ensure_ascii=False)


def get_all_shocolateie():
    """works correctly| Shocolate"""
    dict1 = {}
    response = s.get(url=url_shoc, headers=headers)
    for page in range(1, 4):
        response = s.get(url=f"https://beerkontora.ru/shocolate/page-{page}/", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        x=soup.find(class_="grid-list")
        container = x.find_all("div", class_="ty-column5")

        for i in container:
            try:
                shoc_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                shoc_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                shoc_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
                dict1[title] = {'shoc_hrefs':shoc_hrefs, 'shoc_image':shoc_image, 'shoc_price':shoc_price}
            except:
                pass

    with open("data/shocolate.json", "w", encoding='utf-8') as f:
        json.dump(dict1, f, indent=4, ensure_ascii=False)


def get_all_sidr():
    """works correctly| Sidr"""
    dict1 = {}
    response = s.get(url=url_sidr, headers=headers)
    for page in range(1, 7):
        response = s.get(url=f"https://beerkontora.ru/sidr/page-{page}/", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        x = soup.find(class_="grid-list")
        container = x.find_all("div", class_="ty-column5")

        for i in container:
            try:
                sidr_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                sidr_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                sidr_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
                dict1[title] = {'sidr_hrefs':sidr_hrefs, 'sidr_image':sidr_image, 'sidr_price':sidr_price}
            except:
                pass

    with open("data/sidr.json", "w", encoding='utf-8') as f:
        json.dump(dict1, f, indent=4, ensure_ascii=False)


def get_all_water():
    """works correctly| Watter"""
    dict1 = {}
    response = s.get(url=url_water, headers=headers)
    for page in range(1, 8):
        response = s.get(url=f"https://beerkontora.ru/water/page-{page}/", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find_all("div", class_="ty-column5")
        for i in container:
            try:
                water_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                water_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                water_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
                dict1[title] = {'water_hrefs':water_hrefs, 'water_image':water_image, 'water_price':water_price}
            except:
                pass

    with open("data/water.json", "w", encoding='utf-8') as f:
        json.dump(dict1, f, indent=4, ensure_ascii=False)


def get_all_napitki():
    """works correctly| Naptiki"""
    dict1 = {}
    response = s.get(url=url_napitki, headers=headers)
    for page in range(1, 6):
        response = s.get(url=f"https://beerkontora.ru/napitki/page-{page}/", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        x = soup.find(class_="grid-list")
        container = x.find_all("div", class_="ty-column5")

        for i in container:
            try:
                napitki_hrefs = i.find("a", class_="product-title").get("href")
                title = i.find("a", class_="product-title").text
                napitki_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
                napitki_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
                dict1[title] = {'napitki_hrefs':napitki_hrefs, 'napitki_image':napitki_image, 'napitki_price':napitki_price}
            except:
                pass

    with open("data/napitki.json", "w", encoding='utf-8') as f:
        json.dump(dict1, f, indent=4, ensure_ascii=False)


def get_all_coffee():
    """works correctly| Coffee"""
    dict1 = {}
    response = s.get(url=f"https://beerkontora.ru/kofe/page-0/", headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    x = soup.find(class_="grid-list")
    container = x.find_all("div", class_="ty-column5")
    for i in container:
        try:
            coffee_hrefs = i.find("a", class_="product-title").get("href")
            title = i.find("a", class_="product-title").text
            coffee_image = i.find_all("img", class_="ty-pict cm-image")[0].get("src")
            coffee_price = i.find("span", class_="ty-price-num").text.strip().replace(u"\xa0", "")
            dict1[title] = {'coffee_hrefs':coffee_hrefs,'coffee_image':coffee_image,'coffee_price':coffee_price}
        except:
            pass
    with open("data/coffee.json", "w", encoding='utf-8') as f:
        json.dump(dict1, f, indent=4, ensure_ascii=False)


def main():
    get_all_beer()
    get_all_shocolateie()
    get_all_sidr()
    get_all_water()
    get_all_napitki()
    get_all_coffee()

if __name__ == "__main__":
    main()