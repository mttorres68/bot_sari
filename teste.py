from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.chrome.service import Service

from telebot.async_telebot import AsyncTeleBot
from selenium.webdriver.common.by import By
from selenium import webdriver
from telebot import types,util
from chaves import *
import datetime
import asyncio
import time

bot = AsyncTeleBot(token_bot)


async def login(message, u, s):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(sari)
    time.sleep(1)
    user = browser.find_element(By.ID, 'j_username')
    user.send_keys(u)
    time.sleep(1)
    psw = browser.find_element(By.ID,'j_password')
    psw.send_keys(s)
    time.sleep(1)
    # current_time = datetime.datetime.now()
    # print(current_time)

    browser.find_element(By.NAME,'j_idt6:j_idt26').click()
    time.sleep(1)

    browser.find_element(By.ID,'j_idt7:btnGerenciaMinhaConta').click()
    time.sleep(1)

    browser.find_element(By.ID,'j_idt7:btnCompraTicketUsuario').click()
    time.sleep(2)

    get_url = browser.current_url
    # print(get_url)

    chave_captcha = browser.find_element(By.ID,'Captcha').get_attribute('data-sitekey')


    def capatcha():        
        solver = recaptchaV2Proxyless()
        # VERBOSE = 1 --RETORNA RESPOSTA DO CAPTCHA
        solver.set_verbose(1)
        solver.set_key(api_key)
        solver.set_website_url(get_url)
        solver.set_website_key(chave_captcha)

        resposta = solver.solve_and_return_solution()

        if resposta != 0:
            time.sleep(1)
            browser.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
            browser.find_element(By.ID, 'enviar').click()
        else:
            print(solver.err_string)

    capatcha()

    browser.close()
    return await bot.send_message(message.chat.id,f'Agendado com sucesso!!!')


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
        # await login(message, u, s)

    elif Rj == 'Rj' and len(u) == 11 and len(s) == 10:
        await bot.send_message(message.chat.id,f'Reservar Janta!\nUsuario: {u}\nSenha: {s}')
        # await login(message, u, s),
    else:
        await bot.send_message(message.chat.id,'PARAMETROS ERRADOS')


asyncio.run(bot.polling())




