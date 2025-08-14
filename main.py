import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import os

# --- Configurações da Imagem ---
WIDTH, HEIGHT = 800, 600
MAX_ITER = 200

# --- Interface com a Biblioteca C via CTypes ---

# 1. Carregar a biblioteca compartilhada
lib_path = os.path.join(os.path.dirname(__file__), '..', 'C', 'libmandelbrot.so')
try:
    mandelbrot_lib = ctypes.CDLL(lib_path)
except OSError:
    print(f"Erro: Não foi possível carregar a biblioteca em '{lib_path}'.")
    print("Certifique-se de que o projeto foi compilado com 'make build'.")
    exit(1)


# 2. Definir a assinatura da função (argumentos e tipo de retorno)
# void calculate_mandelbrot(int, int, int, unsigned char*)
mandelbrot_lib.calculate_mandelbrot.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_ubyte)
]
mandelbrot_lib.calculate_mandelbrot.restype = None

# --- Geração da Imagem ---

# 3. Alocar um buffer de memória que será compartilhado com o C
# Este buffer conterá os dados brutos da imagem (pixels em tons de cinza)
buffer_size = WIDTH * HEIGHT
image_buffer = (ctypes.c_ubyte * buffer_size)()

print("Invocando a função C para calcular o fractal...")
# 4. Chamar a função C, passando o buffer para ser preenchido
mandelbrot_lib.calculate_mandelbrot(WIDTH, HEIGHT, MAX_ITER, image_buffer)
print("Cálculo concluído. Renderizando a imagem...")

# 5. Criar uma imagem a partir do buffer preenchido pela biblioteca C
# Usamos a biblioteca Pillow (PIL) para interpretar os bytes brutos
image = Image.frombytes('L', (WIDTH, HEIGHT), image_buffer)

# --- Interface Gráfica com Tkinter ---

# 6. Configurar a janela principal
root = tk.Tk()
root.title("Fractal de Mandelbrot (Python + C)")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

# 7. Converter a imagem do Pillow para um formato que o Tkinter possa exibir
tk_image = ImageTk.PhotoImage(image)

# 8. Exibir a imagem em um widget Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Iniciar o loop principal da aplicação gráfica
root.mainloop()
