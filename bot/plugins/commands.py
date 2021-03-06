#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import random

PHOTOS = [
    "https://telegra.ph/file/80159c858477ea63ce852.jpg",
    "https://telegra.ph/file/9b4f641dc0ebf071771d2.jpg",
    "https://telegra.ph/file/9fabb9ad9ebffd6211f28.jpg",
    "https://telegra.ph/file/84e93fe8ab3dcb74d8a23.jpg",
    "https://telegra.ph/file/84e93fe8ab3dcb74d8a23.jpg",
    "https://telegra.ph/file/84e93fe8ab3dcb74d8a23.jpg",
]

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @movie_center_RU</b>\n \n<b>♻️Join Our Group: @moviecenter321</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                    
                        [
                            InlineKeyboardButton
                                (
                                    '🙏 join our channel🙏', url="https://t.me/movie_center_RU"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://t.me/moviecenter321"
                                )
                        ]
                       
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🔰⚡ My Group 🔰⚡', url='https://t.me/moviecenter321')
    ],[
        InlineKeyboardButton('🔰 join our channel  🔰', url ='https://t.me/movie_center_RU'),
        
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=random.choice(PHOTOS),
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
