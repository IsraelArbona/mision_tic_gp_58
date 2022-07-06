package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        DeDos objInt = new DeDos();

        for(int i = 0; i < 5; i++)
            System.out.println("El siguiente valor es: " + objInt.getSiguiente());
            System.out.println("El valor anterior a " + objInt.getSiguiente() + " es " + objInt.gerAnterior());
        
        System.out.println("\nReiniciando....");
        objInt.reiniciar();

        for(int i = 0; i < 5; i++)
            System.out.println("El siguiente valor es: " + objInt.getSiguiente());
            System.out.println("El valor anterior a " + objInt.getSiguiente() + " es " + objInt.gerAnterior());
            System.out.println("\nIniciando en 1000...");
        
        objInt.setComenzar(1000);

        for(int i = 0; i < 10; i++)
            System.out.println("El siguiente valor es: " + objInt.getSiguiente());
            System.out.println("El valor anterior a " + objInt.getSiguiente() + " es " + objInt.gerAnterior());
    }
}
