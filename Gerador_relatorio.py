import logging, os

def criar_log(pasta_destino: str):
    LOG_CAMINHO = os.path.join(os.path.dirname(__file__), f'{pasta_destino}', 'Log_file.log')
    return logging.basicConfig(filename=LOG_CAMINHO, encoding='utf8', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
