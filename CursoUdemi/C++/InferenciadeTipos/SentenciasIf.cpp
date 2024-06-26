#include <iostream>
#include <string>

int main() {
	using namespace std; //con esto ya no es necesario escribir std todo el rato

	int edad;

	cout << "Ingresa tu edad: ";
	cin >> edad;

	if (edad < 40) {
	
		cout << "Eres muy joven.\n";
		cout << "Tienes mucho por vivir\n";

	}
	else {
		cout << "Eres veterano.\n";
		cout << "Tienes mucho por vivir aun\n";
	}
		
	

	cout << "Gracias por compartir tu edad.";
}