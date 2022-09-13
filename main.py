import telebot
import config
import command_douyin

bot = telebot.TeleBot(config.bot_api)

@bot.message_handler(commands=['douyin_qu_shui_yin'])
def method(message):
    print(message.json['from']['id'])
    # 因为实现单个功能，所以获取url部分可以简单粗暴。如果是多个功能，建议写个单独的函数来分离出指令和参数。
    url = message.text.replace('/douyin_qu_shui_yin', '').replace(' ','')
    if url == '':
        error_text = '指令用得不对，正确用法是 /douyin_qu_shui_yin + 视频链接'
        bot.reply_to(message, text=error_text)
    else:
        judged_url = command_douyin.get_douyin(url)
        bot.reply_to(message, text=judged_url)


if __name__ == '__main__':
    try:
        print(">>> 机器人成功启动！")
        bot.polling(none_stop=True, timeout=1000)
    except Exception as e:
        print(f">>> 错误：{e}")
