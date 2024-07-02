#include <iostream>
#include <string>
#include <time.h>
#include <stdlib.h>

int main() {
	srand(time(0)); //funcion para randomizar numeros


	int numeroAAdivinar = rand() % 100 + 1;
	const int CANTIDAD_INTENTOS = 10;
	int numero;
	bool adivinado = false;
	std::cout << "Adivinador 2.0 - Dispones de " << CANTIDAD_INTENTOS << "para adivinar." << std::endl;

	for (int i = 1; i <= CANTIDAD_INTENTOS && !adivinado; i++) {
		std::cout << "Intento " << i << ":" << std::endl;
		std::cin >> numero;

		if (numero == numeroAAdivinar) {
			std::cout << "Ganaste";
			adivinado = true;
		}

		if (numero < numeroAAdivinar && i != CANTIDAD_INTENTOS && !adivinado) {
			std::cout << "El numero a adivinar es mayor" << std::endl;
		}
		else if (i != CANTIDAD_INTENTOS && !adivinado) {
			std::cout << "El numero a adivinar es menor" << std::endl;
		}
	}

	if (!adivinado) {
		std::cout << "Perdiste:" << std::endl << "El numero era el " << numeroAAdivinar << std::endl;
	}
	system("pause"); //pausamos a expectativas de que el usuario pulse una tecla

	return 0;
}