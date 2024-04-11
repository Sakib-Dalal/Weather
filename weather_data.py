import requests

API_KEY = "e8b2664d494ebd7d2426ffd3679c1ccf"
URL = "http://api.openweathermap.org/data/2.5/forecast"
# https://api.openweathermap.org/data/2.5/forecast?lat=16.815304&lon=74.569595&appid=e8b2664d494ebd7d2426ffd3679c1ccf&cnt=4

MY_LAT = 16.815304
MY_LNG = 74.569595

class GetData:
    def __init__(self) -> None:
        self.parameters = {
            "lat": MY_LAT,
            "lon": MY_LNG,
            "appid": API_KEY,
            "cnt": 4,
        }
    
    def get_weather_data(self):
        response = requests.get(url=URL, params=self.parameters)
        response.raise_for_status    # to raise error
        return response.json()

if __name__ == "__main__":
    pass
