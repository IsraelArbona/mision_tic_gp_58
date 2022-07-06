package co.edu.utp.misiontic2022.c2;

public class Cuadrado extends Figura {

    // Se define un atributo: "lado" (variable de la clase)
    private double lado;

    // Constructor de la clase "Cuadrado"
    public Cuadrado(String color, double lado){
        // Toma de la abstracta "Figura" (super) el (método) constructor "color"
        super(color);
        this.lado = lado;
    }

    //Método que fue definido en la clase abstracta "Figura"
    public double calcularArea(){
        return lado * lado;
    }
    
}
