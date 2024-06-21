package principal;

import java.util.Scanner;

public class principal {
   
    public static void main(String args[]){
        String nombre;
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Hola ingresa tu nombre: ");
        nombre = entrada.nextLine();
        
        System.out.println("Hola " + nombre);
        System.out.println("¿Como estas?");
    }
}
