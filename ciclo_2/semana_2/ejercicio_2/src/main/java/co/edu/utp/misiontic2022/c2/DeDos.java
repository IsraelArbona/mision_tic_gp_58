package co.edu.utp.misiontic2022.c2;

public class DeDos implements Series {
    
    int iniciar;
    int valor;
    int anterior;

    DeDos(){
        iniciar = 0;
        valor = 0;
    }

    public int getSiguiente() {
        anterior = valor;
        valor += 2;
        return valor;
    }

    public void reiniciar(){
        valor = iniciar;
        anterior = valor - 2;
    }

    public void setComenzar(int entrada){
        iniciar = entrada;
        valor = entrada;
        anterior = entrada - 2;
    }

    // Añadir un método que no esta definido en la clase "Series"
    public int gerAnterior(){
        return anterior;
    }


}
