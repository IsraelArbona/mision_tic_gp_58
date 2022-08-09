package co.edu.utp.misiontic2022.c2.controller;

import java.sql.SQLException;
import java.util.ArrayList;

import co.edu.utp.misiontic2022.c2.model.dao.AsesorPorCiudadDao;
import co.edu.utp.misiontic2022.c2.model.vo.AsesorPorCiudadVo;

public class RequerimientoController {
    
    private final AsesorPorCiudadDao asesorPorCiudadDao;

    public RequerimientoController() {
        asesorPorCiudadDao = new AsesorPorCiudadDao();
    }


    public ArrayList<AsesorPorCiudadVo> consultarAsesorPorCiudad() throws SQLException{
        return asesorPorCiudadDao.listar();
    }

}
