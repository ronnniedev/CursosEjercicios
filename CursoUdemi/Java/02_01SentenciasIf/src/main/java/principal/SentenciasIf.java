package principal;

import java.util.Scanner;


public class SentenciasIf {
    
    public static void main (String args[]){
        
        
    Scanner keyboard = new Scanner (System.in);
    final double PI = 3.14;
    double radio;
    double largo;
    double ancho;
    double base;
    double lado;
    double altura;
    String opcion;

    System.out.println("Elige una opcion:\n\n1) o a)Rectangulo\n2) o b)Circunferencia\n"
                         + "3) o c)Triangulo\n\n 0) Salir>> ");

    opcion= keyboard.nextLine();
    
    if(!opcion.equals("1")&& !opcion.equals("a")&&!opcion.equals("2")&& !opcion.equals("b")
            &&!opcion.equals("3")&& !opcion.equals("c")){
        System.out.println("Opcion no valida");
    }
    
    switch(opcion){
        case "1","a":
            
            System.out.println("LARGO >>");
            largo = keyboard.nextDouble();
            keyboard.nextLine();
            System.out.println("Ancho >>");
            ancho = keyboard.nextDouble();
            keyboard.nextLine();
        
            System.out.println("Perimetro = " + (largo * 2 + ancho * 2) 
                                + "Area= "+ (largo * ancho));
            break;
        case "2","b":
            System.out.println("Radio =  ");
            radio = keyboard.nextDouble();
            keyboard.nextLine();
        
            System.out.println("Perimetro = "+ (radio * PI) + " Area = " 
                            + (PI* Math.pow(radio, 2)) );
            break;
            
        case "3","c":
            System.out.println("Lado: ");
            lado = keyboard.nextDouble();
            keyboard.nextLine();
            System.out.println("Base: ");
            base = keyboard.nextDouble();
            keyboard.nextLine();
            System.out.println("Altura: ");
            altura = keyboard.nextDouble();
            keyboard.nextLine();
        
        
            System.out.println("Perimetro =" + (lado*2 + base) + "Area =" 
                            + (base*altura)/2);
            break;
        default:
            System.out.println("Error opcion no valida");
            
    }
        
    }
}
