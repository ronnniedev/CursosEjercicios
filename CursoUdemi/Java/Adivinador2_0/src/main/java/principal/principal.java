package principal;
import java.util.Scanner;


public class principal {
    public static void main (String args[]){
        Scanner keyboard = new Scanner (System.in);
        int numeroSecreto = (int)(Math.random()*100)+1;
        final int MAX_INTENTOS = 10;
        boolean adivinado = false;
        System.out.println("Adivinador 2.0 - Dispones de " + MAX_INTENTOS 
                                + " para adivinar.");
        for(int i = 1; i <= MAX_INTENTOS && !adivinado;i++){
            
            System.out.println("Intento " + i + ":");
            int numero = keyboard.nextInt();
            
            if(numero == numeroSecreto){
                System.out.println("Ganaste");
                adivinado = true;
            }
            
            if (numero < numeroSecreto && !adivinado && i != MAX_INTENTOS){
                System.out.println("El numero a adivinar es mayor");
            }else if (!adivinado && i != MAX_INTENTOS){
                System.out.println("El numero a adivinar es menor");
            }
        }
        
        if(!adivinado){
            System.out.println("Perdiste\nEl numero era el "+ numeroSecreto);
        }
    }
}
