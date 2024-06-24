#include <iostream>
#include <string>

int main() {
	int largo;
	int ancho;
	int perimetro;
	int area;

	std::cout << "Dame largo del rectangulo: " << std::endl;
	std::cin >> largo;
	std::cout << "Dame el ancho del rectangulo: " << std::endl;
	std::cin >> ancho;

	perimetro = largo * 2 + ancho * 2;
	area = largo * ancho;

	std::cout << "El perimetro del rectangulo es " << perimetro << std::endl;
	std::cout << "El area del rectangulo es " << area << std::endl;

}