from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('setcaption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Please include your captions.\n\nExample:- `/setcaption pyrogrammers`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Captions added ✅**")

@Client.on_message(filters.private & filters.command('remcaption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**No captions available to remove.**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**Captions removed ✅**")
                                       
@Client.on_message(filters.private & filters.command('caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Available captions:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**No captions available.**")
          
