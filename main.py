#!/usr/bin/env python3

# imported modules
import smtplib
from weather_data import GetData
from datetime import datetime
import os

# custom modules
from sheety import Sheety

SENDER_EMAIL = "sakibdalal73@gmail.com"
SENDER_PASSWORD = "dzywnwnzhutsgcge"
SET_TIME = "090000"
T_TIME = "145000"

email_list = []

# Send email weather
def sendmail(email, message, raining):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

        # Send Email
        if raining == True:
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email, msg=f"Subject:Weather:\n\nHello todays there will be {message}.\nThere will be rain today bring your 🌂")
        else:
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email, msg=f"Subject:Weather:\n\nHello todays there will be {message}.")

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
    if time == T_TIME:
        data = weather_data.get_weather_data()

        # rain alert
        will_rain = False
        for i in range(0, 4):
            id = data["list"][i]['weather'][0]['id']
            if int(id) < 700:
                will_rain = True
                print(f"Rain today id {id} {will_rain}")
            else:
                print(f"No Rain today id {id} {will_rain}")
        

        send_msg = str(data["list"][0]['weather'][0]['description'])
        select_mail()
        for email in email_list:
            sendmail(email=email, message=send_msg, raining=will_rain)
            print(f"Email send to {email}.")
        print(email_list)

