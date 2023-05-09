import telebot
from telebot.types import InputFile
import keep_alive
import os

bot = telebot.TeleBot(os.environ.get("TOKEN"))
my_id = os.environ.get("my_ID")
chat_id = os.environ.get("chat_ID")


@bot.message_handler(content_types=['text'])
def all(message):
  words = message.text.split(" ")
  for i in range(len(words)):
    if words[i] == "@all":
      bot.send_message(
        chat_id,
        os.environ.get("every_chat_user_username")
      )
      break
  if words[0] == "забань":
    if message.from_user.username == os.environ.get("adm_1") or message.from_user.username == os.environ.get("adm_2"):
      try:
        bot.ban_chat_member(chat_id=chat_id, user_id=words[i + 1])
      except Exception:
        bot.send_message(message.from_user.id, "не удалось забанить")
    else:
      bot.send_message(message.from_user.id, "У тебя нет таких прав ЛОХ")
  if words[0] == "china":
    try:
      if message.from_user.username == os.environ.get("adm_1") or message.from_user.username == os.environ.get("adm_2"):
        bot.set_chat_photo(chat_id, InputFile("ava_tg.png"))
        bot.set_chat_title(chat_id, "КНР")
        for i in range(20):
          bot.send_message(chat_id, "沃爾特，把你的雞巴拿開沃爾特")
      else:
        bot.send_message(
          chat_id,
          f"ВНИМАНИЕ несанкционированная попытка превратить сервер в Китай от пользователя @{message.from_user.username}"
        )
    except Exception as ex:
      bot.send_message(chat_id, "Не удалось превратить сервер в Китай")
      print(ex)
  if message.text == "info":
    bot.send_message(
      chat_id,
      "info-команды бота\n@all - позвать всех\nchina - могут только ограниченный круг людей\nПишите если вам нужны какие-то свои команды"
    )
  if message.text == "Phoenix protocol":
    bot.send_message(chat_id, "Выполняется протокол Phoenix")
    try:
      bot.unban_chat_member(chat_id, my_id)
    except Exception as ex:
      print(ex)
  if message.text == "test":
    print("success")
    bot.send_message(my_id, "TEST SUCCES")


keep_alive.keep_alive()
bot.polling(none_stop=True, interval=0)