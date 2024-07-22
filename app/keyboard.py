from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import sqlite3


conn = sqlite3.connect('new_bot.db')
cur = conn.cursor()


cur.execute('SELECT name FROM goods')
result = cur.fetchall()


def kb_goods():
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item[0]) for item in result]
    # for item in result:
    #     builder.button(text = item[0])
    builder.adjust(3)
    return builder.as_markup(resize_keyboard = True)


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Игры', callback_data='game')],
    [InlineKeyboardButton(text='Счёт', callback_data='score')]
])


games = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кости', callback_data='dice')],
    [InlineKeyboardButton(text= 'Назад', callback_data='back')]
])


replay_game_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_10')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


replay_game_50 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_50')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


replay_game_100 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_100')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


replay_game_500 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_500')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


replay_game_1000 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_1000')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


replay_game_5000 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть снова', callback_data='replay_5000')], [InlineKeyboardButton(text='Назад', callback_data='back_game')]
])


is_score =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть', callback_data='game')]])



no_money = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'Назад', callback_data='back')]
])


bet = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='10', callback_data='bet_10'), InlineKeyboardButton(text='50', callback_data='bet_50')],
    [InlineKeyboardButton(text='100', callback_data='bet_100'), InlineKeyboardButton(text='500', callback_data='bet_500')],
    [InlineKeyboardButton(text='1000', callback_data='bet_1000'), InlineKeyboardButton(text='5000', callback_data='bet_5000')]
])
