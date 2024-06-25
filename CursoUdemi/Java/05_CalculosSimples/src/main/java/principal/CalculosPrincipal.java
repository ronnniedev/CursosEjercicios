package principal;

import java.util.Scanner;

public class CalculosPrincipal {
    
    public static void main (String args[]){
        Scanner consola = new Scanner(System.in);
        final double PI = 3.141592; // CONSTANTES FINALES
        double radio;
        double perimetro;
        double area;
        
        System.out.println("Ingresa el radio: ");
        radio = consola.nextDouble();
        consola.nextLine();
        
        perimetro = (radio*2)*PI;
        area = radio*radio*PI;
        
        System.out.println("P= "+ perimetro+" A= "+area);
                
          
        
    }
}
