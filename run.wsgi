import sys
import os
from dotenv import load_dotenv

# Ajuste o caminho para o diretório do seu projeto
project_dir = '/var/www/html/listify'
sys.path.insert(0, project_dir)

# Carrega variáveis de ambiente
load_dotenv(os.path.join(project_dir, '.env'))

# Ativa o ambiente virtual (ajuste o caminho conforme necessário)
activate_this = '/var/www/html/listify/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import create_app
application = create_app()
