package co.edu.utp.misiontic2022.c2;

public abstract class Figura {

    private String color;
    // Constructor: define atributo "color" con un "this" haciendo las veces de setter
    public Figura(String color){
        this.color = color;
    }

    // Método vacio para ser implementado desde la subclase (hijas)
    public abstract double calcularArea();

    // getter, acceder al atributo color
    public String getColor(){
        return color;
    }
    
}
