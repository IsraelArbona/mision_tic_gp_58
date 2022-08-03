package co.edu.utp.misiontic2022.c2.model.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import co.edu.utp.misiontic2022.c2.model.vo.DeudasPorProyectoVo;
import co.edu.utp.misiontic2022.c2.util.JDBCUtilities;

public class DeudasPorProyectoDao {

    public List<DeudasPorProyectoVo> listar (Double limite) throws SQLException {
        ArrayList<DeudasPorProyectoVo> respuesta = new ArrayList<DeudasPorProyectoVo>();
        Connection conn = JDBCUtilities.getConnection();
        PreparedStatement stmt = null;
        ResultSet rs = null;

        String sql =" SELECT p.ID_Proyecto AS ID, SUM(c.Cantidad * mc.Precio_Unidad) AS VALOR " +
                    " FROM Proyecto p " +
                    " JOIN Compra c ON (p.ID_Proyecto = c.ID_Proyecto) " +
                    " JOIN MaterialConstruccion mc ON (c.ID_MaterialConstruccion = mc.ID_MaterialConstruccion) " +
                    " WHERE c.Pagado = 'No' " +
                    " GROUP BY p.ID_Proyecto " +
                    " HAVING SUM(c.Cantidad * mc.Precio_Unidad) > ? " +
                    " ORDER BY VALOR DESC;";

        try{
            stmt = conn.prepareStatement(sql);
            stmt.setDouble(1, limite);
            rs = stmt.executeQuery();

            while (rs.next()){
                DeudasPorProyectoVo deudaVo = new DeudasPorProyectoVo(
                    rs.getInt("ID"),
                    rs.getDouble("VALOR")
                );

                respuesta.add(deudaVo); 
            }
        } finally {
            if (rs != null){
                rs.close();
            }
            if (stmt != null){
                stmt.close();
            }
            if (conn != null){
                conn.close();
            }
        }
        
        return respuesta;
    }
}
