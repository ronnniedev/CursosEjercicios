package principal;

import java.util.Scanner;

public class CalculosPrincipal {
    
    public static void main (String args[]){
        Scanner consola = new Scanner(System.in);
        double valor;
        double suma;
        
        System.out.print("Ingresa valor 1: ");
        suma = consola.nextDouble();
        consola.nextLine();
        
        System.out.print("Ingresa valor 2: ");
        valor = consola.nextDouble();
        consola.nextLine();
        suma = suma + valor;
        
        System.out.print("Ingresa valor 3: ");
        valor = consola.nextDouble();
        consola.nextLine();
        suma = suma + valor;
        
        System.out.printf("El area sera: %.2f", suma/3);
        
    }
}
