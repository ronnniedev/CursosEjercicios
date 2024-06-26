package principal;

import java.util.Scanner;


public class SentenciasIf {
    
    public static void main (String args[]){
        
        
        Scanner keyboard = new Scanner (System.in);
        System.out.println("Ingresa tu edad: ");
        int edad = keyboard.nextInt();
        keyboard.nextLine();
        /*
        Cadena de ifs para la introduccion de edad
        */
        if(edad == 40){ 
            System.out.println("Tienes 40 años");
        }else if (edad > 40) {
            System.out.println("Eres viejo");
        }else {
            System.out.println("Eres muy joven");
        }
        
        
    }
}
