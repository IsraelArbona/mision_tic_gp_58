package co.edu.utp.misiontic2022.c2;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * try
 * catch
 * finally
 */
public class App 
{
    public static void main( String[] args ) throws Exception
    {
        /* 
        try {
            System.out.println("Intetamos ejecutar los bloques de instrucciones");
            System.out.println("Instruccion 1.");
            System.out.println("Instruccion 2.");
        } catch (Exception e) {
            System.out.println("Error producido en la ejecucion de las instrucciones");
        } finally{
            System.out.println("Instrucciones ejecutadas tanto si se produce el error o no");
        }
        */

        /* 
        int[] array = new int[20];
        try{
            array[-4] = 58;
            int b = 0;
            int a = 58/b;
        } catch(ArrayIndexOutOfBoundsException | ArithmeticException ex){
            System.out.println("Error de operación: " + ex.getMessage());
        }
        */

        /* 
        Scanner teclado = new Scanner(System.in);
        int numero;

        try {
            System.out.println("Ingrese un valor entero");
            numero = teclado.nextInt();
            int cuadrado = numero * numero;
            System.out.println("El cuadrado de " + numero + " es " + cuadrado);
        } catch (InputMismatchException e) {
            System.out.println("Debe ingresar un numero entero obligatorio: " + e.getLocalizedMessage());
        }
        */

        Matematicas matematicas = new Matematicas();
        double c = matematicas.dividir(20, 0);
        System.out.println("El resultado es : " + c);

    }
}
