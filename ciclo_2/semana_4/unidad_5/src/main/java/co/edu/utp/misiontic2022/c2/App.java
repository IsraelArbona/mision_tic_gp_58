package co.edu.utp.misiontic2022.c2;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import co.edu.utp.misiontic2022.c2.model.Persona;

/**
 * ORM
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "INICIO...." );

        Persona persona = new Persona("Maria", 25);

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("unidad_5-pu");
        EntityManager em = emf.createEntityManager();

        try {
            em.getTransaction().begin();
            em.persist(persona);
            em.getTransaction().commit();
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            em.close();
        }


    }
}
