package co.edu.utp.misiontic2022.c2;

import javax.swing.JButton;
import javax.swing.JFrame;

/**
 * Swing
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        JFrame ventana = new JFrame(); // Creamos una instancia del JFrame

        JButton boton = new JButton("Click"); // creamos una instancia de JButton
        boton.setBounds(130, 100, 100, 40); // x axis, y axis, width, height

        ventana.add(boton); // agregamos el boton dentro del JFrame

        ventana.setSize(400, 500); // 400 width, 500 height
        ventana.setLayout(null); // asignamos null manager layout
        ventana.setVisible(true);

    }
}
