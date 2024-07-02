package principal;

import java.util.Scanner;

public class principal {
   public static void main(String args[]){
       Scanner keyboard = new Scanner (System.in);
       
        int numeroAAdivinar = (int)((Math.random()*100)+1);
        System.out.println(numeroAAdivinar);
        int cantidadIntentos = 5;
        boolean adivinado = false;

        for (int i = 1; i <= cantidadIntentos && !adivinado; i++) {
	System.out.println("Ingresa el valor ("  + (cantidadIntentos - i +1) + " intentos):\n");
	int numero = keyboard.nextInt();

	if (numero == numeroAAdivinar){
		System.out.println("Ganaste");
		adivinado = true;
	}
    }

        if (!adivinado) {
            System.out.println("Perdiste");
        }
       
       
   } 
}
