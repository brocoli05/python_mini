"""
Send a motivational quote via email on the current weekday
"""
import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

# load the environment variables
load_dotenv("./.env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:  # Sunday
   with open("quotes.txt") as file:
      quote = random.choice(file.readlines())
      print(quote.strip())

   with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connetion:
      # connetion.starttls()
      connetion.login(user=MY_EMAIL, password=MY_PASSWORD)
      connetion.sendmail(
         from_addr=MY_EMAIL, 
         to_addrs=MY_EMAIL, 
         msg=f"Subject:Sunday Motivation\n\n{quote}"
      )


# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)