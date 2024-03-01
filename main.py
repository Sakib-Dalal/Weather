import smtplib
from weather_data import GetData
from datetime import datetime

SENDER_EMAIL = "sakibdalal73@gmail.com"
SENDER_PASSWORD = "dzywnwnzhutsgcge"
SET_TIME = "224400"

email_list = []


def sendmail(email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

        # Send Email
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email, msg=f"Subject:Weather:\n\n{message}")


def select_mail():
    with open("./email.txt", "r") as email_file:
        email = email_file.readlines()
        email = [line.strip() for line in email]
        print(email)
        email_list.append(email)


weather_data = GetData()

while True:
    time = datetime.now().strftime("%H%M%S")
    if time == SET_TIME:
        data = weather_data.get_weather_data()
        send_msg = str(data["list"][0]['weather'][0]['description'])
        select_mail()
        for email in email_list:
            sendmail(email=email, message=send_msg)
            print("Email Send")
        print(email_list)
