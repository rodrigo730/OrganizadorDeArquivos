import os 
import shutil
import Organizador_diretorio 

extensoes = Organizador_diretorio.Pasta_extensao

# print(extensoes.CODIGOS.value)
PASTA_PRINCIPAL = os.path.abspath(os.path.dirname(__file__))
PASTA_TESTE = os.path.join(PASTA_PRINCIPAL, 'Pasta_teste')
print(PASTA_PRINCIPAL)

for pasta, subpasta, arquivo in os.walk(PASTA_TESTE):
    for x in arquivo:
        nome, extensao = os.path.splitext(x)
        for categorias in extensoes:
            if extensao.lower() in categorias.value:
                caminho_nova_pasta = os.path.join(PASTA_TESTE, f'{categorias.name}')
                DOCUMENTS_PASTA = os.makedirs(caminho_nova_pasta, exist_ok=True)
                arquivo_pasta_raiz = os.path.join(pasta, x)
                ARQUIVO_PASTA = os.path.join(caminho_nova_pasta, x)
                if os.path.exists(ARQUIVO_PASTA):
                    if os.path.exists(os.path.join(PASTA_TESTE,x)):
                        os.unlink(os.path.join(PASTA_TESTE,x))
                    elif os.path.exists(os.path.join(PASTA_TESTE,x)):
                        continue
                    continue
                else:
                    print('Arquivo movido')
                    shutil.move(arquivo_pasta_raiz, caminho_nova_pasta)
