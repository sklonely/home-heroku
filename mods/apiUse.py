# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import json
        import requests
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName
        break


# import自動修復 程式碼片段
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

        self.weatherList = ["資料更新時間: ", weatherData["at"], "簡短描述: ", weatherData["desc"], "體感溫度: ", str(weatherData["felt_air_temp"]) + " 度", "濕度: ", str(weatherData["humidity"]) + " %", "實際溫度: ", str(weatherData["temperature"]) + " 度"]
        # print(self.weatherList)

    def get_all(self):
        return self.weatherList
