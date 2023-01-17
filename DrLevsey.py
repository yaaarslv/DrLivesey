import time

import telebot
from random import randint

bot = telebot.TeleBot("5575703836:AAEhpCnHnK0rh7U8-k4T83P4TUhD4A_7CXw")
bye = [" просто не чекнул закреп...", ", надо было чекать закреп...", ", вот что бывает с теми, кто не чекает закреп!"]
thanks = [", коллеги благодарят тебя за особый вклад в общее дело!", ", коллеги никогда не забудут твой подвиг!",
          ", партия гордится тобой! ⬆️+15 Social Credit!"]
botId = ["5575703836"]


# testBot: 5876092899
# testBot token: 5876092899:AAGZwkHM5TprkQMTFW6LaJb5AYNfBqHvFOY
# DrLiveseyBot: 5575703836
# DrLiveseyBot: 5575703836:AAEhpCnHnK0rh7U8-k4T83P4TUhD4A_7CXw

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    if str(message.new_chat_members[-1].id) not in botId:
        bot.reply_to(message, text=f"Привет, {message.new_chat_members[-1].first_name}, чек закреп!")
        try:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEGbzFjc-GLICudZ_b77O1sKZMLc4BJTAACjRUAAr2-IEuA70Dwz-uXhCsE")
        except:
            pass
    else:
        bot.send_message(message.chat.id, text="А вот и я, доктор Ливси!")
        bot.send_sticker(message.chat.id,
                         sticker="CAACAgQAAxkBAAIOvmN3vDkjwFrQhs_lAUEsDnlKoOAKAAKPAAN5vGEb_3g0j6RPZKgrBA")


@bot.message_handler(content_types=['left_chat_member'])
def byebye(message):
    if str(message.left_chat_member.id) not in botId:
        bot.reply_to(message, text=f"{message.left_chat_member.first_name}{str(bye[randint(0, len(bye) - 1)])}")


collegue = ["CAACAgIAAxkBAAINnmN1Dne4lf5d64MCS7PMdTPWokX9AAImFQACFj4hSwd5XTnarBVEKwQ",
            "CAACAgIAAxkBAAINoWN1DnqHacqUXVYIa7zTJwABa0ExxwACeRkAAuUmIEv007ioyytd_CsE",
            "CAACAgIAAxkBAAINpGN1P97KpnAOArVJo9Rs9AK3EsYlAAKcAAPL-X42TetF5XFHdhsrBA",
            "CAACAgIAAxkBAAINp2N1P_RVuo9NPs99wTIJ7TyPNDXbAAKRFAACrjTJS-5HNWJaZVbWKwQ",
            "CAACAgIAAxkBAAINqmN1P_1vOpOEu7I1krwSgQRuvCWlAAJEBAAC9zQbAAHyIgWOZkgPbCsE",
            "CAACAgIAAxkBAAINrWN1QArTnbDohQcI9bqHhnnPEsuIAAKQFAAC6WIZS0pHLyQzeNG7KwQ",
            "CAACAgIAAxkBAAINsGN1QBHVqsKyR21t6LI4czVf51WSAAJiAAMdkcYZjgYENdbpf7UrBA",
            "CAACAgIAAxkBAAINs2N1QBvP5CEF6JvCHFaGflgCY7UoAAIoAAPzY8QsNN5xnWJQZQErBA",
            "CAACAgIAAxkBAAINtmN1QCMZ6--tm9IZ92wFNbivgCJyAAJIAAPzY8QsyiiJhoTDjssrBA",
            "CAACAgIAAxkBAAINuWN1QCo2SLJv-DNONJ5DGxgjAw_jAAI7DQACx5LJSr3P7ywpsRn1KwQ",
            "CAACAgIAAxkBAAINvGN1QDIKLzpKrxSGFepVHpNHmlDgAAIYAANG2OkFNm1z_4tdxuorBA",
            "CAACAgIAAxkBAAINv2N1QDxmj1XMxH7M5D99yTboGAybAAIRAAPkxRkgZUOQmGqFKBgrBA",
            "CAACAgIAAxkBAAINwmN1QEYnP9rGi9cZi1apd7Ay0kPGAAIMAAORaAwAATaDLTe5U0mQKwQ",
            "CAACAgIAAxkBAAINxWN1QEyNa8MNk0yA1wIpnBtRGSj5AALcAAM8ilca1iybPBKDYEwrBA"]


global ColleagueListBzhd
global ColleagueListFizika
ColleagueListBzhd = []
ColleagueListFizika = []
#физика: -1001528341717
#бжд: -1001663618158


@bot.message_handler(content_types=["pinned_message"])
def message_was_pinned(message):
    if message.chat.title != "ИС ООП у25":
        bot.reply_to(message.pinned_message,
                     text=f"@{message.pinned_message.from_user.username}{str(thanks[randint(0, len(thanks) - 1)])}")
        try:
            bot.send_sticker(message.chat.id, f"{str(collegue[randint(0, len(collegue) - 1)])}")
        except:
            pass

        global ColleagueListBzhd
        added = False
        index = -1
        for i in range(len(ColleagueListBzhd)):
            if f"@{message.pinned_message.from_user.username}" in ColleagueListBzhd[i]:
                added = True
                index = i
                break
        if not added:
            ColleagueListBzhd.append([f"@{message.pinned_message.from_user.username}", 1])
        else:
            ColleagueListBzhd[index][1] += 1


ladno = ["ладно"]
Ulyana = ["ульяна"]


def ladno_Ulyana(message):
    try:
        lad = message.text.split(" ")[0].lower()
        ul = message.text.split(" ")[-1].lower()
        if lad in ladno and ul in Ulyana:
            bot.send_message(message.chat.id, text="Ладно, Ульяна")
    except:
        pass


def baza(message):
    if (message.text == "/baza") or (message.text == "/база"):
        rand = randint(1, 15)
        if rand == 10:
            bot.reply_to(message, text="Вы отчислены без ПСЖ. Поздравляю!")
            try:
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAISbGOdshUFIk5XFtXhyJU2qGww4IYeAALmKQAC_VXQS994eQfZW9DrLAQ")
            except:
                pass
        else:
            text = '[Отправляю координаты базы:](https://fitp.itmo.ru/files/lgd.pdf)'
            bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
            print(message.chat.id)


def sortByNumber(inputArr):
    return inputArr[1]


def sortColleagues():
    global ColleagueListBzhd
    global ColleagueListFizika
    ColleagueListBzhd.sort(key=sortByNumber, reverse=True)
    ColleagueListFizika.sort(key=sortByNumber, reverse=True)


def setColleagueList(message):
    command = message.text.split(" ")
    if command[0] == "/setList":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            chat_name = command[1]
            colleagues = message.text.split(" ")[2:]
            if len(colleagues) != 0:
                if chat_name == "бжд":
                    global ColleagueListBzhd
                    ColleagueListBzhd = []
                    for i in range(0, len(colleagues), 2):
                        ColleagueListBzhd.append([colleagues[i], colleagues[i + 1]])
                elif chat_name == "физика":
                    global ColleagueListFizika
                    ColleagueListFizika = []
                    for i in range(0, len(colleagues), 2):
                        ColleagueListFizika.append([colleagues[i], colleagues[i + 1]])
            else:
                bot.send_message(message.chat.id, "Пустой аргумент!")
        else:
            bot.send_message(message.chat.id, "Вы не имеете права изменять список коллег!")
        sortColleagues()


def clearColleagueList(message):
    command = message.text.split(" ")
    if command[0] == "/clearList":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            chat_name = command[1]
            if chat_name == "бжд":
                global ColleagueListBzhd
                ColleagueListBzhd = []
            elif chat_name == "физика":
                global ColleagueListFizika
                ColleagueListFizika = []
        else:
            bot.send_message(message.chat.id, "Вы не имеете права изменять список коллег!")


def addColleagues(message):
    command = message.text.split(" ")
    if command[0] == "/addColleagues":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            chat_name = command[1]
            colleagues = message.text.split(" ")[2:]
            if len(colleagues) != 0:
                if chat_name == "бжд":
                    global ColleagueListBzhd
                    for i in range(0, len(colleagues), 2):
                        added = False
                        for j in range(len(ColleagueListBzhd)):
                            if colleagues[i] in ColleagueListBzhd[j]:
                                added = True
                                break
                        if not added:
                            ColleagueListBzhd.append([colleagues[i], colleagues[i + 1]])
                        else:
                            bot.send_message(message.chat.id, f"Коллега {colleagues[i]} уже есть в списке")
                elif chat_name == "физика":
                    global ColleagueListFizika
                    for i in range(0, len(colleagues), 2):
                        added = False
                        for j in range(len(ColleagueListFizika)):
                            if colleagues[i] in ColleagueListFizika[j]:
                                added = True
                                break
                        if not added:
                            ColleagueListFizika.append([colleagues[i], colleagues[i + 1]])
                        else:
                            bot.send_message(message.chat.id, f"Коллега {colleagues[i]} уже есть в списке")
            else:
                bot.send_message(message.chat.id, "Пустой аргумент!")
        else:
            bot.send_message(message.chat.id, "Вы не имеете права изменять список коллег!")
        sortColleagues()


def removeColleagues(message):
    command = message.text.split(" ")
    if command[0] == "/removeColleagues":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            chat_name = command[1]
            colleagues = message.text.split(" ")[2:]
            if len(colleagues) != 0:
                if chat_name == "бжд":
                    global ColleagueListBzhd
                    for i in range(len(colleagues)):
                        removed = False
                        for j in range(len(ColleagueListBzhd)):
                            if colleagues[i] in ColleagueListBzhd[j]:
                                removed = True
                                ColleagueListBzhd.pop(j)
                                break
                        if not removed:
                            bot.send_message(message.chat.id, f"Коллеги {colleagues[i]} нет в списке")
                elif chat_name == "физика":
                    global ColleagueListFizika
                    for i in range(len(colleagues)):
                        removed = False
                        for j in range(len(ColleagueListFizika)):
                            if colleagues[i] in ColleagueListFizika[j]:
                                removed = True
                                ColleagueListFizika.pop(j)
                                break
                        if not removed:
                            bot.send_message(message.chat.id, f"Коллеги {colleagues[i]} нет в списке")
            else:
                bot.send_message(message.chat.id, "Пустой аргумент!")
        else:
            bot.send_message(message.chat.id, "Вы не имеете права изменять список коллег!")
        sortColleagues()


def printColleagues(message):
    if message.text == "/rating":
        if str(message.chat.id) == "-1001528341717":
            if len(ColleagueListFizika) != 0:
                text = "Рейтинг закрепов уважаемых коллег:\n"
                for i in range(len(ColleagueListFizika)):
                    text += f"{i + 1}) " + ColleagueListFizika[i][0][1:] + " - " + str(ColleagueListFizika[i][1]) + "\n"
                bot.send_message(message.chat.id, text)
                return
            else:
                bot.send_message(message.chat.id, "Список коллег пустой")
        elif str(message.chat.id) == "-1001663618158":
            if len(ColleagueListBzhd) != 0:
                text = "Рейтинг закрепов уважаемых коллег:\n"
                for i in range(len(ColleagueListBzhd)):
                    text += f"{i + 1}) " + ColleagueListBzhd[i][0][1:] + " - " + str(ColleagueListBzhd[i][1]) + "\n"
                bot.send_message(message.chat.id, text)
                return
            else:
                bot.send_message(message.chat.id, "Список коллег пустой")
        elif str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            if len(ColleagueListFizika) != 0:
                text = "Физика:\nРейтинг закрепов уважаемых коллег:\n"
                for i in range(len(ColleagueListFizika)):
                    text += f"{i + 1}) " + ColleagueListFizika[i][0][1:] + " - " + str(ColleagueListFizika[i][1]) + "\n"
                bot.send_message(message.chat.id, text)
            else:
                bot.send_message(message.chat.id, "Список коллег пустой")
            if len(ColleagueListBzhd) != 0:
                text = "БЖД:\nРейтинг закрепов уважаемых коллег:\n"
                for i in range(len(ColleagueListBzhd)):
                    text += f"{i + 1}) " + ColleagueListBzhd[i][0][1:] + " - " + str(ColleagueListBzhd[i][1]) + "\n"
                bot.send_message(message.chat.id, text)
            else:
                bot.send_message(message.chat.id, "Список коллег пустой")
        elif str(message.chat.id) == "358682084" and str(message.from_user.id) == "358682084":
            bot.send_message(message.chat.id, "Серёжа заебал")
        else:
            bot.send_message(message.chat.id, "Проси рейтинг в беседах")

def sendZaebannostToFizika(message):
    if message.text == "/zaebaliFizika":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            bot.send_message(-1001528341717, "Хватит спамить, я уже заебался отправлять вам псж 🤬")


def sendZaebannostToBzd(message):
    if message.text == "/zaebaliBzd":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            bot.send_message(-1001663618158, "Хватит спамить, я уже заебался отправлять вам псж 🤬")


def sendMessage(message):
    command = message.text.split("\n")
    if command[0] == "/sendMessage":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            to = int(command[1])
            text = message.text.split("\n")[2:]
            bot.send_message(to, text=text[0])


def sendHelp(message):
    command = message.text.split("\n")
    if command[0] == "/sendHelp":
        if str(message.chat.id) == "879035670" and str(message.from_user.id) == "879035670":
            text = message.text.split("\n")[2:]
            if command[1] == "физика":
                bot.send_message(-1001528341717, text=text[0])
            elif command[1] == "бжд":
                bot.send_message(-1001663618158, text=text[0])


@bot.message_handler(content_types=["document", "voice", "file", "photo", "video"])
def sendToKollega(message):
    if str(message.chat.id) != "-1001528341717" and str(message.chat.id) != "-1001663618158":
        #if message.text not in ["/baza", "/база", "/rating"]:
            #bot.send_message(message.chat.id, text="Больше не благодарю, за дальнейший спам ты будешь добавлен в список антиколлег")
        bot.forward_message(-1001726325728, message.chat.id, message.id)
        bot.send_message(-708771697, text=f"Text: {message.text}\nChat id: {message.chat.id}\nChat title: {message.chat.title}\nUser: {message.from_user}")

# # def deleteMessages(message):
# #     if message.text == "/deleteMessage":


@bot.message_handler(content_types=["text"])
def textHandler(message):
    if message.text != "/start":
        ladno_Ulyana(message)
        baza(message)
        setColleagueList(message)
        printColleagues(message)
        clearColleagueList(message)
        addColleagues(message)
        removeColleagues(message)
        sendHelp(message)
        sendZaebannostToFizika(message)
        sendZaebannostToBzd(message)
        sendToKollega(message)
        sendMessage(message)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Этот бот предназначен для совета просмотреть закрепленные сообщения новыми участниками группы, рейтинга участников в этих группах, сбора лабораторных работ по физике и отправке бланка для отчисления по собственному желанию. Больше бот ничего не умеет! НЕ НУЖНО СПАМИТЬ ЕМУ В ЛИЧНЫЕ СООБЩЕНИЯ! НИКАКОЙ ПОЛЕЗНОЙ ИНФОРМАЦИИ ВЫ НЕ ПОЛУЧИТЕ!\n\nHi! This bot is designed for the council to view pinned messages by new group members, rating participants in these groups, collecting laboratory work on physics and sending a form for deduction at their own request. The bot can't do anything else! NO NEED TO SPAM HIM IN PRIVATE MESSAGES! YOU WON'T GET ANY USEFUL INFORMATION!\n\nChào! Bot này được thiết kế để hội đồng xem các tin nhắn được ghim bởi các thành viên nhóm mới, những người tham gia xếp hạng trong các nhóm này, thu thập công việc trong phòng thí nghiệm về vật lý và gửi một biểu mẫu để khấu trừ theo yêu cầu của riêng họ. Bot không thể làm gì khác! KHÔNG CẦN PHẢI SPAM ANH TA TRONG TIN NHẮN RIÊNG TƯ! BẠN SẼ KHÔNG NHẬN ĐƯỢC BẤT KỲ THÔNG TIN HỮU ÍCH!")


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)