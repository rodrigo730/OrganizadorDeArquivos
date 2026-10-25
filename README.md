# OrganizadorDeArquivos 

## 📌 Sobre o Projeto
 Automação em Python, modular e focado em manter pastas organizadas, limpas e livres de ficheiros duplicados.
 
---
[![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge&logo=git&logoColor=white)](https://github.com/rodrigo730/OrganizadorDeArquivos)
![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
---

## 🎯 O Problema
Dentre pastas de trabalho ou de transferências (`Downloads`) é um problema comum: centenas de arquivos desorganizados de vários tipos (imagens, documentos, instaladores) misturados, dificultando encontrar o que é importante facilmente.

## 💡 A Solução

O **OrganizadorDeArquivos** automatiza este processo de procura. Através de um script em Python, a ferramenta percorre diretórios recursivamente, categoriza os arquivos pelas respetivas extensões, move-os de forma segura para pastas dedicadas, trata duplicados e regista todas as ações num sistema de auditoria por logs.

---
## 🛠️ Arquitetura do Projeto

O projeto foi construído seguindo princípios estritos de **separação de responsabilidades** e código modular:

```text
OrganizadorDeArquivos/
│
├── Mover_arquivos.py        # Ponto de entrada (Controla o fluxo de execução e a varredura)
├── Organizador_diretorio.py # Mapeamento de diretótio e extensões 
└── Gerador_relatorio.py     # Criação e organização de informações do arquivo log
```

## 🚀 Como Executar 

## Pré-requisitos
Para executar o projeto você precisa da seguinte tecnologia:
- Python 3.x 
---
<h3>Clonando</h3>

```bash
git clone https://github.com/rodrigo730/OrganizadorDeArquivos.git
```
<h3>Iniciando</h3>

```bash
cd OrganizadorDeArquivos
python Mover_arquivos.py
```

## 🛠️ Tecnologias Utilizadas

- Python

- Bibliotecas: os / shutil / logging / Enum