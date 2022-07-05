
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor ingrese su nombre");
        String nombre = sc.nextLine();

        System.out.println("El nombre es : " + nombre);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Ingrese su nombre");
        String nombre_br = br.readLine();

        System.out.println("El nombre br es -> " + nombre_br);
    }
}
