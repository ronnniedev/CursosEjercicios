#include <iostream>
#include <string>
/*
int main() {
	using namespace std; //con esto ya no es necesario escribir std todo el rato

	const float PI = 3.14;
	float radio;
	float largo;
	float ancho;
	char opcion;
	bool hayError;

	cout << "Elige una opcion: \n\n"
		<< "a) Perimetro de rectangulo\n"
		<< "b) Area de rectangulo\n"
		<< "c) Perimetro de circunferencia \n"
		<< "d) Area de circunferencia\n\n"
		<< "x) SALIR\n\n"
		<< ">> ";

	cin >> opcion;

	switch (opcion) {
		case 'a':
		case 'A':
			cout << "Largo= ";
			cin >> largo;

			if(largo <= 0) {
				hayError = true;
			}
			else {
				hayError = false;
			}

			if (hayError) {
				cout << "ERROR: Ingresa un valor mayor que 0.";
				break;
			}
			else {
				cout << "Ancho =";
				cin >> ancho;

				hayError = ancho <= 0;

				cout << "Perimetro= " << largo * 2 + ancho * 2;
			}

			break;
		case 'b':
		case 'B':
			cout << "Largo= ";
			cin >> largo;
			cout << "Ancho =";
			cin >> ancho;

			if (largo <= 0 || ancho <= 0) {
				hayError = true;
			}
			else {
				hayError = false;
			}

			if (hayError) {
				cout << "ERROR: Ingresa un valor mayor que 0.";
				break;
			}
			else {
				cout << "Area= " << largo * ancho;
			}

			break;
		case 'c':
		case 'C':
			cout << "Radio: ";
			cin >> radio;

			if (radio < 0) {
				cout << "ERROR: Ingresa un error menor que 0";
			}
			else {
				cout << "Perimetro: " << radio * PI;
			}
			break;
		case 'd':
		case 'D':
			cout << "Radio: ";
			cin >> radio;
			if (radio < 0) {
				cout << "ERROR: Ingresa un error menor que 0";
			}
			else {
				cout << "Area: " << radio * radio * PI;
			}
			break;
		case 'x':
		case 'X':
			return 0;
		default:
			cout << "ERROR: ingresa una opcion valida";
			break;

	}

	return 0;
}

*/

