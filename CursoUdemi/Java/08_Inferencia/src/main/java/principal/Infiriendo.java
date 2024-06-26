package principal;

import java.util.Scanner;


public class Infiriendo {
   public static void main (String args[]){
       var entrada = new Scanner(System.in);
       var frase = entrada.nextLine(); //con var el tipo de variable se asigna automaticamente
       
       System.out.println("La frase << " + frase + ">> es correcta.");
       
       var i = 10; 
   } 
}
