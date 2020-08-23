from datetime import datetime as dt

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler

from spreadsheet import sheet
from texts import HELLO_MESSAGE

users = []  # users of bot
row = []


SMALL_SEIZURE, BIG_SEIZURE, MOOD, ASK_WEATHER, WAS_NISE, WAS_SOLPADEIN, WAS_ANALGIN, WAS_NOSHPA, FEEDBACK, ADDITIONAL = range(
    10
)

def hello(update, context):
    users.append(update.effective_user.id)
    update.message.reply_text(HELLO_MESSAGE)
    return SMALL_SEIZURE


def reply_to_first(update, context):
    reply_keyboard = [["Да", "Нет"]]
    global row
    row = [dt.strftime(dt.now(), "%d.%m.%Y. %H:%M"), update.message.text]
    update.message.reply_text(
        "Был ли большой приступ?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return BIG_SEIZURE


def reply_to_second(update, context):
    row.append(update.message.text)
    update.message.reply_text("Какое у Илюши было настроение, общее состояние, поведение?")
    return MOOD


def reply_to_third(update, context):
    row.append(update.message.text)
    update.message.reply_text("Какая сегодня была погода?")
    return ASK_WEATHER

# def reply_to_fourth(update, context):
#     row.append(update.message.text)
#     update.message.reply_text("Какое было поведение у Илюши?")
#     return BEHAVIOR


def nise(update, context):
    reply_keyboard = [["Да", "Нет"]]
    row.append(update.message.text)
    update.message.reply_text(
        "Сегодня давали Найз?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return WAS_NISE

def solpadein(update, context):
    reply_keyboard = [["Да", "Нет"]]
    row.append(update.message.text)
    update.message.reply_text("А Солпадеин?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WAS_SOLPADEIN


def analgin(update, context):
    reply_keyboard = [["Да", "Нет"]]
    row.append(update.message.text)
    update.message.reply_text("Анальгин?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WAS_ANALGIN


def noshpa(update, context):
    reply_keyboard = [["Да", "Нет"]]
    row.append(update.message.text)
    update.message.reply_text("Давали Ношпу?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return WAS_NOSHPA


def thanks(update, context):
    reply_keyboard = [["Да", "Нет"]]
    row.append(update.message.text)
    update.message.reply_text(
        "Спасибо за ответы! Хочешь еще что-то добавить?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return FEEDBACK


def goodbye(update, context):
    update.message.reply_text("Пока!")
    sheet.append_row(row)
    del row[:]
    return SMALL_SEIZURE

def save_and_goodbye(update, context):
    row.append(update.message.text)
    return goodbye(update, context)

#   row.append(update.message.text)
#   update.message.reply_text('Спасибо за ответы! В любой момент их можно дополнить, просто написав сюда')
#   return FEEDBACK

def additions(update, context):
    row.append(update.message.text)
    update.message.reply_text("Давай, записываю.")
    return ADDITIONAL


conversation = ConversationHandler(
    entry_points=[CommandHandler("start", hello), MessageHandler(Filters.regex("^(Да, был)$"), reply_to_first), MessageHandler(Filters.regex("^(Нет, не было)$"), reply_to_first)],
    states={
        SMALL_SEIZURE: [CommandHandler("start", hello), MessageHandler(Filters.text, reply_to_first)],
        # BIG_SEIZURE: [MessageHandler(Filters.regex("^(Да, был)$"), reply_to_second), MessageHandler(Filters.regex("^(Нет, не было)$"), reply_to_second)],
        BIG_SEIZURE: [
            MessageHandler(Filters.regex("^(Да)$"), reply_to_second()),
            MessageHandler(Filters.regex("^(Нет)$"), reply_to_second()),
        ],
        MOOD: [MessageHandler(Filters.text, reply_to_third)],
        ASK_WEATHER: [MessageHandler(Filters.text, nise)],
        # BEHAVIOR: [MessageHandler(Filters.text, nise)],
        WAS_NISE: [
            CommandHandler("start", hello),
            MessageHandler(Filters.regex("^(Да)$"), solpadein),
            MessageHandler(Filters.regex("^(Нет)$"), solpadein),
        ],
        WAS_SOLPADEIN: [
            CommandHandler("start", hello),
            MessageHandler(Filters.regex("^(Да)$"), analgin),
            MessageHandler(Filters.regex("^(Нет)$"), analgin),
        ],
        WAS_ANALGIN: [
            CommandHandler("start", hello),
            MessageHandler(Filters.regex("^(Да)$"), noshpa),
            MessageHandler(Filters.regex("^(Нет)$"), noshpa),
        ],
        WAS_NOSHPA: [
            CommandHandler("start", hello),
            MessageHandler(Filters.regex("^(Да)$"), thanks),
            MessageHandler(Filters.regex("^(Нет)$"), thanks),
        ],
        FEEDBACK: [
            CommandHandler("start", hello),
            MessageHandler(Filters.regex("^(Да)$"), additions),
            MessageHandler(Filters.regex("^(Нет)$"), goodbye),
        ],
        ADDITIONAL: [MessageHandler(Filters.text, save_and_goodbye)],
    },
    fallbacks=[],
)
