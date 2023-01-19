from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["share"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Share Link" ,url=f"https://t.me/share/url?url=https://t.me/NameEditor_Bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Share this bot to your friend and earn 500 MB bandwidth.\nPer Refer 500MB\n Your Link :- https://t.me/NameEditor_Bot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
