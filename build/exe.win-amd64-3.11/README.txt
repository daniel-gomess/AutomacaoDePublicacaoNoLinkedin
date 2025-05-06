🤖 Automação de Publicações no LinkedIn com Python e Selenium
Este script em Python utiliza a biblioteca Selenium para automatizar o processo completo de login, criação, agendamento e postagem de um conteúdo no LinkedIn, incluindo a anexação de um vídeo.

📌 Funcionalidades
Abertura do navegador com configurações personalizadas (idioma, tamanho, modo anônimo).

Login automatizado com digitação humanizada.

Preenchimento automático do campo de texto para a publicação.

Upload de vídeo local diretamente na publicação.

Agendamento da postagem para data e hora específicas.

Execução de cliques e interações como se fossem feitas manualmente.

⚙️ Requisitos
Python 3.7+

Google Chrome instalado

Instalar dependências com:
pip install selenium webdriver-manager pyperclip pyautogui


🧠 Bibliotecas Utilizadas
selenium: automação do navegador

webdriver_manager: gerenciamento automático do driver do Chrome

pyautogui: controle do teclado para preenchimento de campos difíceis

pyperclip: manipulação da área de transferência (clipboard)

random, time: delays e variações para tornar a interação mais natural

📝 Como Usar
Edite os campos abaixo com suas informações:

E-mail e senha do LinkedIn

Caminho do vídeo local

Texto da publicação

Data e hora do agendamento

Execute o script com:
python linkedin_automation.py


O navegador abrirá e o processo será executado automaticamente.

⚠️ Importante: este script foi feito para fins educacionais e pode parar de funcionar se o LinkedIn alterar sua estrutura interna. Use com responsabilidade e evite violações dos termos de uso da plataforma.