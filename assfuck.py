#!/usr/bin/env python3

enable_token_check = False

def readff(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None

print("""

                   ______          _    
     /\           |  ____|        | |   
    /  \   ___ ___| |__ _   _  ___| | __
   / /\ \ / __/ __|  __| | | |/ __| |/ /
  / ____ \\__ \__ \ |  | |_| | (__|   < 
 /_/    \_\___/___/_|   \__,_|\___|_|\_\
                                        
  Catware AssFuck (ебать дениса носкова)
""")
print(">>> Импортирую time...")
import time
print(">>> Импортирую vk_api...")
import vk_api
print(">>> Импортирую VkLongPoll, VkEventType...")
from vk_api.longpoll import VkLongPoll, VkEventType
print(">>> Чтение файла token.txt...")
token = readff("token.txt")
if enable_token_check:
    if len(token) != 85:
        print("!!! Токен не найден. Создайте файл token.txt и запишите туда токен от своей страницы.")
        time.sleep(10)
        exit()
print(">>> Авторизация в ВКонтакте...")
vk_session = vk_api.VkApi(token=token)
print(">>> Обозначение VkUpload... ")
vk_upload = vk_api.upload.VkUpload(vk_session)
print(">>> Обозначение VkLongPoll...")
longpoll = VkLongPoll(vk_session)
print(">>> Получение доступа к API...")
try:
    vk = vk_session.get_api()
    print("[V] Доступ успешен")
except Exception as e:
    print("[X] Нельзя получить доступ: " + str(e))
    exit()
chatid = input("Введите ID чата, в котором находится ЭТОТ ВЫБЛЯДОК ЕБАНЫЙ БЛЯТЬ ~> ")
uid = input("Введите ID ублюдка (цифры) которого надо ПОИМЕТЬ ~> ")
print(">>> Начинаю чтение...")
while True:
    try:
        #for event in longpoll.listen():
        #    print("[i] Получен обьект события")
        #    print("Определение параметров...")
        #    #print(event)
        #    try:
        #        user_id = event.user_id
        #        peer_id = event.peer_id
        #        chat_id = event.chat_id
        #        text = event.text
        #        print(f"""
# Обнаруженные параметры:
# - ID пользователя = {str(user_id)}
# - Peer ID = {str(peer_id)}
# - ID чата = {str(chat_id)}
# - Текст сообщения = {text}
#""")
        #    except Exception as e:
        #        print(str(e))
        vk.messages.removeChatUser(chat_id=chatid, member_id=uid)
    except Exception as e:
        #print("[!] Сообщение получено не из беседы или имеет ошибку, оно не будет обработано")
        print("Exception: " + str(e))

