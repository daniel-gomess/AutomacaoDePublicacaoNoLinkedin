import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final. Se houver mais arquivos, adicione-os aqui, informando o nome e a extensão.
arquivos = ['README.txt']
# Saida de arquivos
configuracao = Executable(
    script='app.py',
    icon='linkedin.ico' # Coloque o nome do seu ícone aqui, se não houver, deixe vazio
)
# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatiza a postagem de uma publicação no LinkedIn.',
    author='Daniel Augusto Gomes',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)