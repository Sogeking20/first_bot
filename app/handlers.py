from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums.dice_emoji import DiceEmoji
import time
import app.keyboard as kb




router = Router()

points = 10000

data = {}



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Выбери, что тебе нужно", reply_markup=kb.main)



@router.callback_query(F.data == 'game')
async def games(callback: CallbackQuery):
    await callback.answer('Вы выбрали игры')
    await callback.message.edit_text('В какую игру хочешь сыграть?', reply_markup=kb.games)



@router.callback_query(F.data == 'score')
async def games(callback: CallbackQuery):
    await callback.answer('Вы выбрали счёт')
    await callback.message.edit_text(f'Ваш счёт: {points}', reply_markup=kb.games)



@router.callback_query(F.data == 'dice')
async def play_dice(callback: CallbackQuery):
    await callback.message.edit_text(f"Выберите ставку, ваш счёт: {points}", reply_markup=kb.bet)



@router.callback_query(F.data == 'bet_10')
@router.callback_query(F.data == 'replay_10')
async def play_dice_10(callback: CallbackQuery):
    global points
    print(type(points))
    if points >= 10:
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        time.sleep(3)
        if x.dice.value == 6:
            points += 10
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_10)
        else:
            points -= 10
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_10)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)


@router.callback_query(F.data == 'bet_50')
@router.callback_query(F.data == 'replay_50')
async def play_dice_50(callback: CallbackQuery):
    global points
    time.sleep(3)
    if points >= 50:
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        if x.dice.value == 6:
            points += 50
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_50)
        else:
            points -= 50
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_50)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)


@router.callback_query(F.data == 'bet_100')
@router.callback_query(F.data == 'replay_100')
async def play_dice_100(callback: CallbackQuery):
    global points
    time.sleep(3)
    if points >= 100:
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        if x.dice.value == 6:
            points += 100
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_100)
        else:
            points -= 100
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_100)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)


@router.callback_query(F.data == 'bet_500')
@router.callback_query(F.data == 'replay_500')
async def play_dice_500(callback: CallbackQuery):
    global points
    time.sleep(3)
    if points >= 500:
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        if x.dice.value == 6:
            points += 500
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_500)
        else:
            points -= 500
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_500)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)


@router.callback_query(F.data == 'bet_1000')
@router.callback_query(F.data == 'replay_1000')
async def play_dice_1000(callback: CallbackQuery):
    global points
    time.sleep(3)
    if points >= 1000:   
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        if x.dice.value == 6:
            points += 1000
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_1000)
        else:
            points -= 1000
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_1000)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)


@router.callback_query(F.data == 'bet_5000')
@router.callback_query(F.data == 'replay_5000')
async def play_dice_5000(callback: CallbackQuery):
    global points
    time.sleep(3)
    if points >= 5000:
        x = await callback.message.answer_dice(DiceEmoji.DICE)
        if x.dice.value == 6:
            points += 5000
            await callback.message.answer(f"Победа! Ваш счёт: {points}", reply_markup=kb.replay_game_5000)
        else:
            points -= 5000
            await callback.message.answer(f"Проигрыш. Ваш счёт: {points}", reply_markup=kb.replay_game_5000)
    else:
        await callback.message.answer(f"У вас недостаточно средств", reply_markup=kb.no_money)




@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text("Ты вернулся назад", reply_markup=kb.main)



@router.callback_query(F.data == 'back_game')
async def back_game(callback: CallbackQuery):
    await callback.answer('Вы вернулись назад')
    await callback.message.edit_text('В какую игру хочешь сыграть?', reply_markup=kb.games)



@router.message()
async def cmd_start(message: Message):
    await message.answer("Я вас не понимаю. Выберите что-то из меню", reply_markup=kb.main)
