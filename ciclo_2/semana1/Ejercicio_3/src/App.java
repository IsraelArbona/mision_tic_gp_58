import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /* 
            Scanner entrada = new Scanner(System.in);
            System.out.println("Ingrese el nombre");
            String resultado = entrada.nextLine();
            
            int valor = 3;

            if (valor > 4) {
                System.out.println("Correcto!");
            } else if (valor <= 3){
                System.out.println("Correcto valor menor o igual a 3");
            } else {
                System.out.println("Incorrecto");
            }

            if (resultado == "isr") {
                System.out.println("Es correcto.");
            } else if (resultado.equals("isr")){
                System.out.println("Correcto.....");
            } else {
                System.out.println("No es correcto");
            }

            if (resultado != "isr"){
                System.out.println("Son diferentes");
            } else{
                System.out.println("Son iguales");
            }
        */

        Scanner entValor = new Scanner(System.in);
        System.out.println("Ingrese un número");
        int result = entValor.nextInt();

        switch (result){
            case 1:
                System.out.println("Caso 1 es correcto");
                break;
            case 2:
                System.out.println("Caso 2 es correcto");
                break;
            default:
                System.out.println("Ninguno de los anteriores");
        }



    }
}
