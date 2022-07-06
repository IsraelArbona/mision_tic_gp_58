package co.edu.utp.misiontic2022.c2;

/**
 * Interfases
 * 
 * Define métodos sin cuerpo
 * Implementado por subclases
 * 
 * <(modificador)"public" o "default"> interface <nombre>(<tipo paramentro>)
 * 
 * Donde:
 *      public: para todos los paquetes.
 *      default: Nose coloca y solo es visible desde otros miembros del mismo paquete.
 * 
 * La variables declaradas en una interfaz no son variables de instancia. En cambio,
 * son implícitament public, final y static y deben incializarse. Por lo tanto,
 * son esencialmente constantes.
 */

public interface Series {
    
    int getSiguiente();         // Retorna el siguiente número de la serie
    void reiniciar();           // Reinicia la serie
    void setComenzar(int x);    // Establece el valor inicial.
    
}
