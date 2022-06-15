from pyrogram import Client, filters 
from pyrogram.types import Chatpermission
from pyrogram.types import InlinekeyboardButton, InlinekeyboardMarkup
import os

bot=Client(
    "Night Vission Bot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

START_MESSAGE = "Im Night Vission Group Help Bot"
START_MESSAGE_BUTTONS = [
[InlinekeyboardButton('SUPPORT', url='https://t.me/NightVisssion')
]
@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
	text = START_MESSAGE
	reply_markup = InlinekeyboardMarkup(START_MESSAGE_BUTTONS)
	message.reply(
	text=text,
	reply_markup=reply_markup
	disable_web_page_preview=True

print("Night Vission Bot Online Danger")
bot.run()
