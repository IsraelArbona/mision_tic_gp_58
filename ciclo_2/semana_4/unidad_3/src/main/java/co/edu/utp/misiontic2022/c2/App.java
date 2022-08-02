package co.edu.utp.misiontic2022.c2;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

/**
 * Serializable
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /* 
        File nombre = new File("Objeto.dat");

        try {
            FileOutputStream archivo = new FileOutputStream(nombre);
            ObjectOutputStream oos = new ObjectOutputStream(archivo);

            oos.writeObject(new Persona("552871883", "Maria", "Ruiz Ramos"));
            oos.writeObject(new Persona("403020104", "Juan", "Gonzalez Lopez"));
            oos.close();

            System.out.println("Archivo escrito");

        } catch (FileNotFoundException e) {
            System.out.println("El archivo no existe");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        */

        File nombre = new File("Objeto.dat");

        try {
            FileInputStream archivo = new FileInputStream(nombre);
            ObjectInputStream ois = new ObjectInputStream(archivo);

            Persona p1 = (Persona) ois.readObject();
            Persona p2 = (Persona) ois.readObject();
            ois.close();

            System.out.println("Cedula \t\t Nombre");
            System.out.println(p1.getAtributos());
            System.out.println(p2.getAtributos());

        } catch (FileNotFoundException e) {
            System.out.println("El archivo no existe");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
