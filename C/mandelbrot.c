#include "mandelbrot.h"
#include <math.h>

// Função principal exportada para a biblioteca.
void calculate_mandelbrot(int width, int height, int max_iter, unsigned char* data) {
    // Itera por cada pixel da imagem
    for (int py = 0; py < height; py++) {
        for (int px = 0; px < width; px++) {
            // Mapeia as coordenadas do pixel para o plano complexo
            double x0 = (px - width / 2.0) * 4.0 / width;
            double y0 = (py - height / 2.0) * 4.0 / height;

            double x = 0.0;
            double y = 0.0;

            int iteration = 0;
            // Loop principal do cálculo de Mandelbrot
            while (x * x + y * y <= 4.0 && iteration < max_iter) {
                double xtemp = x * x - y * y + x0;
                y = 2 * x * y + y0;
                x = xtemp;
                iteration++;
            }

            // Define a cor (em tons de cinza) baseada no número de iterações
            // O valor é escrito diretamente no buffer de dados passado pelo Python
            int color = (int)(255 * (iteration / (double)max_iter));
            data[py * width + px] = (unsigned char)(color < 255 ? color : 0);
        }
    }
}
