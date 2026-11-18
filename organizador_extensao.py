import  aenum
import enum
import pathlib 
import json

PATH = pathlib.Path(__file__).parent / 'extensoes.json'


class Pasta_extensao(enum.Enum):
    ...
    # Valores padrão 
    # IMAGENS = '.png', '.jpg', '.jpeg', '.gif'
    # DOCUMENTOS = '.pdf', '.docx', '.txt', '.xlsx' 
    # EXECUTAVEIS = '.exe', '.msi' 
    # CODIGOS = '.py', '.js', '.html', '.css'

teste = None
with open(PATH, 'r', encoding='utf8') as a:
    teste = json.load(a)
for x in teste.items():
    chave, valor = x
    aenum.extend_enum(Pasta_extensao, chave, *valor)
    # print(chave, valor)

# print(dict_)

def creating_extension(value, *args):
    resposta_formatada = value.replace(' ', '_').upper()
    if resposta_formatada in Pasta_extensao.__members__:
                    return None
    aenum.extend_enum(Pasta_extensao,
                    f'{resposta_formatada}', 
                    args
                    )
    valor = {x.name: x.value for x in Pasta_extensao}
    with open(PATH, 'w',encoding='utf8') as a:
        json.dump(valor, a,indent=2)
    return valor

print([x.name for x in Pasta_extensao])