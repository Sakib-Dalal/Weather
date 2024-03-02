import requests

SHEETY_USER_NAME = "822d50c0ba48a0d28feb2305a5a52d6c"
SHEETY_PROJECT_NAME = "weather"
SHEETY_NAME = "sheet1"

SHEETY_END_POINT = f"https://api.sheety.co/{SHEETY_USER_NAME}/{SHEETY_PROJECT_NAME}/{SHEETY_NAME}"

class Sheety:
    def __init__(self) -> None:
        pass
    
    def get_sheet_data(self):
        self.response = requests.get(url=SHEETY_END_POINT)
        data = self.response.json()
        self.email_data = []
        for email in data['sheet1']:
            self.email_data.append(email['email'])
        return self.email_data

if __name__ == "__main__":
    data = Sheety()
    print(data.get_sheet_data())
    print(type(data.get_sheet_data()))

