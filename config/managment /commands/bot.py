from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot, types
import requests
import telebot
import requests
from bs4 import BeautifulSoup
import os
import telebot
from telebot import types
from decouple import config
import datetime

# def scrape_page(url):
#     response = requests.get(url)
#     htmltext = response.text
#     soup = BeautifulSoup(htmltext, 'lxml')
#
#     news_items = soup.find_all('section', class_='news-item')
#
#     news_list = []
#
#     for item in news_items:
#         news_title = item.find('div', class_='title').text.strip()
#         img = item.find('img').get('src') if item.find('img') is not None else 'None'
#         date_time = item.find('span', class_='date').text.strip()
#         news_url = 'https://www.intermedia.ru' + item.find('a')['href']
#
#         news_list.append({'title': news_title, 'image': img, 'date': date_time, 'url': news_url})
#
#     return news_list
#
# def get_last_10_music_tracks():
#     music_directory = os.path.join(settings.MEDIA_ROOT, 'music_tracks')
#     music_files = [f for f in os.listdir(music_directory) if os.path.isfile(os.path.join(music_directory, f))]
#     music_files.sort(key=lambda x: os.path.getmtime(os.path.join(music_directory, x)), reverse=True)
#     last_10_tracks = music_files[:10]
#     return last_10_tracks



# bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)
#
# class Command(BaseCommand):
#     help = 'Implemented to Django application telegram bot setup command'
#
#     def handle(self, *args, **kwargs):
#         bot.enable_save_next_step_handlers(delay=2)
#         bot.load_next_step_handlers()
#         bot.infinity_polling()
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     message1 = bot.send_message(message.chat.id, 'Выбери нужный пункт', reply_markup=keyboard)
#
# keyboard = types.ReplyKeyboardMarkup()
# button1 = types.KeyboardButton('/news')
# button2 = types.KeyboardButton('music')
# keyboard.add(button1, button2)




















# import telebot
# from telebot import types
# from decouple import config
# import datetime
#
#
# TOKEN = config('BOT_TOKEN')
# bot = telebot.TeleBot(TOKEN)
#
# admin_ids = config('admin_ids').split()
#
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# bt1 = types.KeyboardButton('Малый Noir')
# bt2 = types.KeyboardButton('Малый Chinoieserie')
# bt3 = types.KeyboardButton('Средний Lost')
# bt4 = types.KeyboardButton('Большой Alien')
# markup.add(bt1, bt2, bt3, bt4)
#
# y_n_markup = types.ReplyKeyboardMarkup(row_width=2)
# ye = types.KeyboardButton('Да')
# no = types.KeyboardButton('Нет')
# y_n_markup.add(ye, no)
#
# admin_btns = types.ReplyKeyboardMarkup()
# butt1 = types.KeyboardButton('Подсчет стоимости')
# butt2 = types.KeyboardButton('Статусы комнат')
# butt3 = types.KeyboardButton('Выход')
# for i in [butt1, butt2, butt3]:
#     admin_btns.add(i)
#
# room_choice = types.ReplyKeyboardMarkup(row_width=2)
# btn1 = types.KeyboardButton('Контакты')
# btn2 = types.KeyboardButton('Атмосфера')
# btn3 = types.KeyboardButton('Выход')
# room_choice.add(btn1, btn2, btn3)
#
# nu_mark = types.ReplyKeyboardMarkup(row_width=2)
# nu = types.KeyboardButton('Ну')
# nu_mark.add(nu, no)
#
# fl_nums = [
#     1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8.0,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,9.0,9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9,10.0,10.1,10.2,10.3,10.4,10.5,10.6,10.7,10.8,10.9,11.0,11.1,11.2,11.3,11.4,11.5,11.6,11.7,11.8,11.9,12.0,
# ]
#
# room_status = {
#     'Малый Noir': {
#         'status': 'свободен',
#         'msg': 'Малый зал Noir (Оптимально 2-4 чел)\n\n-350 будний день, с 14:00-18:00\n-450 будний день, после 18:00\n-450 пятница-воскресенье, с 14:00-18:00\n-550 пятница-воскресенье, после 18:00\n\n*Цена указана за аренду зала на 1 час',
#         'images': [
#             'https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15/327101663_600078011947061_1239666833570504694_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ffru2-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=DqjMooVNTlgAX8n_H5D&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=MzAyMzMyODU5MjI0NzU0OTEwMA%3D%3D.2-ccb7-5&oh=00_AfB2DBjA_jmJJ4__R9PFBSpJltss-N6qLe9y4dIPp5YD1g&oe=647EDDC9&_nc_sid=640168'
#         ],
#     },
#     'Малый Chinoieserie': {
#         'status': 'свободен',
#         'msg': 'Малый зал Chinoieserie (Оптимально 2-4 чел)\n\n-350 будний день, с 14:00-18:00\n-450 будний день, после 18:00\n-450 пятница-воскресенье, с 14:00-18:00\n-550 пятница-воскресенье, после 18:00\n\n*Цена указана за аренду зала на 1 час',
#         'images': [
#             'https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15/210573356_851094468847396_241235410120476500_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.ffru2-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=_B9TpCAYtLcAX-B7gXB&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MjYxMTc4MjU0ODU1NDkwMzczMQ%3D%3D.2-ccb7-5&oh=00_AfD3MzE9ljEiVUgngSrBtff_o5QSGPAbzlJm0A5OcruJRA&oe=647F060C&_nc_sid=a1ad6c 1080w,https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15'
#         ],
#     },
#     'Средний Lost': {
#         'status': 'свободен',
#         'msg': 'Средний зал Lost (Оптимально до 7 человек)\n\n-450 будний день, с 14:00-18:00\n-550 будний день, после 18:00\n-600 пятница-воскресенье, с 14:00-18:00\n-650 пятница-воскресенье, после 18:00\n\n*Цена указана за аренду зала на 1 час',
#         'images': [
#             'https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15/165388613_469666667571175_3421612594208343017_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.ffru2-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=bDBqw5OQkGkAX8ABR9n&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MjUzOTk3Mjg0MzIwMDU4Njk0Ng%3D%3D.2-ccb7-5&oh=00_AfD_tFzcODsg1ZIzw0Q6wJTN7tq9auDsXN7l3a7A0exQPw&oe=647FB234&_nc_sid=a1ad6c'
#         ],
#     },
#     'Большой Alien': {
#         'status': 'свободен',
#         'msg': 'Большой зал Alien (Оптимально до 12 человек)\n\n-800 будний день, с 14:00-18:00\n-900 будний день, после 18:00\n-950 пятница-воскресенье, с 14:00-18:00\n-1050 пятница-воскресенье, после 18:00\n\n*Цена указана за аренду зала на 1 час',
#         'images': [
#             "https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15/275970060_4939132019501582_2613564906365875572_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.ffru2-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=yG0zdC5IXEMAX_A8sPQ&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=Mjc5Mzg3NTMxODExNzY0MDgxMw%3D%3D.2-ccb7-5&oh=00_AfCzWYlLzEjTB65YUVVe4uZgoYikFN0B8LJnmS9RLqe_vQ&oe=647E3A5D&_nc_sid=640168"
#         ],
#     },
# }
#
#
# @bot.message_handler(commands=['start'])
# def starting_screen(message):
#     for v in room_status.values():
#         try:
#             if datetime.datetime.strptime(v['status'][-5:], '%H:%M').time() <= datetime.datetime.now().time():
#                 v['status'] = 'свободен'
#         except:
#             pass
#     if str(message.from_user.id) in admin_ids:
#         bot.send_message(
#             message.chat.id,
#             'Здарова Админ!\nВыбери нужную тебе опцию',
#             reply_markup=admin_btns,
#         )
#     else:
#         bot.send_message(
#             message.chat.id,
#             'Добро пожаловать в Антикинотеатр TwinPeaks\n Выберите подходящий Вам зал',
#             reply_markup=markup,
#         )
#
#
# @bot.message_handler(
#     func=lambda x: x.text
#     in ['Малый Noir', 'Малый Chinoieserie', 'Средний Lost', 'Большой Alien']
# )
# def room_info(message):
#     global room, room1
#     if str(message.from_user.id) in admin_ids:
#         if message.text == 'Малый Noir':
#             room1 = 'Малый Noir'
#             bot.send_message(
#                 message.chat.id,
#                 'Во сколько начнется?\nНаписать вот так "17:56"',
#                 reply_markup=types.ReplyKeyboardRemove(),
#             )
#         elif message.text == 'Малый Chinoieserie':
#             room1 = 'Малый Chinoieserie'
#             bot.send_message(
#                 message.chat.id,
#                 'Во сколько начнется?\nНаписать вот так "17:56"',
#                 reply_markup=types.ReplyKeyboardRemove(),
#             )
#         elif message.text == 'Средний Lost':
#             room1 = 'Средний Lost'
#             bot.send_message(
#                 message.chat.id,
#                 'Во сколько начнется?\nНаписать вот так "17:56"',
#                 reply_markup=types.ReplyKeyboardRemove(),
#             )
#         elif message.text == 'Большой Alien':
#             room1 = 'Большой Alien'
#             bot.send_message(
#                 message.chat.id,
#                 'Во сколько начнется?\nНаписать вот так "17:56"',
#                 reply_markup=types.ReplyKeyboardRemove(),
#             )
#     else:
#         if message.text == 'Малый Noir':
#             room = 'Малый Noir'
#             bot.send_message(
#                 message.chat.id,
#                 f'{room_status["Малый Noir"]["msg"]}\n\nВ данный момент {room_status["Малый Noir"]["status"].upper()}',
#                 reply_markup=room_choice,
#             )
#         elif message.text == 'Малый Chinoieserie':
#             room = 'Малый Chinoieserie'
#             bot.send_message(
#                 message.chat.id,
#                 f'{room_status["Малый Chinoieserie"]["msg"]}\n\nВ данный момент {room_status["Малый Chinoieserie"]["status"].upper()}',
#                 reply_markup=room_choice,
#             )
#         elif message.text == 'Средний Lost':
#             room = 'Средний Lost'
#             bot.send_message(
#                 message.chat.id,
#                 f'{room_status["Средний Lost"]["msg"]}\n\nВ данный момент {room_status["Средний Lost"]["status"].upper()}',
#                 reply_markup=room_choice,
#             )
#         elif message.text == 'Большой Alien':
#             room = 'Большой Alien'
#             bot.send_message(
#                 message.chat.id,
#                 f'{room_status["Большой Alien"]["msg"]}\n\nВ данный момент {room_status["Большой Alien"]["status"].upper()}',
#                 reply_markup=room_choice,
#             )
#
#
# @bot.message_handler(
#     func=lambda x: x.text.lower() in ['контакты', 'атмосфера', 'выход']
# )
# def contacts_photo(message):
#     if message.text.lower() == 'контакты':
#         bot.send_message(
#             message.chat.id,
#             'Контакты:\n🏡: проспект Манаса 30/Токтогула (позади остановки)\n☎️: +996 999 505 303',
#         )
#     elif message.text.lower() == 'атмосфера':
#         for i in range(len(room_status[room]['images'])):
#             bot.send_photo(message.chat.id, room_status[room]['images'][i])
#     elif message.text.lower() == 'выход':
#         bot.send_message(
#             message.chat.id,
#             'Пока\nЧтобы запустить обратно --> /start',
#             reply_markup=types.ReplyKeyboardRemove(),
#         )
#
#
# @bot.message_handler(
#     func=lambda x: x.text.lower() in ['подсчет стоимости', 'статусы комнат']
# )
# def cost_status(message):
#     global room1
#     if str(message.from_user.id) in admin_ids:
#         if message.text.lower() == 'подсчет стоимости':
#             bot.send_message(
#                 message.chat.id, 'Какой зал интересует ?', reply_markup=markup
#             )
#         elif message.text.lower() == 'статусы комнат':
#             bot.send_message(
#                 message.chat.id,
#                 f'Малый Noir - {room_status["Малый Noir"]["status"].upper()}\nМалый Chinoieserie - {room_status["Малый Chinoieserie"]["status"].upper()}\nСредний Lost - {room_status["Средний Lost"]["status"].upper()}\nБольшой Alien - {room_status["Большой Alien"]["status"].upper()}',
#             )
#
#
# @bot.message_handler(func=lambda x: ':' in x.text and len(x.text) == 5)
# def set_start(message):
#     global rent_start
#     rent_start = datetime.datetime.strptime(message.text, '%H:%M')
#     if (
#         rent_start.time() > datetime.datetime.strptime('13:59', '%H:%M').time()
#         or rent_start.time() < datetime.datetime.strptime('03:00', '%H:%M').time()
#     ):
#         bot.send_message(
#             message.chat.id,
#             'На сколько часов аренда зала?(Например 2.5)',
#             reply_markup=types.ReplyKeyboardRemove(),
#         )
#     else:
#         bot.send_message(
#             message.chat.id, 'Мы не работаем в это время, наш график 14:00-03:00'
#         )
#
# @bot.message_handler(func=lambda x: x.text.replace('.', '').isdigit())
# def cost_calc(message):
#     global rent_close
#     if str(message.from_user.id) in admin_ids:
#         if float(message.text) in fl_nums:
#             rent_close = rent_start + datetime.timedelta(hours=float(message.text))
#             if room1 == 'Малый Noir' or room1 == 'Малый Chinoieserie':
#                 cost = 0
#                 dt_copy = rent_start
#                 while dt_copy.time() < rent_close.time():
#                     if (
#                         dt_copy.time()
#                         < datetime.datetime.strptime('18:00', '%H:%M').time()
#                     ):
#                         cost += (
#                             5.83
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 7.5
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#                     elif dt_copy.time() < rent_close.time():
#                         cost += (
#                             7.5
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 9.16
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#             elif room1 == 'Средний Lost':
#                 cost = 0
#                 dt_copy = rent_start
#                 while dt_copy.time() < rent_close.time():
#                     if (
#                         dt_copy.time()
#                         < datetime.datetime.strptime('18:00', '%H:%M').time()
#                     ):
#                         cost += (
#                             10
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 12.5
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#                     elif dt_copy.time() < rent_close.time():
#                         cost += (
#                             11.66
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 14.16
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#             elif room1 == 'Большой Alien':
#                 cost = 0
#                 dt_copy = rent_start
#                 while dt_copy.time() < rent_close.time():
#                     if (
#                         dt_copy.time()
#                         < datetime.datetime.strptime('18:00', '%H:%M').time()
#                     ):
#                         cost += (
#                             13.33
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 15.83
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#                     elif dt_copy.time() < rent_close.time():
#                         cost += (
#                             15
#                             if datetime.datetime.now().weekday() in range(4)
#                             else 17.5
#                         )
#                         dt_copy += datetime.timedelta(minutes=1)
#             bot.send_message(
#                 message.chat.id,
#                 f'Сеанс начнется в {rent_start.time().strftime("%H:%M")}, закончится в {rent_close.time().strftime("%H:%M")}\nОбщая стоимость на сегодня - {round(cost,2)}\nВписать?',
#                 reply_markup=y_n_markup,
#             )
#         elif float(message.text) == 0:
#             bot.send_message(
#                 message.chat.id, 'Точно освободить зал?', reply_markup=nu_mark
#             )
#         else:
#             bot.send_message(
#                 message.chat.id,
#                 'Напишите правильное кол-во часов для подсчета',
#             )
#
#
# @bot.message_handler(func=lambda x: x.text.lower() in ['да', 'нет', 'ну'])
# def status_change(message):
#     if str(message.from_user.id) in admin_ids:
#         if message.text.lower() == 'да':
#             room_status[room1]['status'] = f'Занят до {rent_close.time().strftime("%H:%M")}'
#             bot.send_message(message.chat.id, 'Записал!', reply_markup=admin_btns)
#         elif message.text.lower() == 'нет':
#             bot.send_message(message.chat.id, 'Окей', reply_markup=admin_btns)
#         elif message.text.lower() == 'ну':
#             room_status[room1]['status'] = 'свободен'
#             bot.send_message(message.chat.id, 'Освободил', reply_markup=admin_btns)
#
#
# @bot.message_handler(commands=['add'])
# def start_message(message):
#     with (open('file.txt', 'a') as f2, open('file.txt', ) as f1):
#         content = f1.read().replace('\n', ' ').split()
#         user_info = str(message.from_user.id)+' '+ message.from_user.first_name
#         if not (str(message.from_user.id) in content):
#             f2.write(user_info+'\n')
#
# bot.polling()