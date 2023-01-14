import bs4
import requests

# res = requests.get("https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK/")
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# elems = soup.select("#kindle-price")
# print(elems[0].text.strip())

# A simple program to retrive the price of a product on Amazon: -
def get_amazon_price(product_URL):
    res = requests.get(product_URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("#corePrice_feature_div > div > span > span:nth-child(2)")
    return elems[0].text.strip()

price = get_amazon_price("https://www.amazon.co.uk/Anker-Charger-Compact-Foldable-MacBook-Black/dp/B09C87NLDN/ref=sr_1_6?crid=22RGZSYTT10BG&keywords=anker&qid=1673471368&sprefix=anke%2Caps%2C128&sr=8-6")
print(price)
