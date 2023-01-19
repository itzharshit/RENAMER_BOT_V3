"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('premium'))
async def upgrade(bot,update):
	text = """**Free Plan**
	Daily  Upload limit 5GB
	Price Free
	
	**Plan 1 ** 
	Daily  Bandwidth 20GB
	Price 100 Rupees  🇮🇳/🌎 2$  per Month
	
	**Plan 2 **
	Daily Bandwidth 50GB
	Price Rs 150  🇮🇳/🌎 3$  per Month
	
	**Plan 3**
	Daily Bandwidth 100GB
	Price Rs 250  🇮🇳/🌎 4$  per Month
	
	**Plan 4**
	Daily Bandwidth Unlimited
	Price Rs 400  🇮🇳/🌎 7$  per Month
	
	Pay using BTC ```bc1ql4fxwhkw7g7jl7g26kwpzlqf7kvjr8evrvv08s```
	For UPI and debit card contact @michaelpanther
	After Payment Send Screenshot Of 
        Payment To @michaelpanther"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MichaelPanther")], 
        			[InlineKeyboardButton("Crypto 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Debit, credit card",url = "https://t.me/MichaelPanther")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan**
	Daily  Upload limit 2GB
	Price 0
	
	**Plan 1 ** 
	Daily  Bandwidth 20GB
	Price 100 Rupees  🇮🇳/🌎 2$  per Month
	
	**Plan 2 **
	Daily Bandwidth 50GB
	Price Rs 150  🇮🇳/🌎 3$  per Month
	
	**Plan 3**
	Daily Bandwidth 100GB
	Price Rs 250  🇮🇳/🌎 4$  per Month
	
	**Plan 4**
	Daily Bandwidth Unlimited
	Price Rs 400  🇮🇳/🌎 7$  per Month
	
	
	Pay Using Upi I'd ```9480251952@paytm```
	
	After Payment Send Screenshots Of 
        Payment To @michaelpanther"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/MichaelPanther")], 
        			[InlineKeyboardButton("Crypto 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Debit, credit card",url = "https://t.me/MichaelPanther")],[InlineKeyboardButton("Cancel",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)
