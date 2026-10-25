import logging, os

LOG_CAMINHO = os.path.join(os.path.dirname(__file__), 'Pasta_teste', 'Log_file.log')

def criar_log():
    return logging.basicConfig(filename=LOG_CAMINHO, encoding='utf8', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
