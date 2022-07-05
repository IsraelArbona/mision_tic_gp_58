public class App {
    public static void main(String[] args) throws Exception {
       
        String cadena = "         EstoesunaCadenaDeCaracteres       ";
        int longitud = 0;

        longitud = cadena.length();

        System.out.println("La longitud de la cadena es : " + longitud);
        System.out.println("Indice de caracter t: " + cadena.indexOf('t'));
        System.out.println("Posición del caracter '2' : " + cadena.charAt(2));

        System.out.println("Devuelve la sub-cadena desde la posiciçon 1 hasta 9: " + cadena.substring(1,9));

        System.out.println("Devuelve la cadena convertida a mayúsculas : " + cadena.toUpperCase());
        System.out.println("Devuelve la cadena convertida a minúscula: " + cadena.toLowerCase());

        System.out.println("Elimina los espacios al inicio y final de una cadena de carracteres " + cadena.trim());

    }
}
