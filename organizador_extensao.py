import  aenum
import enum
import pathlib 
import json
import re

PATH = pathlib.Path(__file__).parent / 'extensoes.json'

teste = None
with open(PATH, 'r', encoding='utf8') as a:
    teste = json.load(a)

class Pasta_extensao(enum.Enum):
    ...
    # Standard values 
    # IMAGENS = '.png', '.jpg', '.jpeg', '.gif'
    # DOCUMENTOS = '.pdf', '.docx', '.txt', '.xlsx' 
    # EXECUTAVEIS = '.exe', '.msi' 
    # CODIGOS = '.py', '.js', '.html', '.css'


for x in teste.items():
    chave, valor = x
    aenum.extend_enum(Pasta_extensao, chave, tuple(valor))

def creating_extension(value, *args: str):
    teste = ' '.join(args)
    extensoes = re.findall(r'\.[a-zA-Z0-9]+', teste)
    resposta_formatada = value.replace(' ', '_').upper()
    if resposta_formatada in Pasta_extensao.__members__:
                    return False
    elif resposta_formatada in Pasta_extensao._member_names_:
        return False
    if len(extensoes) == 1 :
        aenum.extend_enum(Pasta_extensao,
                            f'{resposta_formatada}', 
                            tuple(extensoes)
                            )
    else:
        aenum.extend_enum(Pasta_extensao,
                        f'{resposta_formatada}', 
                        *extensoes
                        )
    valor = {x.name: x.value for x in Pasta_extensao}
    with open(PATH, 'w',encoding='utf8') as a:
            json.dump(valor, a,indent=2)
    return valor

if __name__ == '__main__':
    ...