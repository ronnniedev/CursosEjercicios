#include <iostream>
#include <string> // llamamos a la libreria de variables tipo stream

int main() {
	std::string nombre;
	int edad;
	std::string nombreDos;
	int edadDos;

	std::cout << "Escribe tu nombre: ";
	std::cin >> nombre;
	std::cout << "Dime tu edad: ";
	std::cin >> edad;
	std::cout << "Escribe El nombre de tu pariente: ";
	std::cin >> nombreDos;
	std::cout << "Dime la edad de tu pariente: ";
	std::cin >> edadDos;

	std::cout << "Hola " << std::endl; 
	std::cout << nombre + ", es un gusto conocerte a tus ";
	std::cout << edad;
	std::cout << " años" << std::endl;
	std::cout << "Hola " << std::endl;
	std::cout << nombreDos + ", es un gusto conocerte a tus ";
	std::cout << edadDos;
	std::cout << " años" << std::endl;
	
}