public class MyApp {
    public static void main(String[] args) throws Exception {
        
        // Ciclo de for

        /*
            for (inicializacion; condicion; incremento) {
                instrucciones
            }
        */

        /*
        for (int i = 0; i < 100; i++) {
           System.out.println("numero es: " + i); 
        }
        */

        // Ciclo del while

        /*
        var numero = 0;
        while (numero < 100){
            if(numero == 11){
                break;
            }
            System.out.println("numero while es : " + numero);
            numero++;
        }
        */

        // Ciclo del do while
        // Imprimir del numero 100 al numero 120 

        var numero2 = 0;
        do {
            if ((numero2 >= 100) && (numero2 <=120)){
                System.out.println("numero de while es : " + numero2);
                // continue;
            }
            numero2++;
        } while (numero2 < 200);


    }
}
