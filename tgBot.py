import telebot
from telebot import types
from db import create_bd, add_result
from main import get_number_png


with open("token.txt", "r") as file:
    token = file.readline()


bot = telebot.TeleBot(token)

numbers = {
    "algebra-7": 1247,
    "bustova-7-1": 267,
    "bustova-7-2": 139,
    "ladjenskaya-7-1": 307,
    "ladjenskaya-7-2": 539,
    "bustova-8-1": 280,
    "bustova-8-2": 173,
    "barhydarov-8": 527,
    "algebra-8": 1153,
    "algebra-9": 1097,
    "geom-7-9": 1310,
    "geom-10-11": 763,

}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton(text="Поиск решения 🔎")
    but2 = types.KeyboardButton(text="Оставить фидбэк 📄")

    markup.add(but1, but2)

    bot.send_message(message.from_user.id, f"""Привет, {message.from_user.first_name} 🖐️! Выбери опцию:""", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def start_menu(message):
    if message.text == "Поиск решения 🔎":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        klass7 = types.KeyboardButton(text="7")
        klass8 = types.KeyboardButton(text="8")
        klass9 = types.KeyboardButton(text="9")
        markup.row(klass7, klass8, klass9)

        klass10 = types.KeyboardButton(text="10")
        klass11 = types.KeyboardButton(text="11")
        back = types.KeyboardButton(text="<-Назад")

        markup.row(klass10, klass11, back)

        bot.send_message(message.chat.id, "В каком ты классе? ⬇️", reply_markup=markup)

    elif message.text == "Оставить фидбэк 📄":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton(text="Назад ⬅️")
        markup.row(back)

        bot.send_message(message.chat.id, f"Напиши свой фидбэк. Спасибо❤️", reply_markup=markup)

    elif message.text == "Назад ⬅️" or message.text == "<-Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton(text="Поиск решения 🔎")
        but2 = types.KeyboardButton(text="Оставить фидбэк 📄")

        markup.add(but1, but2)

        bot.send_message(message.from_user.id, f"Выбери опцию:", reply_markup=markup)

    elif message.text == "7":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 7 Макарычев")
        geometry = types.KeyboardButton(text="Геометрия 7-9 Атанасян")
        russkiy1 = types.KeyboardButton(text="Русский язык 7 Быстрова")
        markup.row(algebra, geometry, russkiy1)

        russkiy2 = types.KeyboardButton(text="Русский язык 7 Ладыженская")
        back = types.KeyboardButton(text="Назад")

        markup.row(russkiy2, back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "8":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 8 Макарычев")
        geometry = types.KeyboardButton(text="Геометрия 7-9 Атанасян")
        russkiy1 = types.KeyboardButton(text="Русский язык 8 Быстрова")
        markup.row(algebra, geometry, russkiy1)

        russkiy2 = types.KeyboardButton(text="Русский язык 8 Бархударов")
        back = types.KeyboardButton(text="Назад")

        markup.row(russkiy2, back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "9":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 9 Макарычев")
        geometry = types.KeyboardButton(text="Геометрия 7-9 Атанасян")
        markup.row(algebra, geometry)

        #russkiy = types.KeyboardButton(text="Русский язык 9 Быстрова")
        back = types.KeyboardButton(text="Назад")

        markup.row(back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "10":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 10 Мордкович")
        geometry = types.KeyboardButton(text="Геометрия 10-11 Атанасян")
        markup.row(algebra, geometry)

        back = types.KeyboardButton(text="Назад")

        markup.row(back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "11":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 11 Мордкович")
        geometry = types.KeyboardButton(text="Геометрия 10-11 Атанасян")
        markup.row(algebra, geometry)

        back = types.KeyboardButton(text="Назад")

        markup.row(back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        klass7 = types.KeyboardButton(text="7")
        klass8 = types.KeyboardButton(text="8")
        klass9 = types.KeyboardButton(text="9")
        markup.row(klass7, klass8, klass9)

        klass10 = types.KeyboardButton(text="10")
        klass11 = types.KeyboardButton(text="11")
        back = types.KeyboardButton(text="<-Назад")

        markup.row(klass10, klass11, back)

        bot.send_message(message.chat.id, "В каком ты классе? ⬇️", reply_markup=markup)

    elif message.text == "Русский язык 7 Быстрова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        chast1 = types.KeyboardButton(text="I часть, Быстрова 7")
        chast2 = types.KeyboardButton(text="II часть, Быстрова 7")

        markup.row(chast1, chast2)

        back = types.KeyboardButton(text="⬅️ Назад")
        markup.row(back)

        bot.send_message(message.from_user.id, f"Какая часть?", reply_markup=markup)

    elif message.text == "Русский язык 7 Ладыженская":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        chast1 = types.KeyboardButton(text="I часть, Ладыженская 7")
        chast2 = types.KeyboardButton(text="II часть, Ладыженская 7")

        markup.row(chast1, chast2)

        back = types.KeyboardButton(text="⬅️ Назад")
        markup.row(back)

        bot.send_message(message.from_user.id, f"Какая часть?", reply_markup=markup)

    elif message.text == "I часть, Быстрова 7":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('bustova-7-1')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "7", "bistrova", "bustova-7-1", images="1")

    elif message.text == "II часть, Быстрова 7":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('bustova-7-2')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "7", "bistrova", "bustova-7-1", images="1", new="part2")

    elif message.text == "I часть, Ладыженская 7":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('ladjenskaya-7-1')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "7", "baranov", "ladjenskaya-7-1", images="1", new="new")

    elif message.text == "II часть, Ладыженская 7":
        bot.send_message(message.chat.id, f"Введите нужный номер (308-{numbers.get('ladjenskaya-7-2')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "7", "baranov", "ladjenskaya-7-2", images="1", new="new")

    elif message.text == "⬅️ Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        algebra = types.KeyboardButton(text="Алгебра 7 Макарычев")
        geometry = types.KeyboardButton(text="Геометрия 7-9 Атанасян")
        russkiy1 = types.KeyboardButton(text="Русский язык 7 Быстрова")
        markup.row(algebra, geometry, russkiy1)

        russkiy2 = types.KeyboardButton(text="Русский язык 7 Ладыженская")
        back = types.KeyboardButton(text="Назад")

        markup.row(russkiy2, back)

        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=markup)

    elif message.text == "Алгебра 7 Макарычев":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('algebra-7')})")

        bot.register_next_step_handler(message, send_number, "algebra", "7", "makarichev", "algebra-7", new="new")

    elif message.text == "Русский язык 8 Быстрова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        chast1 = types.KeyboardButton(text="I часть, Быстрова 8")
        chast2 = types.KeyboardButton(text="II часть, Быстрова 8")

        markup.row(chast1, chast2)

        back = types.KeyboardButton(text="⬅️ Назад")
        markup.row(back)

        bot.send_message(message.from_user.id, f"Какая часть?", reply_markup=markup)

    elif message.text == "Русский язык 8 Бархударов":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('barhydarov-8')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "8", "barh_new", "barhydarov-8", images="1")

    elif message.text == "I часть, Быстрова 8":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('bustova-8-1')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "8", "bistrova", "bustova-8-1", images="1")

    elif message.text == "II часть, Быстрова 8":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('bustova-8-1')})")

        bot.register_next_step_handler(message, send_number, "russkijazik", "8", "bistrova", "bustova-8-2", images="1", new="part2")

    elif message.text == "Алгебра 8 Макарычев":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('algebra-8')})")

        bot.register_next_step_handler(message, send_number, "algebra", "8", "makarichev", "algebra-8", images="1", new="2")

    elif message.text == "Алгебра 9 Макарычев":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('algebra-9')})")

        bot.register_next_step_handler(message, send_number, "algebra", "9", "makarichev", "algebra-9")

    elif message.text == "Геометрия 7-9 Атанасян":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('geom-7-9')})")

        bot.register_next_step_handler(message, send_number, "geometriya", "7", "atanasyan", "geom-7-9", images="1")

    elif message.text == "Геометрия 10-11 Атанасян":
        bot.send_message(message.chat.id, f"Введите нужный номер (1-{numbers.get('geom-10-11')})")

        bot.register_next_step_handler(message, send_number, "geometriya", "10", "atanasyan10-11", "geom-10-11", new="clear")

    elif message.text == "Алгебра 10 Мордкович":
        bot.register_next_step_handler(message, send_number_mod, "algebra", "10", "mordkovich2", new="clear", check="check")




    else:
        create_bd()
        add_result(message.from_user.username, message.text)


def send_number(message, subject, klass, autor, sub_subject, images="", new="", check=""):
    flag = False

    while not flag:
        try:
            if 1 <= int(message.text) <= numbers.get(sub_subject):
                bot.send_photo(message.chat.id, get_number_png(subject=subject, klass=klass, number=message.text, autor=autor, images=images, new=new, check=check))
                flag = True
                bot.register_next_step_handler(message, start_menu)
                break
            else:
                bot.send_message(message.chat.id, "Некорректный ввод, выберите предмет и номер заново")
                flag = True
                break
        except ValueError:
            bot.send_message(message.chat.id, "Некорректный ввод, выберите предмет и номер заново")
            flag = True
            break


def send_number_mod(message, subject, klass, autor, images="", new="", check=""):
    bot.send_message(message.chat.id, f"Введите нужный номер 1-123 (Повторение) или 1.1-49.30 (через точку)")

    try:
        if 1 <= int(message.text) <= 123:
            pass


    except ValueError:
        pass

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
