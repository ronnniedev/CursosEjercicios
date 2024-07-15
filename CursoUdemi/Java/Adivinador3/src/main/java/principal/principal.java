package principal;

import java.util.Scanner;

public class principal {
  
    public static void main(String args[]){
    
      Scanner keyboard = new Scanner(System.in); 
      boolean adivinado = false;
      
      System.out.println("Intentare adivinar un numero que tu elijas.");
      System.out.println("Cuando indique un numero tu deberas indicar:");
      System.out.println("= si acierto el numero que tu quieres que adivine");
      System.out.println("> si el numero que tu quieres que adivine es mayor que el que mostre");
      System.out.println("< si el numero que tu quieres que adivine es menor que el que mostre");
        
      System.out.println("Escribeme el numero inicial");
      int min = keyboard.nextInt();
      
      System.out.println("Escribeme el numero final");
      int max = keyboard.nextInt();
      
      int intentos =(int)((Math.log10(max-min)/Math.log10(2))+2);
      System.out.println(intentos);
      
      System.out.println("Adivinare tu numero en no mas de " + intentos + " intentos");
      System.out.println("Presiona ENTER cuando quieras empezar...");
      keyboard.nextLine();
  
      while (intentos > 0){
          int numeroPosible = ((max - min) /2) + min;
          System.out.println("Es tu numero el " + numeroPosible);
          String opcion = keyboard.next();
          
         switch (opcion) {
            case ">":
                   min = numeroPosible +1;
                   break;
            case "<":
                    max = numeroPosible -1;
                    break;
            case "=":
                    adivinado = true;
                    System.out.println("He ganado!!!");
                    return;
            default:
                    System.out.println("La opción seleccionada no es válida");
        }
        if ((min > max) || (max < min)){
          System.out.println("Estas haciendo trampa!!!");
          return;
        } 
        
      }
      System.out.println("Has ganado!!!");
    }
}
