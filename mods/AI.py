# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import googlesheet
        import apiUse
        from Naked.toolshed.shell import execute_js, muterun_js
        from googlesheet import GoogleSheet

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
sheet = GoogleSheet("database", "電器狀態")
sheet2 = GoogleSheet("database", "匯率")


def AI_answer(myMsg):
    myResult = ""
    print(myMsg)
    if (myMsg == "你好" or myMsg == "早安" or myMsg == "午安" or myMsg == "晚安"):
        myResult = myMsg

    elif (myMsg == "使用方法" or myMsg == "?" or myMsg == "？"):
        myResult = "------指令清單------\n 1.熱水器 開\n 2.熱水器 關\n 3.熱水器 狀態\n 4.開發者"

    elif (myMsg == "天氣"):
        myResult = ""
        a = apiUse.Weather().get_all()
        for i in range(len(a)):
            if (i % 2):
                myResult = myResult + (a[i - 1] + a[i] + "\n")

    elif (myMsg == "匯率"):
        myResult = ""
        data = sheet2.row_values(2)
        tittle = sheet2.row_values(1)
        for i in range(len(data)):
            myResult = myResult + (tittle[i] + ": " + data[i] + "\n")
        print(myResult)

    elif (myMsg == "Aon" or myMsg == "A on" or myMsg == "熱水器 開" or myMsg == "熱水器開"):
        myResult = "已開啟熱水器"
        sheet.update(1, 2, 1)
        response = muterun_js('webduino_on.js')
        if response.exitcode == 0:
            print(response.stdout)

    elif (myMsg == "Aoff" or myMsg == "A off" or myMsg == "熱水器 關" or myMsg == "熱水器關"):
        myResult = "已關閉熱水器"
        sheet.update(1, 2, 0)
        response = muterun_js('webduino_off.js')
        if response.exitcode == 0:
            print(response.stdout)

    elif (myMsg == "熱水器" or myMsg == "A？" or myMsg == "熱水器 狀態" or myMsg == "熱水器狀態"):
        if (sheet.cell(1, 2) == "1"):
            myResult = "熱水器現在: 開啟"
        else:
            myResult = "熱水器現在: 關閉"

    elif (myMsg == "熱水器 腳位" or myMsg == "熱水器腳位"):
        myResult = "13"

    elif (myMsg == "開發者"):
        myResult = "我的創造者是sklonley"

    else:
        myResult = "抱歉，不太理解 " + str(myMsg) + " 這句話的意思!"

    return myResult


""""
print(AI_answer("熱水器 開"))
print(AI_answer("熱水器 狀態"))
print(AI_answer("熱水器 關"))
print(AI_answer("熱水器 狀態"))
print(AItest)
"""
