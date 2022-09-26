from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chaves import sari, api_key
from selenium import webdriver
from botTelegram import *

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

    # chave_captcha = browser.find_element(By.ID,'Captcha').get_attribute('data-sitekey')


    def capatcha():        
        solver = recaptchaV2Proxyless()
        # VERBOSE = 1 --RETORNA RESPOSTA DO CAPTCHA
        solver.set_verbose(1)
        solver.set_key(api_key)
        solver.set_website_url(get_url)
        # solver.set_website_key(chave_captcha)

        resposta = solver.solve_and_return_solution()

        if resposta != 0:
            time.sleep(1)
            browser.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
            browser.find_element(By.ID, 'enviar').click()
        else:
            print(solver.err_string)

    # capatcha()

    browser.close()
    msg = 'Agendado com sucesso!!!'
    return msg