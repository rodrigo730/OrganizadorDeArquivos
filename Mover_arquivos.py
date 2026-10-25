import os 
import shutil
import Organizador_diretorio, Gerador_relatorio

caminho_usuario = input('Digite o caminho: ')
extensoes = Organizador_diretorio.Pasta_extensao
arquivo_log = Gerador_relatorio

PASTA_PRINCIPAL = os.path.abspath(os.path.dirname(caminho_usuario))
PASTA_NOVA = os.path.join(PASTA_PRINCIPAL, f'{caminho_usuario}')
arquivo_log.criar_log(PASTA_NOVA)
arquivo_log.logging.info("Inicio execução")

for pasta, subpasta, arquivo in os.walk(PASTA_NOVA):
    for x in arquivo:
        nome, extensao = os.path.splitext(x)
        for categorias in extensoes:
            if extensao.lower() in categorias.value:
                caminho_nova_pasta = os.path.join(PASTA_NOVA, f'{categorias.name}')
                DOCUMENTS_PASTA = os.makedirs(caminho_nova_pasta, exist_ok=True)
                arquivo_pasta_raiz = os.path.join(pasta, x)
                ARQUIVO_PASTA = os.path.join(caminho_nova_pasta, x)
                arquivo_log.criar_log(ARQUIVO_PASTA)
                if not os.path.exists(ARQUIVO_PASTA):
                    arquivo_log.logging.info(f"Caminhos Criados na Pasta{caminho_nova_pasta}")   
                if os.path.exists(ARQUIVO_PASTA):
                    if os.path.exists(os.path.join(PASTA_NOVA,x)):
                        arquivo_log.logging.warning("Arquivos duplicados, na pasta raiz")  
                        os.unlink(os.path.join(PASTA_NOVA,x))
                        arquivo_log.logging.warning("Arquivos duplicados, na pasta raiz com Sucesso!!")  
                    elif os.path.exists(os.path.join(PASTA_NOVA,x)):  
                        break
                    continue
                else:
                        print('Arquivo movido')
                        shutil.move(arquivo_pasta_raiz, caminho_nova_pasta)         
arquivo_log.logging.info("Fim da execução") 
