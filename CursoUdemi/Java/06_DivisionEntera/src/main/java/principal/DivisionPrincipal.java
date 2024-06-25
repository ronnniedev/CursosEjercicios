package principal;

import java.util.Scanner;


public class DivisionPrincipal {
    
    public static void main (String args[]){
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Ingresame un numero de 4 cifras");
        int numero = keyboard.nextInt();
        
        // Nos aseguramos que el tamaño de las cifras sea 4
        
        while (numero >999999 || numero < 100000){
            System.out.println("Es necesario que el numero tenga 4 cifras: ");
            numero = keyboard.nextInt();
        }
        
        int suma = numero %10;
        suma = suma + (numero/10)%10;
        suma = suma + (numero/100)%10;
        suma = suma + (numero/1000)%10;
        suma = suma + (numero/10000)%10;
        suma = suma + numero/100000;
        
        System.out.println("La suma dara resultado como " + suma);
        
        
        
    }
}
