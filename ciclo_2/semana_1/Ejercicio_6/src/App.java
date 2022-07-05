import java.security.DrbgParameters.NextBytes;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
       
        var sc = new Scanner(System.in);

        System.out.println("Ingrese el numero entero");
        var numero = sc.nextInt();

        var digitos = numeroDigito(numero);
        System.out.println("El número tiene : " + digitos + " cifras");

    }


    public static int numeroDigito(int numero){
        int cifras = 0;

        while (numero != 0){
            // numero = numero / 10;
            numero /= 10;

            // cifras = cifras +1;
            cifras++;
        }
        
        return cifras;
    }
}
