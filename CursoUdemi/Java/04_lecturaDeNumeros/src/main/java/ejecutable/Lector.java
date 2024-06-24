package ejecutable;
import java.util.Scanner;

public class Lector {
  
    public static void main (String args[]){
        String nombrePersona;
        String nombrePersonaDos;
        String nombrePersonaTres;
        int edadPersona;
        int edadPersonaDos;
        int edadPersonaTres;
        
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Ingresa tu nombre: ");
        nombrePersona = keyboard.nextLine();
        
        System.out.println("Ingresa tu edad: ");
        edadPersona = keyboard.nextInt();
        keyboard.nextLine();
        
        System.out.println("Ingresa otro nombre: ");
        nombrePersonaDos = keyboard.nextLine();
        
        System.out.println("Ingresa otra edad: ");
        edadPersonaDos = keyboard.nextInt();
        keyboard.nextLine();
        
        
        System.out.println("Ingresa otro nombre: ");
        nombrePersonaTres = keyboard.nextLine();
        
        System.out.println("Ingresa otra edad: ");
        edadPersonaTres = keyboard.nextInt();
        keyboard.nextLine();
       
        System.out.println("Hola " + nombrePersona + " es un gusto conocerte a "
                            + "tus "+ edadPersona + " años.");
        System.out.println("Hola " + nombrePersonaDos + " es un gusto conocerte a "
                            + "tus "+ edadPersonaDos + " años.");
        System.out.println("Hola " + nombrePersonaTres + " es un gusto conocerte a "
                            + "tus "+ edadPersonaTres + " años.");
        
    }
}
