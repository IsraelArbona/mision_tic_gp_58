package co.edu.utp.misiontic2022.c2;

import java.util.HashMap;
import java.util.Map;

/**
 * Map
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        HashMap<Integer, String> m = new HashMap<>();

        m.put(924, "Jose Diaz");
        m.put(921, "Ana Lopez");
        m.put(700,"Cesar Vazquez");
        m.put(219,"Camilo Guerra");
        m.put(537,"Alan Brito");
        m.put(921,"Maria Clara");

        System.out.println(m.get(921));
        System.out.println(m.get(605));
        System.out.println(m.get(537));

        System.out.println("Todos los elementos de m son: " + m);

        System.out.println("Todos los elementos de m son con entrySet: " + m.entrySet());

        for(Map.Entry pareja: m.entrySet()){
            System.out.println(pareja);
        }
    }
}
