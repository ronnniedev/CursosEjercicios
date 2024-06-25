#include <iostream>
#include <string>

int main() {
	int numeroCuatroC; //El número entero a leer.
	/* Variables para obtener las cifras*/
	int c1, c2, c3, c4;

	//Pedir ingreso de valor al usuario
	std::cout << "Ingresa un entero de 4 cifras: ";
	std::cin >> numeroCuatroC;

	/*Vamos a obtener cociente y resto paso a paso para descomponer un numero.*/

	c1 = numeroCuatroC %10;
	numeroCuatroC = numeroCuatroC / 10;
	c2 = numeroCuatroC % 10;
	numeroCuatroC = numeroCuatroC / 10;
	c3 = numeroCuatroC % 10;
	numeroCuatroC = numeroCuatroC / 10;
	c4 = numeroCuatroC % 10;
	numeroCuatroC = numeroCuatroC / 10;

	std::cout << c1 << c2 << c3 << c4;


}