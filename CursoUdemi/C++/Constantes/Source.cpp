#include <iostream>
#include <string>

int main() {
	const int IVA = 22;
	float precioProducto;
	float calculoIva;
	float precioFinal;

	std::cout << "Ingresa el precio sin IVA: ";
	std::cin >> precioProducto;
	
	calculoIva = precioProducto * (float)IVA/100; // son buenas practicas castear una variable en el mismo tipo que el resultado
	precioFinal = precioProducto + calculoIva;

	std::cout << "Valor inicial $" << precioProducto << " IVA $" << calculoIva << " Final $" << precioFinal << std::endl;

}