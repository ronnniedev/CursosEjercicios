#include <iostream>
#include <string>

int main() {
	int base;
	int altura;
	float area;

	std::cout << "Ingresa la base y la altura: ";
	std::cin >> base >> altura;

	area = (float)(base * altura) / 2; // casteo en C++

	std::cout << "Area = " << area;

}