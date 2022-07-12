package co.edu.utp.misiontic2022.c2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Set
 * Desarrollar un programa que elimine las cadenas duplicadas de un objeto "List",
 * haciendo uso de objeto HashSet.
 *
 */
public class App 
{
    private String colores[] = {"rojo","blanco","azul","gris","verde","blanco","naranja","gris"};

    public App(){
        List<String> lista = Arrays.asList(colores);
        System.out.println("\nArrayList : \n" + lista);
        imprimirSinDuplicados(lista);
    }

    private void imprimirSinDuplicados(Collection<String> coleccion){
        Set<String> conjunto = new HashSet<String>(coleccion);
        System.out.println("\nLos valores sin duplicados son: \n");

        for(String string: conjunto){
            System.out.println(string);
        }
    }

    public static void main( String[] args )
    {
        Set<Integer> conjuntoEntero = new HashSet<>();

        conjuntoEntero.add(4);
        conjuntoEntero.add(5);
        conjuntoEntero.add(7);
        conjuntoEntero.add(4);      // No acepta duplicados
        conjuntoEntero.add(2);

        /* 
            for(Integer entero: conjuntoEntero){
                System.out.println("Conjunto : " + entero);
            }
        */

        new App();


    }
}
