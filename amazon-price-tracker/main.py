from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv

# load the environment variables
load_dotenv("./.env")
EMAIL = os.getenv("EMAIL")
PW = os.getenv("PASSWORD")

TARGET_PRICE = 200.0

URL = "https://www.amazon.com/Logitech-Vertical-Wireless-Mouse-Rechargeable/dp/B07FNJB8TT/ref=sr_1_4?crid=3LB7GN815YPXT&dib=eyJ2IjoiMSJ9.s0wugfTUby_FFI2WmBjczGsuGeRdypnJFy9XMGDwtJezAgGq1_3STFSwXWseG3d3psTxoVCbOy8rsea6T4wTp1u8McqlFnyGCjnnp8_FWEc0TBKuIAfA_f5IJXh3WzI-jFaVSNGAaQdtoyYahX7p4M-6hHFTYnw-WgqhP5jUAvb-Wybshtl6VEYvdiHRjUncQZ9sboQ2AOwEJA2B3GeM1RA4WkrPxyUrSZFTLKNskuQ.5GaPolKC_LAD-eKZP2-SnIZ4EkNuvxPIm-PHne3eVBM&dib_tag=se&keywords=vertical+mouse&qid=1717533051&sprefix=verti%2Caps%2C153&sr=8-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en,ko-KR;q=0.9,ko;q=0.8,en-US;q=0.7"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price_as_whole = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
price_as_fraction = soup.find(class_="a-price-fraction").getText()
price = float(f"{price_as_whole}.{price_as_fraction}")
print(price)

# send email
title = soup.find(id="productTitle").getText().strip()
print(title)

print((price < TARGET_PRICE))
if price < TARGET_PRICE:
    message = f"{title} is now {price}"

    try:
        with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as connection:
            # connection.starttls()
            result = connection.login(EMAIL, PW)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")