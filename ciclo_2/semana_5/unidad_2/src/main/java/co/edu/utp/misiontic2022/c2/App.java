package co.edu.utp.misiontic2022.c2;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

/**
 * Swing
 *
 */
public class App 
{
    JFrame f;

    App() {
        f = new JFrame("Ejercicio Componentes");
        
        JLabel l1,l2;

        l1 = new JLabel("Caja de texto");
        l1.setBounds(50, 30, 150, 20);

        JTextField tf = new JTextField();
        tf.setBounds(50, 50, 150, 20);

        JButton b = new JButton("Click");
        b.setBounds(50, 100, 100, 30);
        b.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent arg0) {
                tf.setText("Grupo 58"); 
            } 
        });

        l2 = new JLabel("Btn Imagen");
        l2.setBounds(50, 180, 300, 20);
        JButton bIm = new JButton(new ImageIcon("./mintic.png"));
        bIm.setBounds(50, 200, 300, 160);

        f.add(tf);
        f.add(b);
        f.add(bIm);
        f.add(l1);
        f.add(l2);
        f.setSize(500, 600);
        f.setLayout(null);
        f.setVisible(true);
    }

    public static void main( String[] args )
    {
        new App();
    }
}
