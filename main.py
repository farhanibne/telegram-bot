import json
from datetime import datetime, timedelta

from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Updater,
    Filters,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
)

def main():
    BOT_TOKEN = "YOUR TOKEN HERE"
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # leave here empty, we will add some code later

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Bot is running...")
    main()

    main_keyboard = [
    ["➕ Add Reminder", "➖ Delete History"],
    ["📃 All Reminders", "🌐 Change UTC"],
    ["💰 Donate"],
    ]

    REMINDER_TITLE, REMINDER_DATE, REMINDER_TIME, REMINDER_INFO = range(4)
    DELETE_REMINDER_INDEX = range(1)
    ADD_UTC = range(1)  


    {
    "users": {

    }
}

def is_new_user(user, username, first_name, last_name):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        if user not in content["users"]:
            content["users"][user] = {
                "username": username,
                "first name": first_name,
                "last name": last_name,
                "utc": "",
                "reminders": [],
            }
            file.seek(0)
            json.dump(content, file)
            file.truncate()

            return True
        else:
            return False


def json_add_utc(user, utc):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["utc"] = utc
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_get_utc(user):
    user = str(user)
    with open("data.json", "r") as file:
        content = json.load(file)
        return content["users"][user]["utc"]


def json_get_info(user):
    user = str(user)
    with open("data.json", "r") as file:
        content = json.load(file)
        return content["users"][user]["reminders"][0]


def json_add_reminder(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["reminders"].insert(
            0, {"title": "", "date": "", "time": "", "info": ""}
        )
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_add_reminder_info(user, key, value):
    user = str(user)
    key = str(key)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["reminders"][0][key] = value
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_cancel_add_reminder_process(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        del content["users"][user]["reminders"][0]
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_delete_reminder(user, index):
    user = str(user)
    index = index - 1

    with open("data.json", "r+") as file:
        content = json.load(file)

        del content["users"][user]["reminders"][index]
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_get_reminders_list(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content = content["users"][user]["reminders"]

        if len(content) == 0:
            message = "📪 You have no reminders!"
            return message

        else:
            message = ""
            for i in range(len(content)):
                title = content[i]["title"]
                date = content[i]["date"]
                time = content[i]["time"]
                info = content[i]["info"]

                message += f"""
*Reminder {i+1}*
------------------
_Title_ : {title}
_Date_ : {date}
_Time_ : {time}
_Info_ : {info}
"""
            return message

def is_new_user(user, username, first_name, last_name):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        if user not in content["users"]:
            content["users"][user] = {
                "username": username,
                "first name": first_name,
                "last name": last_name,
                "utc": "",
                "reminders": [],
            }
            file.seek(0)
            json.dump(content, file)
            file.truncate()

            return True
        else:
            return False


def json_add_utc(user, utc):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["utc"] = utc
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_get_utc(user):
    user = str(user)
    with open("data.json", "r") as file:
        content = json.load(file)
        return content["users"][user]["utc"]


def json_get_info(user):
    user = str(user)
    with open("data.json", "r") as file:
        content = json.load(file)
        return content["users"][user]["reminders"][0]


def json_add_reminder(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["reminders"].insert(
            0, {"title": "", "date": "", "time": "", "info": ""}
        )
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_add_reminder_info(user, key, value):
    user = str(user)
    key = str(key)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content["users"][user]["reminders"][0][key] = value
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_cancel_add_reminder_process(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        del content["users"][user]["reminders"][0]
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_delete_reminder(user, index):
    user = str(user)
    index = index - 1

    with open("data.json", "r+") as file:
        content = json.load(file)

        del content["users"][user]["reminders"][index]
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def json_get_reminders_list(user):
    user = str(user)
    with open("data.json", "r+") as file:
        content = json.load(file)
        content = content["users"][user]["reminders"]

        if len(content) == 0:
            message = "📪 You have no reminders!"
            return message

        else:
            message = ""
            for i in range(len(content)):
                title = content[i]["title"]
                date = content[i]["date"]
                time = content[i]["time"]
                info = content[i]["info"]

                message += f"""
*Reminder {i+1}*
------------------
_Title_ : {title}
_Date_ : {date}
_Time_ : {time}
_Info_ : {info}
"""
            return message

start_command_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start_command)],
        states={
       ADD_UTC: [MessageHandler(Filters.text, add_utc)],
        },
    fallbacks=[CommandHandler("nevermind", start_command)],
              )
dp.add_handler(start_command_handler)

change_utc_handler = ConversationHandler(
entry_points=[MessageHandler(Filters.regex("Change UTC"), request_utc)],
states={
ADD_UTC: [MessageHandler(Filters.text, add_utc)],
},
fallbacks=[CommandHandler("nevermind", request_utc)],
)
dp.add_handler(change_utc_handler)

dp.add_handler(MessageHandler(Filters.regex("Donate"), donate))
dp.add_handler(MessageHandler(Filters.regex("All Reminders"), all_reminders))

add_reminder_handler = ConversationHandler(
entry_points=[MessageHandler(Filters.regex("Add Reminder"), add_reminder)],
states={
REMINDER_TITLE: [
MessageHandler(
Filters.text & ~Filters.regex("/cancel"), add_reminder_title
)
],
REMINDER_DATE: [
MessageHandler(
Filters.text & ~Filters.regex("/cancel"), add_reminder_date
)
],
REMINDER_TIME: [
MessageHandler(
Filters.text & ~Filters.regex("/cancel"), add_reminder_time
)
],
REMINDER_INFO: [
MessageHandler(
Filters.text & ~Filters.regex("/cancel"), add_reminder_info
)
],
},
fallbacks=[CommandHandler("cancel", cancel_add_reminder_process)],
)
dp.add_handler(add_reminder_handler)

delete_reminder_handler = ConversationHandler(
entry_points=[MessageHandler(Filters.regex("Delete History"), delete_reminder)],
states={
DELETE_REMINDER_INDEX: [
MessageHandler(
Filters.text & ~Filters.regex("/cancel"), delete_reminder_status
)
]
},
fallbacks=[CommandHandler("cancel", cancel_delete_reminder_process)],
)
dp.add_handler(delete_reminder_handler)            