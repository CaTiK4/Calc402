import telepot as telepot
from telepot.loop import MessageLoop

TOKEN = 'свой токен я не дам!'
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Ответ: Бака, пиши по человечески!\nА то я тебя не понимаю\nНачни вводить выражение вида '2+3 или 1*3'"
    bot.sendMessage(chat_id, "Ответ: {}".format(answer))

MessageLoop(bot, handle).run_as_thread()

# Пока не введёшь stop, код будет работать
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break