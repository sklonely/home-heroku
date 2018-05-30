import os
from flask import Flask, abort, request
import AI
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (ImageSendMessage, MessageEvent, TextMessage,
                            TextSendMessage)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'SCxxKg4cVbfVJn/ZU1E/Hor5wlyakdnjCBo7uHK1P7wqMB+VNMUmcbipYTw2yrRrZZzxUNfAOBmHN/rGjXFGUfaGjAk96l/VVzkzGif6jIxNgL04G93aRK9n/E8gjLMplwzP7Y8gielrXBMUqT55VAdB04t89/1O/w1cDnyilFU='
)
# Channel Secret
handler = WebhookHandler('a61a3af3affa9274c388bf7fe3b07058')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@app.route("/getup", methods=['GET'])
def getup():
    print("google get up heroku")
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    AI_answer = AI.AI_answer(event.message.text)
    message = TextSendMessage(text=AI_answer)
    print("使用者說: ", event.message.text, "\nAI回: ", AI_answer)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
