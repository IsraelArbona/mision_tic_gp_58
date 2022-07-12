package co.edu.utp.misiontic2022.c2;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Colas en java con Queue:
 * 
 * para insertar
 * - add(e)
 * - offer(e)
 * 
 * para extraer
 * - remove()
 * - poll()
 * 
 * para consultar el frente
 * - element()
 * - peek()
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // creamos la Cola indicando el tipo de dato
        Queue<Integer> cola = new LinkedList<>();

        cola.offer(3);      // insertar un elemento (mejor método)
        cola.add(14);       // insertar un elemento (lanzar excepciones)
        cola.offer(12);
        cola.add(7);
        cola.offer(10);

        // impresión de la cola con todos los datos.
        System.out.println("Cola llena : " + cola);

        // Estructura repetitiva para desencolar
        while(cola.poll() != null){                 // Recuperar el primer elemento, si es null= vacio
            System.out.println(cola.peek());        //Muestre el primer elemento de la cola
        }

        // Muestra null debido a que la ya esta esta vacia
        System.out.println(cola.peek());
    }
}
