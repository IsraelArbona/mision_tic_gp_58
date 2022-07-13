package co.edu.utp.misiontic2022.c2;

public class Matematicas {

    public double dividir(double a, double b) throws Exception{

        if(b == 0){
            throw new Exception("El parametro b no puede ser 0");
        }
        return a/b;
    }
    
}
