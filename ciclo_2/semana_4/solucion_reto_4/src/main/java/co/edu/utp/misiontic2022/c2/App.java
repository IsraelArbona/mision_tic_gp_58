package co.edu.utp.misiontic2022.c2;

import co.edu.utp.misiontic2022.c2.view.ReportesView;

/**
 * Solucion reto 4
 * JDBC
 */
public class App 
{
    public static void main( String[] args )
    {
        var reportesView = new ReportesView();
        var banco = "Conavi";
        // reportesView.proyectosFinanciadosPorBanco(banco);

        var limiteInferior = 50_000d;
        reportesView.totalAdeudadoPorProyectosSuperioresALimite(limiteInferior);
    }
}
