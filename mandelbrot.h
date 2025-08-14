#ifndef MANDELBROT_H
#define MANDELBROT_H

/*
 * Calcula o conjunto de Mandelbrot e preenche um buffer de dados de imagem.
 * Parâmetros:
 * - width: Largura da imagem em pixels.
 * - height: Altura da imagem em pixels.
 * - max_iter: Número máximo de iterações por pixel.
 * - data: Ponteiro para um array de unsigned char (1 byte por pixel) que receberá os dados da imagem em tons de cinza.
 */
void calculate_mandelbrot(int width, int height, int max_iter, unsigned char* data);

#endif //MANDELBROT_H
