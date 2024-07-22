import asyncio 
from aiogram import Bot, Dispatcher

from app.handlers import router

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token='7080196246:AAE4k96geDcFdRDSjyGqjpVmCwdu0lHCMG0') 
dp = Dispatcher()

dp.include_router(router)




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())