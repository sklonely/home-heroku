import json
import requests


class Weather():

    def __init__(self):
        weatherJsonUrl = "https://works.ioa.tw/weather/api/weathers/2.json"
        response = requests.get(weatherJsonUrl)
        response.raise_for_status()
        weatherData = json.loads(response.text)
        # print("天氣預報時間: ", weatherData["at"])  # 漂亮打印出天气字典
        # print("簡短描述: ", weatherData["desc"])
        # print("體感溫度: ", str(weatherData["felt_air_temp"]) + " 度")
        # print("濕度: ", str(weatherData["humidity"]) + " %")
        # print("實際溫度: ", str(weatherData["temperature"]) + " 度")

        self.weatherList = ["天氣預報時間: ", weatherData["at"], "簡短描述: ", weatherData["desc"], "體感溫度: ", str(weatherData["felt_air_temp"]) + " 度", "濕度: ", str(weatherData["humidity"]) + " %", "實際溫度: ", str(weatherData["temperature"]) + " 度"]
        # print(self.weatherList)

    def get_all(self):
        return self.weatherList


a = Weather().get_all()
b=""

print(b)
