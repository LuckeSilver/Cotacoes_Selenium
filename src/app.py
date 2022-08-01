from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from simple_chalk import chalk

#Abre o navegador
navegador = webdriver.Chrome()

#Acessa o site que eu quiser
navegador.get('https://www.google.com/')
input_pesquisa_google = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
xpath_dolar = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

#Pesquisando no google  e pegando cotação do dólar
navegador.find_element('xpath', f'{input_pesquisa_google}').send_keys('Cotação dólar')
navegador.find_element('xpath', f'{input_pesquisa_google}').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', f'{xpath_dolar}').get_attribute('data-value')
print(chalk.green(f'Cotação dolar hoje: R${cotacao_dolar}'))

#Entrando no site melhor cambio e pegando cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
print(chalk.yellow(f'Cotação ouro hoje: R${cotacao_ouro}'))
print(chalk.green('Programa finalizado com Sucesso!'))
navegador.close()