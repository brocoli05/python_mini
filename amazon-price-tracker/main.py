from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.com/Logitech-Vertical-Wireless-Mouse-Rechargeable/dp/B07FNJB8TT/ref=sr_1_4?crid=3LB7GN815YPXT&dib=eyJ2IjoiMSJ9.s0wugfTUby_FFI2WmBjczGsuGeRdypnJFy9XMGDwtJezAgGq1_3STFSwXWseG3d3psTxoVCbOy8rsea6T4wTp1u8McqlFnyGCjnnp8_FWEc0TBKuIAfA_f5IJXh3WzI-jFaVSNGAaQdtoyYahX7p4M-6hHFTYnw-WgqhP5jUAvb-Wybshtl6VEYvdiHRjUncQZ9sboQ2AOwEJA2B3GeM1RA4WkrPxyUrSZFTLKNskuQ.5GaPolKC_LAD-eKZP2-SnIZ4EkNuvxPIm-PHne3eVBM&dib_tag=se&keywords=vertical+mouse&qid=1717533051&sprefix=verti%2Caps%2C153&sr=8-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en,ko-KR;q=0.9,ko;q=0.8,en-US;q=0.7"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price_as_whole = soup.find(name="span", class_="a-price-whole").getText()
price = price_as_whole.split(".")[0]
price_as_flot = soup.find(class_="a-price-fraction").get_text()
print(price)
print(price_as_flot)