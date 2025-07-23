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
            results = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.latitude}&lon={self.longtitude}&appid=77faabcc09b1d617fb78f0462bb2ead8")

        except:
             print("Error Loading Data from Url")
        response = results.json()
        self.temp = response['main']['temp']
        self.temp_min = response['main']['temp_min']
        self.temp_max = response['main']['temp_max']


    def give_info(self):
        print(f"Current Temperature in Accra is Between: {self.temp_min}° and {self.temp_max}° degree Celcius")


name_city = input('Please, Enter Your City \n')
latitude = input('Enter Your Latitude \n')
longtitude = input('Enter your Longtitude \n')
unit = input('Please, Enter Your Unit \n')
token = input('Please, Enter Your Token \n')
my_city = City(name_city, latitude, longtitude,unit, token)
my_city.give_info()
        




