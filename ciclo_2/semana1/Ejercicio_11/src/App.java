import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        var sc = new Scanner(System.in);
        int dia, mes, anio, numSuerte,sumFecha, cf1, cf2, cf3, cf4;

        System.out.println("Por favor, introduzca su fecha de nacimiento");
        System.out.print("día: ");
        dia = sc.nextInt();

        System.out.print("mes: ");
        mes = sc.nextInt();

        System.out.print("año: ");
        anio = sc.nextInt();

        sumFecha = dia + mes + anio;
        System.out.println(sumFecha);

        cf1 = sumFecha/1000;            // Obtiene la primera cifra
        cf2 = sumFecha/100%10;          // Obtiene la segunda cifra
        cf3 = sumFecha/10%10;           // Obtiene la tercera cifra
        cf4 = sumFecha/1%10;            // Obtiene la cuarta cifra

        numSuerte = cf1 + cf2 + cf3 + cf4;

        System.out.println("Su número de la suerte es : " + numSuerte);

    }
}
