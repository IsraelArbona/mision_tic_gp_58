package co.edu.utp.misiontic2022.c2;

/**
 * Enum
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        // System.out.println( Color.BLANCO );

        Transporte tp;
        tp = Transporte.CAMION;

        /*
            System.out.println("Valor de tp: "+ tp);
            if (tp == Transporte.AVION)
                System.out.print("tp tiene el valor de AVION");
            else
                System.out.print("tp tiene el valor de: " + tp);
        */

        // Enum para controlar sentencia switch

        switch(tp){
            case COCHE:
                System.out.println("Respuesta de Enum COCHE");
                break;
            case CAMION:
                System.out.println("Respuesta de Enum CAMION");
                break;
            case AVION:
                System.out.println("Respuesta de Enum AVION");
                break;
            case TREN:
                System.out.println("Respuesta de Enum TREN");
                break;
            default:
                System.out.println("Respuesta de Enum BARCO");
        }




    }
}
