# Makefile para o projeto Mandelbrot com Python e C

# Compilador e flags
CC = gcc
CFLAGS = -Wall -fPIC -O3

# Arquivos C
C_SOURCE = C/mandelbrot.c
C_HEADER = C/mandelbrot.h
SHARED_LIB = C/libmandelbrot.so

# Script Python
PY_SCRIPT = Python/main.py

# Alvo padrão: compila tudo
all: build

# Alvo para compilar a biblioteca compartilhada em C
build: $(SHARED_LIB)

$(SHARED_LIB): $(C_SOURCE) $(C_HEADER)
	@echo "Compilando a biblioteca em C..."
	$(CC) $(CFLAGS) -shared -o $@ $<
	@echo "Biblioteca $(SHARED_LIB) criada com sucesso."

# Alvo para executar o caso de estudo (a aplicação principal)
run:
	@echo "Executando a aplicação gráfica..."
	python3 $(PY_SCRIPT)

# Alvo para limpar os arquivos gerados
clean:
	@echo "Limpando arquivos compilados..."
	rm -f $(SHARED_LIB)
	rm -rf Python/__pycache__

.PHONY: all build run clean
