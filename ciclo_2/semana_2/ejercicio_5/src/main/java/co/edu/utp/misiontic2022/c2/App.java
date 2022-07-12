package co.edu.utp.misiontic2022.c2;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * List
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        ArrayList<Integer> listaEnteros = new ArrayList<>();
        // var lista = new ArrayList<>();

        listaEnteros.add(4);
        listaEnteros.add(5);
        listaEnteros.add(7);
        listaEnteros.add(2,6); // agrega  el 6 entre 5 y 7

        System.out.println("El tamaño de la lista es de: " + listaEnteros.size());

        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca el número a buscar: ");
        int buscar = sc.nextInt();

        if(!listaEnteros.isEmpty()){

            if(listaEnteros.contains(buscar) == true){
                System.out.println(buscar + " Si esta");
            } else {
                System.out.println(buscar + " No esta");
            }
            
            for(int i = 0; i < listaEnteros.size(); i++){
                if(listaEnteros.get(i) == buscar){
                    System.out.println(buscar + " si esta");
                } 
            }
    
            System.out.println("Ingrese un número para devolver la posición: ");
            int buscar2 = sc.nextInt();
    
            for(int i = 0; i <= listaEnteros.size(); i++){
                if(listaEnteros.contains(buscar2) == true){
                    System.out.println(buscar2 + " esta en la posición " + listaEnteros.indexOf(buscar2));
                } else {
                    System.out.println(buscar2 + " no esta");
                }
            }

        } else {
            System.out.println("La lista esta vacia");
        }



    }
}
