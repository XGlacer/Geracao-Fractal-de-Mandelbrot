# Projeto: Fractal de Mandelbrot com Python e C

Este projeto foi desenvolvido para a disciplina de Conceitos de Linguagens de Programação e implementa a geração do fractal de Mandelbrot utilizando uma arquitetura de duas linguagens, conforme especificado no trabalho.

- **Python:** Utilizado para a criação da interface gráfica (GUI), gerenciamento do programa e exibição da imagem final.
- **C:** Utilizado como um serviço de cálculo de alta performance, implementado como uma biblioteca compartilhada (`shared library`) para realizar o processamento numérico intensivo do fractal.

## Arquivos do Repositório

O repositório está estruturado da seguinte forma:
├── C/
│   ├── mandelbrot.c      # Código-fonte em C que calcula o fractal
│   └── mandelbrot.h      # Arquivo de cabeçalho para a função em C
├── Python/
│   └── main.py           # Script Python principal que gera a UI e chama a biblioteca C
├── Makefile              # Automatiza a compilação e execução do projeto
├── README.md             # Este arquivo
└── Documentacao_Implementacao.pdf # Documento explicando a arquitetura

## Pré-requisitos

Para compilar e executar este projeto, você precisará ter os seguintes softwares instalados:

- `gcc`: Compilador para a linguagem C.
- `make`: Ferramenta para automação da compilação.
- `python3`: Interpretador Python (versão 3.6 ou superior).
- Bibliotecas Python: `Pillow` e `Tkinter` (geralmente incluído na instalação padrão do Python).

Para instalar os pré-requisitos em um sistema baseado em Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-tk
pip3 install Pillow
