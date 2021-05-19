import requests

class Weather:
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def good_response_code(self, res):
        if res.status_code >= 200 and res.status_code < 300:
            return True

    def get_city_weather(self, city_name, lang, units):
        query = {
            "q": city_name,
            "appid": self.token,
            "lang": lang,#"ru",
            "units": units#"metric"
        }
        response = requests.get(self.url, params=query)

        if not self.good_response_code(response):
            return "Случилась ошибка, повторите попытку еще раз"

        res = response.json()

        description = res["weather"][0]["description"]
        temp = res["main"]["temp"]

        return_str = (f"В городе {city_name}, {description}\n" \
                      f"Температура воздуха {temp} градусов.")
        return return_str


city_name = input("Введите название города: ")
lang = input("Введите язык, на котором необходимо вывести информацию (например, ru): ")
units = input("Введите единицы измерения, в которых необходимо вывести данные (мапример, metric): ")
token = "799461e6591f3a6352bc3ef6727ecd2b"
url = "https://api.openweathermap.org/data/2.5/weather"

open_weather = Weather(token, url)
print(open_weather.get_city_weather(city_name, lang, units))





# response = requests.get(url, params=query)
# print(response.status_code)
# print(response.text)
# print(type(response.json()))
# json_response = response.json()
# # print("Температура в городе", json_response["main"]["temp"])
# print(json_response["weather"][0]["description"])
# print(json.dumps(json_response, indent=4))
#
# if response.status_code == 200:
#
#     temp = json_response["main"]["temp"]
#     description = json_response["weather"][0]["description"]
#     print(f"В городе {city}, {description}, {temp} градусов.")
# else:
#     print("Возникла ошибка")







#Наследование
class A:
    a_string = "a"

    def print_a_string(self):
        print(self.a_string)



#Инкапсуляция
class Phone:
    number = ""

    def set_number(self, new_number):
        self.number = new_number

phone1 = Phone()
new_num = "+79999931113"
phone1.number = new_num
phone1.set_number(new_num)

phone2 = Phone()
phone2.set_number("+75656464646")
print(phone1.number)
print(phone2.number)
