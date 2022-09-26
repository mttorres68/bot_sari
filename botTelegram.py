from telebot.async_telebot import AsyncTeleBot
from chaves import token_bot
from login import login
import asyncio

bot = AsyncTeleBot(token_bot)


@bot.message_handler(func=lambda m: True)
async def agendaralmoco(message):
    userName = message.text
    # bot.send_message(message.chat.id,'opa')
    Ra =  userName.split(" ")[0]
    Rj = userName.split(" ")[0]
    u = userName.split(" ")[1]
    s = userName.split(" ")[2]


    if Ra == 'Ra' and len(u) == 11 and len(s) == 10:
        await bot.send_message(message.chat.id,f'Reservar Almoço!\nUsuario: {u}\nSenha: {s}') 
        await login(message, u, s)
        msg = login()
        await bot.send_message(message.chat.id,f'ok{msg}')

    elif Rj == 'Rj' and len(u) == 11 and len(s) == 10:
        await bot.send_message(message.chat.id,f'Reservar Janta!\nUsuario: {u}\nSenha: {s}')
        # await login(message, u, s),
    else:
        await bot.send_message(message.chat.id,'PARAMETROS ERRADOS')


asyncio.run(bot.polling())




