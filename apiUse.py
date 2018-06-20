import json
import requests


class Weather():

    def __init__(self):
        weatherJsonUrl = "https://works.ioa.tw/weather/api/weathers/2.json"
        response = requests.get(weatherJsonUrl)
        response.raise_for_status()
        weatherData = json.loads(response.text)
        import pprint  # 导入pprint模块
        pprint.pprint(weatherData)  # 漂亮打印出天气字典


a = Weather()
