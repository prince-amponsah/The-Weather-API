import requests
class City:
    def __init__(self, name_city, latitude, longtitude, units='metric'):
        self.name_city = name_city
        self.latitude = latitude
        self.longtitude = longtitude
        self.units = units
        self.get_data()
        self.give_info()


    def get_data(self):
        try:
            results = requests.get(f"{url with api key}")

        except:
             print("Error Loading Data from Url")
        response = results.json()
        self.temp = response['main']['temp']
        self.temp_min = response['main']['temp_min']
        self.temp_max = response['main']['temp_max']


    def give_info(self):
        print(f"Current Temperature in Accra is Between: {self.temp_min}° and {self.temp_max}° degree Celcius")

my_city = City("Accra","5.5593","0.1974")
my_city.give_info()
        




