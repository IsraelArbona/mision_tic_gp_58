package co.edu.utp.misiontic2022.c2;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /*
            MiPrimerClase mpc = new MiPrimerClase();
            MiPrimerClase mpc2 = new MiPrimerClase(20);
            MiPrimerClase mpc3 = new MiPrimerClase(10,25);

            mpc.incrementarContador(10);
            System.out.println("Valor del atributo contador mpc es: " + mpc.getContador());
            mpc.setContador(50);
            System.out.println("Valor del atributo contador mpc es: " + mpc.getContador());

            System.out.println("Valor del atributo contador mpc2 es: " + mpc2.getContador());
            mpc2.incrementarContador(80);
            System.out.println("Valor del atributo contador mpc2 es: " + mpc2.getContador());

            System.out.println("Valor contador mpc3 es: " + mpc3.getContador());
            System.out.println("Valor numero Horas mpc3 es: " + mpc3.getNumHoras());
        */

        /*
            // Declarar variables
            String colorTriangulo;
            double baseTriangulo;
            double alturaTriangulo;

            // Se instancia sc de la clase Scanner
            Scanner sc = new Scanner(System.in);

            System.out.print("Introduzca el color del triángulo: ");
            colorTriangulo = sc.nextLine();
            System.out.print("Introduzca la base del triángulo: ");
            baseTriangulo = sc.nextDouble();
            System.out.print("Introduzca la altura del triágulo: ");
            alturaTriangulo = sc.nextDouble();

            Triangulo triangulo = new Triangulo(colorTriangulo, baseTriangulo, alturaTriangulo);
            System.out.printf("El área del triángulo %s es: %f", triangulo.getColor(), triangulo.calcularArea());
            sc.close();
        */

        //Declara variable
        String colorCuadrado;
        double ladoCuadrado;

        // instanciamos de la clase Scanner
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduzca el color del cuadrado: ");
        colorCuadrado = sc.nextLine();
        System.out.print("Introduzca el lado del cuadrado: ");
        ladoCuadrado = sc.nextDouble();

        Cuadrado cuadrado = new Cuadrado(colorCuadrado, ladoCuadrado);
        System.out.printf("El área del cuadrado %s es: %f", cuadrado.getColor(),cuadrado.calcularArea());
        sc.close();
    }
}
