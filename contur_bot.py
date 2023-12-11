import telebot
from telebot import types

bot = telebot.TeleBot('Укажите здесь токен вашего бота полученного от BotFather')

links = {
    "company": "https://kontur.ru/about/info",
    "products": "https://kontur.ru/products",
    "news": "https://kontur.ru/press/news/company",
    "careers": "https://kontur.ru/career",
    "vacancies": "https://kontur.ru/career/vacancies/conditions",
    "interns": "https://kontur.ru/education/programs/intern",
    "partnership": "https://kontur.ru/partnership",
    "contacts": "https://kontur.ru/contacts/66/city-5457",
    "book": "https://kontur.ru/press/news/47738-skb_kontur_vypustil_pervuyu_knigu_ob_it_na_urale",
}

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-гид в мире Контура!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Чем занимается кампания Контур?')
        btn2 = types.KeyboardButton('Какие продукты производит кампания Контур?')
        btn3 = types.KeyboardButton('Что нового произошло в Контуре')
        btn4 = types.KeyboardButton('Какие вакансии есть в Контуре?')
        btn5 = types.KeyboardButton('Как попасть на работу в Контур?')
        btn6 = types.KeyboardButton('Бывают ли в Контуре стажировки?')
        btn7 = types.KeyboardButton('У Контура есть своя обучающая платформа?')
        btn8 = types.KeyboardButton('Как стать партнером Контура?')
        btn9 = types.KeyboardButton('Где можно посмотреть контактную информацию?')
        btn10 = types.KeyboardButton('Как мне можно получить экземпляр книги "35. IT-история"?')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)


    elif message.text == 'Чем занимается кампания Контур?':
        bot.send_message(message.from_user.id, 'Контур создает программное обеспечение для бизнеса с 1988 года... ' + f'{links["company"]}', parse_mode='Markdown')

    elif message.text == 'Какие продукты производит кампания Контур?':
        bot.send_message(message.from_user.id, 'В портфеле Контура более 70 продуктов —... ' + f'{links["products"]}', parse_mode='Markdown')

    elif message.text == 'Что нового произошло в Контуре':
        bot.send_message(message.from_user.id, 'Последние новости кампании можно посмотреть здесь... ' + f'{links["news"]}', parse_mode='Markdown')

    elif message.text == 'Какие вакансии есть в Контуре?':
        bot.send_message(message.from_user.id, 'Подробно обо всех вакансиях можно прочитать здесь... ' + f'{links["careers"]}', parse_mode='Markdown')

    elif message.text == 'Как попасть на работу в Контур?':
        bot.send_message(message.from_user.id, 'У нас несколько этапов приема на работу, каждый из них помогает понять, что мы на 100% подходим друг другу... ' + f'{links["vacancies"]}', parse_mode='Markdown')

    elif message.text == 'Бывают ли в Контуре стажировки?':
        bot.send_message(message.from_user.id, 'Да, у нас регулярно проходят стажировки по различным направлениям... ' + f'{links["interns"]}', parse_mode='Markdown')

    elif message.text == 'У Контура есть своя обучающая платформа?':
        bot.send_message(message.from_user.id, 'У нас есть бесплатная платформа с интерактивными онлайн-курсами Ulearn.me, где можно пройти курсы по различным направлениям... ', parse_mode='Markdown')

    elif message.text == 'Как стать партнером Контура?':
        bot.send_message(message.from_user.id, 'Выберите удобную форму партнерства и начните зарабатывать с нами... ' + f'{links["partnership"]}', parse_mode='Markdown')

    elif message.text == 'Где можно посмотреть контактную информацию?':
        bot.send_message(message.from_user.id, 'Всю подробную информацию о том как связаться с нами, вы можете найти здесь... ' + f'{links["contacts"]}', parse_mode='Markdown')

    elif message.text == 'Как мне можно получить экземпляр книги "35. IT-история"?':
        bot.send_message(message.from_user.id, 'К сожалению в продажу книга не поступит, но около трети тиража будет передано в федеральные и региональные библиотеки страны... ' + f'{links["book"]}', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)