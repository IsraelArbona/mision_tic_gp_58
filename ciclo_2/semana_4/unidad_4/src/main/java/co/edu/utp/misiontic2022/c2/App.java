package co.edu.utp.misiontic2022.c2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import co.edu.utp.misiontic2022.c2.model.Employee;

/**
 * JDBC
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /* 
        String direccionDB = "C://Users/israelarbonaguerrero/Desktop/RUTA2_MISIONTIC_2022/grupo_58/ciclo_2/semana_3/db/hr.db";

        String url = "jdbc:sqlite:" + direccionDB;
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection(url);
            stmt = conn.createStatement();
            var sql = "SELECT employee_id, first_name, last_name, email FROM employees";

            rs = stmt.executeQuery(sql);

            while (rs.next()) {
                int id = rs.getInt("employee_id");
                String nombre = rs.getString("first_name");
                String apellido = rs.getString("last_name");
                String email = rs.getString("email");

                System.out.println("(" + id + ") " + nombre + " " + apellido);
                
            }
        } catch (Exception e) {
            System.out.println("Error de conexion : " + e.getMessage());
        }

        */

        String direccionDB = "C://Users/israelarbonaguerrero/Desktop/RUTA2_MISIONTIC_2022/grupo_58/ciclo_2/semana_3/db/hr.db";

        String url = "jdbc:sqlite:" + direccionDB;
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        var listaEmployee = new ArrayList<Employee>();

        try {
            conn = DriverManager.getConnection(url);
            stmt = conn.createStatement();
            String sql =  "SELECT employee_id, first_name, last_name, email FROM employees LIMIT 10";

            rs = stmt.executeQuery(sql);

            while (rs.next()) {

                Employee empleados = new Employee();

                empleados.setEmployee_id(rs.getInt("employee_id"));
                empleados.setFirst_name(rs.getString("first_name"));
                empleados.setLast_name(rs.getString("last_name"));
                empleados.setEmail(rs.getString("email"));


                int id = rs.getInt("employee_id");
                String nombre = rs.getString("first_name");
                String apellido = rs.getString("last_name");
                String email = rs.getString("email");

                Employee empleados2 = new Employee(
                    id,
                    nombre,
                    apellido,
                    email
                );

                // System.out.println(empleados.getEmail());
                // System.out.println(empleados2.getEmail());

                listaEmployee.add(empleados);

            }

        } catch (Exception e) {
            System.out.println("Error en la base de datos: " + e.getMessage());
        } finally {
            try {
                if (rs != null){
                    rs.close();
                }
                if (stmt != null){
                    stmt.close();
                }
                if (conn != null){
                    conn.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        for (Employee el: listaEmployee){
            // System.out.println(el.getLast_name());
            System.out.println(el.toString());
        }

    }
}
