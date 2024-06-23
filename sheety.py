import requests

SHEETY_USER_NAME = "Sheety app Key"
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
    
    def post_sheet_data(self, email):
        sheet_input = {
            "sheet1":{
                "email": email
            }
        }
        self.response = requests.post(url=SHEETY_END_POINT, json=sheet_input)
        print(self.response.text)

    def delete_sheet_data(self, email):
        self.response = requests.delete(url=f"{SHEETY_END_POINT}/{email}")
        print(self.response.text)

if __name__ == "__main__":
    data = Sheety()
    print(data.get_sheet_data())
    print(type(data.get_sheet_data()))

