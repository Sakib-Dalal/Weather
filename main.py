#!/usr/bin/env python3

# imported modules
import smtplib   # email
from datetime import datetime # date 
import os # os
from prettytable import PrettyTable # for formating the data
from prettytable import MARKDOWN
import requests # http requests for api's

# custom modules
from sheety import Sheety
from weather_data import GetData 

SENDER_EMAIL = "sakibdalal73@gmail.com"
SENDER_PASSWORD = "dzywnwnzhutsgcge"
SET_TIME = "090000"

email_list = []

# Send email weather
def sendmail(email, message, raining):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

        # Quote Generator
        URL = "https://zenquotes.io/api/random"
        quote = requests.get(url=URL).json()[0]['q']

        # Send Email
        if raining == True:
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email, msg=f"Subject:Weather:\n\n\tQuote: {quote}\n\n{message}\n\nThere will be rain today bring your umbrella.")
        else:
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email, msg=f"Subject:Weather:\n\n\tQuote: {quote}\n\n{message}")

# select email from sheety data
def select_mail():
    sheety_data = Sheety()
    global email_list
    email_list = sheety_data.get_sheet_data()

weather_data = GetData()

while True:
    time = datetime.now().strftime("%H%M%S")
    now = datetime.now()

    # Reboot if time = 12
    if now.hour == 12 and now.minute == 15:
        os.system("sudo reboot")

    # send email
    if time == SET_TIME:
        data = weather_data.get_weather_data()

        # rain alert
        will_rain = False
        for i in range(0, 4):
            id = data["list"][i]['weather'][0]['id']
            if int(id) < 700:
                will_rain = True
        
        # table 
        table = PrettyTable(padding_width=15)
        table.set_style(MARKDOWN)
        table.field_names = ["Date-Time    ", "           Weather  ", "          Wind Speed", "     Temperature  ", "    Pressure  ", "    Humidity  "] 
        for i in range(0, 4):
            table.add_rows(
                [
                    [data["list"][i]['dt_txt'], data["list"][i]['weather'][0]['description'], f"{data['list'][i]['wind']['speed']} Km", f"{round(float(data['list'][i]['main']['temp_max'])-273.15, 2)} C", data["list"][i]['main']['pressure'], data["list"][i]['main']['humidity']]
                ]
            )

        # print table
        table.align = "c"
        table.border = False
        table.preserve_internal_border = False
        print(table)

        # Send mail
        select_mail()
        for email in email_list:
            sendmail(email=email, message=table, raining=will_rain)
            print(f"Email send to {email}.")
        print(email_list)

