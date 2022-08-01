package co.edu.utp.misiontic2022.c2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class App 
{
    public static void main( String[] args )
    {

        /* 
        int numBytes = 0;
        char caracter;

        System.out.println("\nEscriba el texto: ");
        try {

            do {
                caracter = (char) System.in.read();
                System.out.print(caracter);
                numBytes++;
            } while (caracter != '\n');

            System.out.printf("%d bytes leidos %n", numBytes);

        } catch (Exception e) {
            System.err.println(e);
        }
        */




        /*
        byte[] buffer = new byte[255];

        System.out.println("\nEscriba el texto: ");

        try {
            System.in.read(buffer,0,255);
        } catch (Exception e) {
            System.err.println(e);
        }

        System.out.println("\nLa línea escrita es: ");
        System.out.println(buffer);
        System.out.println(new String(buffer));

        */




        /* 

        String linea = null;

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader entrada = new BufferedReader(isr);
        PrintWriter salida = new PrintWriter(System.out, true);

        salida.println("\nEscribir un texto: ");

        try {
            linea = entrada.readLine();
        } catch (Exception e) {
            System.err.println(e);
        }

        salida.println("\nLa línea escrita es: ");
        salida.println(linea);

        */

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        try {
            System.out.print("Sumando 1 : ");
            int s1 = Integer.parseInt(br.readLine());

            System.out.print("Sumando 2 : ");
            int s2 = Integer.parseInt(br.readLine());

            int suma = s1 + s2;
            System.out.println("La suma es " + s1 + " + " + s2 + " = " + suma);

        } catch (Exception e) {
            e.printStackTrace();
        }




    }
}
