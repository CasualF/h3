

from django.core.management.base import BaseCommand
import telebot
from django.conf import settings
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


class Command(BaseCommand):
    help = 'Команда для запуска бота Telegram в Django'

    def handle(self, *args, **kwargs):
        bot.remove_webhook()
        bot.polling(none_stop=True, interval=0, timeout=20)


WELCOME_MESSAGE = (
    'Добро пожаловать в нашу онлайн-школу IT-профессий!\n'
    'Мы гордимся предоставлением высокоэффективных курсов, разработанных для тех, '
    'кто стремится развить свои навыки в сфере информационных технологий и достичь '
    'новых высот в своей карьере.\n\n'
    'Наша программа включает в себя следующие ключевые области:'
)

AREAS_MESSAGE = (
    'Выберите интересующую вас ключевую область:\n\n'
    '🌐 Frontend - это направление, связанное с разработкой пользовательских '
    'интерфейсов и взаимодействием с пользователем.\n\n'
    '💼 Backend - это направление, отвечающее за разработку серверной части приложений, '
    'работу с базами данных и обработку бизнес-логики.'
)

FRONTEND_SUBAREAS = (
    'Вы выбрали Frontend. Теперь выберите подраздел:\n\n'
    '🌐 JavaScript - язык программирования для создания интерактивных веб-приложений.\n\n'
    '🎨 UI/UX Дизайн - проектирование пользовательских интерфейсов и опыта взаимодействия.'
)

EXIT_MESSAGE = 'Вы покинули бота. До свидания!'

states = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('📞 Служба поддержки')
    button2 = types.KeyboardButton('🚀 Ключевые области')
    button3 = types.KeyboardButton('📰 Новости')
    button4 = types.KeyboardButton('❌ Выйти из бота')
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id, WELCOME_MESSAGE, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '📞 Служба поддержки')
def support_message(message):
    response = ('Добрый день!\n'
                'Электронная почта для связи akusevtimur733@gmail.com\n'
                '...')

    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == '🚀 Ключевые области')
def areas_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('🌐 Frontend')
    button2 = types.KeyboardButton('💼 Backend')
    button3 = types.KeyboardButton('🔙Назад')
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, AREAS_MESSAGE, reply_markup=keyboard)
    states[message.chat.id] = 'areas_message'


@bot.message_handler(func=lambda message: message.text == '🌐 Frontend')
def frontend_subareas(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('🌐 JavaScript')
    button2 = types.KeyboardButton('🎨 UI/UX Дизайн')
    button3 = types.KeyboardButton('🔙Назад')
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, FRONTEND_SUBAREAS, reply_markup=keyboard)
    states[message.chat.id] = 'frontend_subareas'


@bot.message_handler(func=lambda message: message.text == '🔙Назад')
def back(message):
    if message.chat.id in states:
        if states[message.chat.id] == 'areas_message':
            start_message(message)
        elif states[message.chat.id] == 'frontend_subareas':
            areas_message(message)
        else:
            bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")
    else:
        bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")


@bot.message_handler(func=lambda message: message.text == '❌ Выйти из бота')
def exit_bot(message):
    bot.send_message(message.chat.id, EXIT_MESSAGE)


@bot.message_handler(func=lambda message: message.text == '🎨 UI/UX Дизайн')
def ui_ux_design(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    price_button = types.KeyboardButton('💲Цена и сроки📅')
    learn_button = types.KeyboardButton('📊Система обучения📈')
    back_button = types.KeyboardButton('🔙Hазад')
    keyboard.add(price_button, learn_button, back_button)

    bot.send_message(message.chat.id, "Выберите, что вы хотите узнать о UI/UX Дизайне:", reply_markup=keyboard)
    states[message.chat.id] = 'ui_ux_design'


@bot.message_handler(func=lambda message: message.text == '🔙Hазад')
def back(message):
    if message.chat.id in states:
        if states[message.chat.id] == 'ui_ux_design':
            start_message(message)
        elif states[message.chat.id] == 'ui_ux_design':
            areas_message(message)
        else:
            bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")
    else:
        bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")

@bot.message_handler(func=lambda message: message.text == '💲Цена и сроки📅')
def show_price_info(message):
    url = 'https://itlogia.ru/uxui'
    response = requests.get(url)
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'lxml')

    price_element = soup.find('div', id='price')
    price_blocks = price_element.find_all('div', class_='price-block')

    price_info = []

    for block in price_blocks:
        price_value = block.find('span', class_='price-number').text.strip()
        price_unit = block.find('span', class_='price-unit').text.strip()
        price_description = block.find('div', class_='price-description').text.strip()

        price_info.append("Цена: " + price_value + price_unit + "\n" + "Описание: " + price_description)

    all_price_info = "\n\n".join(price_info)

    bot.send_message(message.chat.id, all_price_info)


@bot.message_handler(func=lambda message: message.text == '📊Система обучения📈')
def show_learn_info(message):
    url = 'https://itlogia.ru/uxui'
    response = requests.get(url)
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'lxml')

    will_learn_title = soup.find('div', class_='will-learn-title')
    course_title = will_learn_title.text.strip()
    will_learn_list_ux = soup.find('div', class_='will-learn-list ux active')
    ul_elements = will_learn_list_ux.find_all('ul')

    learn_items = []

    for ul in ul_elements:
        li_elements = ul.find_all('li')
        for li in li_elements:
            learn_items.append(li.text.strip())

    learn_text_button = "\n".join(learn_items)

    bot.send_message(message.chat.id, learn_text_button)





@bot.message_handler(func=lambda message: message.text == '🌐 JavaScript')
def java_script(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    price_button = types.KeyboardButton('💲Цена и cроки📅')
    learn_button = types.KeyboardButton('📊Сиcтема обучения📈')
    back_button = types.KeyboardButton('🔙Нaзад')
    keyboard.add(price_button, learn_button, back_button)

    bot.send_message(message.chat.id, "Выберите, что вы хотите узнать о JavaScript:", reply_markup=keyboard)
    states[message.chat.id] = 'java_script'

@bot.message_handler(func=lambda message: message.text == '🔙Нaзад')
def back(message):
    if message.chat.id in states:
        if states[message.chat.id] == 'java_script':
            start_message(message)
        elif states[message.chat.id] == 'java_script':
            areas_message(message)
        else:
            bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")
    else:
        bot.send_message(message.chat.id, "Нет предыдущего меню для возврата.")

@bot.message_handler(func=lambda message: message.text == '💲Цена и cроки📅')
def show_price_info(message):
    url = 'https://itlogia.ru/front'
    response = requests.get(url)
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'lxml')

    price_element = soup.find('div', id='price')
    price_blocks = price_element.find_all('div', class_='price-block')

    price_info = []

    for block in price_blocks:
        price_value = block.find('span', class_='price-number').text.strip()
        price_unit = block.find('span', class_='price-unit').text.strip()
        price_description = block.find('div', class_='price-description').text.strip()

        price_info.append("Цена: " + price_value + price_unit + "\n" + "Описание: " + price_description)

    all_price_info = "\n\n".join(price_info)

    bot.send_message(message.chat.id, all_price_info)


@bot.message_handler(func=lambda message: message.text == '📊Сиcтема обучения📈')
def show_learn_info(message):
    url = 'https://itlogia.ru/front'
    response = requests.get(url)
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'html.parser')
    skills_items = soup.find('div', id='skills-items')
    skill_items = skills_items.find_all('div', class_='skill-item')

    learn_text = []

    for skill_item in skill_items:
        skill_text = skill_item.get_text(strip=True)
        skill_text_cleaned = skill_text[2:]
        learn_text.append(skill_text_cleaned)

    all_learn_text = "\n".join(learn_text)

    bot.send_message(message.chat.id, all_learn_text)



@bot.message_handler(func=lambda message: message.text == '📰 Новости')
def send_news(message):
    base_url = "https://itlogia.ru/blog?category=it_industry"
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all("div", class_="article")

        articles_data = []

        for article in articles:
            title_element = article.find("a", class_="article-title")
            text_element = article.find("div", class_="article-text")
            details_element = article.find("div", class_="article-details")

            if title_element and text_element and details_element:
                title = title_element.get_text(strip=True)
                text = text_element.get_text(strip=True)
                details = details_element.get_text(strip=True)

                image_element = article.find("img")
                if image_element:
                    image_url = base_url + image_element["src"]
                else:
                    image_url = None

                article_url = base_url + title_element["href"]

                article_data = {
                    "Заголовок": title,
                    "Ссылка": article_url,
                    "Текст": text,
                    "Детали": details,
                    "Изображение": image_url
                }

                articles_data.append(article_data)


        max_articles_to_send = 5
        for i, article_data in enumerate(articles_data[:max_articles_to_send], start=1):
            news_text = f"Статья {i}:\n"
            news_text += f"Заголовок: {article_data['Заголовок']}\n"
            news_text += f"Ссылка: {article_data['Ссылка']}\n"
            news_text += f"Текст: {article_data['Текст']}\n"
            news_text += f"Детали: {article_data['Детали']}\n"
            # news_text += f"Изображение: {article_data['Изображение']}\n\n"
            bot.send_message(message.chat.id, news_text)



bot.polling()