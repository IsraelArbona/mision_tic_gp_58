package co.edu.utp.misiontic2022.c2;

public class Triangulo extends Figura {

    // Se definen dos atributos: "base" y "altura" (variables de la clase)
    private double base;
    private double altura;

    // Constructor de la clase "Triangulo"
    public Triangulo(String color, double base, double altura){
        // Toma de la clase abstracta "Figura" (super) el (método) constructor "color"
        super(color);
        this.base = base;
        this.altura = altura;
    }

    // Método que fue definido en la clase abstracta "Figura"
    public double calcularArea(){
        return ((base * altura) / 2);
    }
    
}
