package co.edu.utp.misiontic2022.c2;

public class PrecioTotal {

    // atributos
    private Double totalComputadores = 0.0;
    private Double totalComputadoresMesa = 0.0;
    private Double totalComputadoresPortatiles = 0.0;

    private Computadores[] listaComputadores;

    // Constructor
    public PrecioTotal(Computadores[] listaComputadores){
        this.listaComputadores = listaComputadores;
    }

    public void mostrarTotales(){

        for (Computadores compu: listaComputadores){
            if (compu instanceof Computadores){
                totalComputadores += compu.calcularPrecio();
            }
            if (compu instanceof ComputadoresMesa){
                totalComputadoresMesa += compu.calcularPrecio();
            }
            if (compu instanceof ComputadoresPortatiles){
                totalComputadoresPortatiles += compu.calcularPrecio();
            }
        }

        // mostrar los resultados
        System.out.println("La suma del precio de los computadores es de " + totalComputadores);
        System.out.println("La suma del precio de los computadores de mesa es de " + totalComputadoresMesa);
        System.out.print("La suma del precio de los computadores portátiles es de " + totalComputadoresPortatiles);
    }

}
