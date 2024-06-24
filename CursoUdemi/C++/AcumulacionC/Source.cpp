#include <iostream>
#include <string>

int main() {
	int puntos = 0;
	int puntosMoneda;

	std::cout << "Ingresa los puntos a sumar" << std::endl;
	std::cin >> puntos;
	
	std::cout << "Ingresa los puntos a sumar" << std::endl;
	std::cin >> puntosMoneda;
	puntos = puntos + puntosMoneda;

	std::cout << "Ingresa los puntos a sumar" << std::endl;
	std::cin >> puntosMoneda;
	puntos = puntos + puntosMoneda;

	std::cout << "puntos= " << puntos << " - puntosMoneda= " << puntosMoneda;

}