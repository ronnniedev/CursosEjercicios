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
    final String OPCION_1= "1";
    final String OPCION_2= "2";
    final String OPCION_3= "3";
    final String OPCION_SALIR= "0";

    System.out.println("Elige una opcion:\n\n1) o a)Rectangulo\n2) o b)Circunferencia\n"
                         + "3) o c)Triangulo\n\n 0) Salir>> ");

    opcion= keyboard.nextLine();
    
    if(!opcion.equals("1")&& !opcion.equals("a")&&!opcion.equals("2")&& !opcion.equals("b")
            &&!opcion.equals("3")&& !opcion.equals("c")){
        System.out.println("Opcion no valida");
    }
    while(!opcion.equals("s")&& !opcion.equals("S") && !opcion.equals(OPCION_SALIR)){
        System.out.println("Elige una opcion:\n\n1) o a)Rectangulo\n2) o b)Circunferencia\n"
                         + "3) o c)Triangulo\n\n 0) Salir>> ");

    opcion= keyboard.nextLine();
    switch(opcion){
        case OPCION_1,"a":
            
            System.out.println("LARGO >>");
            largo = keyboard.nextDouble();
            keyboard.nextLine();
            System.out.println("Ancho >>");
            ancho = keyboard.nextDouble();
            keyboard.nextLine();
        
            System.out.println("Perimetro = " + (largo * 2 + ancho * 2) 
                                + "Area= "+ (largo * ancho));
            break;
        case OPCION_2,"b":
            System.out.println("Radio =  ");
            radio = keyboard.nextDouble();
            keyboard.nextLine();
        
            System.out.println("Perimetro = "+ (radio * PI) + " Area = " 
                            + (PI* Math.pow(radio, 2)) );
            break;
            
        case OPCION_3,"c":
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
            case OPCION_SALIR,"s","S":
            
            break;
        default:
            System.out.println("Error opcion no valida");
    
    }
    
            
    }
        
    }
}
