#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

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
                caption = f"<code>{file_name}</code>\n🔰༺ ──•◈•─ ─•◈•──༻🔰\n📢ɢʀᴏᴜᴘ    :@movie_house2\n📢ᴄʜᴀɴɴᴇʟ :@ds_movies1",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ Share Group 🎖️', url="https://t.me/share/url?url=https://t.me/movie_house2"
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
        InlineKeyboardButton('⚜️ My Developer ⚜️', url='https://t.me/DS_KUNJAVA')
    ],[
        InlineKeyboardButton('🔰 ɢʀᴏᴜᴘ 🔰', url ='https://t.me/movie_house2'),
        InlineKeyboardButton('⭕️ ᴄʜᴀɴɴᴇʟ ⭕️', url='https://t.me/ds_movies1')
    ],[
        InlineKeyboardButton('Close ⚡️', callback_data='close'),
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/c2edac4a6cd119b61e9a9.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('⚜️ My Developer ⚜️', url='https://t.me/DS_KUNJAVA')
    ],[
        InlineKeyboardButton('🔰 ɢʀᴏᴜᴘ 🔰', url ='https://t.me/movie_house2'),
        InlineKeyboardButton('⭕️ ᴄʜᴀɴɴᴇʟ ⭕️', url='https://t.me/ds_movies1')
    ],[
        InlineKeyboardButton('Home 🏠', callback_data='start'),
        InlineKeyboardButton('About 🌀', callback_data='about')
    ],[
        InlineKeyboardButton('Close ⚡️', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('⚡️ Support ⚡️', url ='https://t.me/movie_house2')
    ],[
        InlineKeyboardButton('Home 🏠', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
