import requests
class City:
    def __init__(self, name_city, latitude, longtitude, unit, token):
        self.name_city = name_city
        self.latitude = latitude
        self.longtitude = longtitude
        self.units = unit
        self.token = token
        self.get_data()
        self.give_info()

    def get_data(self):
        try:
            results = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.latitude}&lon={self.longtitude}&appid={self.token}")

        except:
             print("Error Loading Data from Url")
        response = results.json()
        self.temp = response['main']['temp']
        self.temp_min = response['main']['temp_min']
        self.temp_max = response['main']['temp_max']


    def give_info(self):
        print(f"Current Temperature in Accra is Between: {self.temp_min}° and {self.temp_max}° degree Celcius")

def main():
    name = input('Enter your city name: ')
    
    try:
        latitude = float(input('Enter your latitude (e.g., 5.5600): '))
        longitude = float(input('Enter your longitude (e.g., -0.2050): '))
    except ValueError:
        print("[ERROR] Latitude and Longitude must be numbers.")
        return

    units = input("Enter unit (metric for °C, imperial for °F) [default: metric]: ") or "metric"
    token = input('Enter your OpenWeather API token: ')

    city = City(name, latitude, longitude, units, token)
    
    if city.get_data():
        city.give_info()

if __name__ == "__main__":
    main()




