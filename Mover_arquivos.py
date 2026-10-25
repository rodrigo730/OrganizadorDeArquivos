import os 
import shutil
import Organizador_diretorio, Gerador_relatorio

extensoes = Organizador_diretorio.Pasta_extensao
arquivo_log = Gerador_relatorio
arquivo_log.criar_log()
# print(extensoes.CODIGOS.value)
PASTA_PRINCIPAL = os.path.abspath(os.path.dirname(__file__))
PASTA_TESTE = os.path.join(PASTA_PRINCIPAL, 'Pasta_teste')
print(PASTA_PRINCIPAL)
arquivo_log.logging.info("Inicio execução")
for pasta, subpasta, arquivo in os.walk(PASTA_TESTE):
    for x in arquivo:
        nome, extensao = os.path.splitext(x)
        for categorias in extensoes:
            if extensao.lower() in categorias.value:
                caminho_nova_pasta = os.path.join(PASTA_TESTE, f'{categorias.name}')
                DOCUMENTS_PASTA = os.makedirs(caminho_nova_pasta, exist_ok=True)
                arquivo_pasta_raiz = os.path.join(pasta, x)
                ARQUIVO_PASTA = os.path.join(caminho_nova_pasta, x)
                if not os.path.exists(ARQUIVO_PASTA):
                    arquivo_log.logging.info("Caminhos Criados")   
                if os.path.exists(ARQUIVO_PASTA):
                    if os.path.exists(os.path.join(PASTA_TESTE,x)):
                        arquivo_log.logging.warning("Arquivos duplicados, na pasta raiz")   
                        os.unlink(os.path.join(PASTA_TESTE,x))
                        arquivo_log.logging.warning("Arquivos duplicados, na pasta raiz com Sucesso!!")   
                    elif os.path.exists(os.path.join(PASTA_TESTE,x)):  
                        continue
                    continue
                else:
                    print('Arquivo movido')
                    shutil.move(arquivo_pasta_raiz, caminho_nova_pasta)         
arquivo_log.logging.info("Fim da execução")
