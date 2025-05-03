from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import pyperclip
import pyautogui

def iniciar_driver():
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'C:\\Users\\daani\\OneDrive\\Desktop\\Daniel\\Projetos\\Mestre Python\\Automatização\\Selenium\\Nova pasta',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    return driver

def digitar_email(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(0.05)

def digitar_senha(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(0.05)

def digitar_publicacao(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(0.05)

def digitar_data_agendamento(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(0.05)

def digitar_hora_agendamento(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(0.05)


email = 'email@email.com' # informe seu e-mail
senha = 'senha123' # informe sua senha

# Altere o texto da publicação como desejar
texto_puclicacao = '''ESSA PUBLICAÇÃO FOI TODA FEITA DE FORMA AUTOMATIZADA!!!

Sim, você leu certo. Cada palavra que você está lendo agora foi gerada automaticamente por um script em Python — sem precisar abrir o editor de texto ou sequer digitar manualmente. Isso mostra, na prática, como a programação pode transformar tarefas comuns do dia a dia em processos rápidos, inteligentes e escaláveis.

Python é uma das linguagens mais poderosas e acessíveis para quem quer começar a automatizar processos. Com poucas linhas de código, é possível criar scripts que escrevem relatórios, enviam e-mails, organizam dados, atualizam dashboards e, como você pode ver aqui, até publicam conteúdo com uma estrutura bem pensada e envolvente.

A automatização não é só sobre economizar tempo — é sobre liberar espaço mental para focar no que realmente importa: análise, estratégia e criatividade. Quando tarefas repetitivas deixam de consumir suas horas mais produtivas, você começa a perceber o verdadeiro valor do seu tempo.

Se você ainda não começou a explorar o poder da automação com Python, talvez seja a hora de repensar como tem investido seus esforços. A tecnologia está aí para ser sua aliada — e o primeiro passo pode ser mais simples do que você imagina.

@Jhonatan de Souz
@Dev Aprende

OBS: Além de todo o processo ser automatizado, a publicação também foi. Pois todo o processo foi feito hoje (03/05) pela manhã (10:10h) e agendado para ser publicado hoje às 12:00!!!

#Python #automacao #automacaopython #automacaodetarefas #dev #desenvolvedor #automation #pythonautomation'''

data_agendamento = '3/5/2025'
hora_agendamento = '12:00'

driver = iniciar_driver()
# Navegar até o site do LinkedIn
driver.get('https://www.linkedin.com/login')
sleep(1.5)
# Maximizar a janela do navegador
driver.maximize_window()
sleep(1.5)
# Achar o campo de e-mail e inserir o e-mail
campo_email = driver.find_element(By.ID, 'username')
sleep(1)
digitar_email(email, campo_email)

# Achar o campo de e-mail e inserir o e-mail
campo_senha = driver.find_element(By.ID, 'password')
sleep(1)
digitar_senha(senha, campo_senha)
sleep(1)

# Clicar no botão de entrar
botao_entrar = driver.find_element(By.XPATH, "//*[@class='btn__primary--large from__button--floating']")
driver.execute_script("arguments[0].click();", botao_entrar)
sleep(12)

# Achar e clicar no campo de criar nova publicação
criar_publicacao = driver.find_element(By.ID, 'ember44')
driver.execute_script("arguments[0].click();", criar_publicacao)
sleep(2)

# Digitar o texto da publicação
campo_da_publicacao = driver.find_element(By.XPATH, "//*[@role='textbox']")
digitar_publicacao(texto_puclicacao, campo_da_publicacao)
sleep(7)

# Anexando video
buscar_video = driver.find_element(By.XPATH, "//button[@aria-label='Adicione um vídeo' and @data-view-name='hiring-growth-member-sharebox']").click()
sleep(5)

try:
    buscar_video = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))  # Ajuste o seletor conforme necessário
    )
    # Caminho para o arquivo local
    buscar_video.send_keys(r'C:\desktop.....mp4') # informe o caminho do arquivo no seu computador e a extensão
except Exception as e:
    print("❌ Erro ao encontrar ou usar o campo de upload:", e)

sleep(5)
botao_avancar = driver.find_element(By.XPATH, '//button[@aria-label="Avançar"]').click()
sleep(2)

# Clicando no botão de Agendar publicação
driver.find_element(By.XPATH, '//button[@aria-label="Agendar publicação"]').click()
sleep(2)

# Agendando publicação para 10:00 do dia 03/05/2024
campo_data = driver.find_element(By.XPATH, '//input[@class=" artdeco-text-input--input" and @id="share-post__scheduled-date"]')
campo_data.click()
sleep(1)
campo_data.click()
sleep(1)
pyautogui.hotkey('ctrl', 'a')
sleep(0.5)
digitar_data_agendamento(data_agendamento, campo_data)
sleep(1)
campo_hora = driver.find_element(By.CLASS_NAME, 'artdeco-typeahead__input ')
campo_hora.click()
sleep(0.5)
campo_hora.click()
sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
sleep(0.5)
digitar_hora_agendamento(hora_agendamento, campo_hora)
sleep(1.5)
botao_avancar = driver.find_element(By.XPATH, '//button[@aria-label="Avançar"]')
botao_avancar.click()
sleep(1)
botao_avancar = driver.find_element(By.XPATH, '//button[@aria-label="Avançar"]')
botao_avancar.click()
sleep(1)

# Clicar em "Agendar"
botao_publicar = driver.find_element(By.XPATH, '//button[@class="share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()
# driver.execute_script("arguments[0].click();", botao_publicar)
sleep(5)


input('')