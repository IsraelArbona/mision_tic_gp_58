package co.edu.utp.misiontic2022.c2;

/**
 * Gen
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // Crear una instancia Fen para Integers
        Gen<Integer> iOb;

        iOb = new Gen<Integer>(58);

        // Muestra el tipo de dato utilizado iOb
        iOb.mostrarTipo();

        // este caso no necesitamos una conversion
        int v = iOb.getOb();
        System.out.println("valor : " + v);

        //Crear un objeto Gen de tipo string
        Gen<String> cadena = new Gen<String>("Grupo 58");

        // mostrar el tipo de dato
        cadena.mostrarTipo();

        // no se necesita una conversion
        String dato = cadena.getOb();
        System.out.println("Cadena: " + dato);


    }
}

// T es un parametro de tipo que sera reemplazado por un tipo real cuando el objeto se cree
class Gen<T>{

    // T es el parametro de tipo generico
    T ob;

    // Pasar al constructor una referencia  un objeto de tipo T
    Gen(T o){
        ob = o;
    }

    T getOb(){
        return ob;
    }

    // muestra el tipo T
    void mostrarTipo(){
        System.out.println("El tipo de T es: " + ob.getClass().getName());
    }
}
