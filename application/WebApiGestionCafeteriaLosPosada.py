#WebAPIGestionCafeteriaLosPosada

##############################################################

from fastapi import FastAPI

from core.domain.geografia.GeografiaModel import Geografia

from core.domain.empresa.EmpresaModel import Empresa

from core.domain.productos.ProductosModel import Productos

from core.domain.clientes.ClientesModel import Clientes

from core.domain.transaccional.TransaccionalModel import Transaccional

app: FastAPI = FastAPI(
                        title='Web API Gestion Cafeteria Los Posada',
                        description='UUSBGS - 202302'
                      )
##############################################################

@app.post(
        "/ingresargeografia",
        response_model= Geografia,
        summary="Ingresar Geografia",
        description="API para ingresar Geografia",
        tags=["Geografia"]
        )

async def  ingresar_geografia(geografia: Geografia | None =  None):
    return geografia


@app.post(
        "/modificargeografia",
        response_model= Geografia,
        summary="Modificar Geografia",
        description="API para modificar Geografia",
        tags=["Geografia"]
        )

async def  retirar_geografia(geografia: Geografia | None =  None):
    return geografia


@app.post(
        "/retirargeografia",
        response_model= Geografia,
        summary="Retirar Geografia",
        description="API para retirar Geografia",
        tags=["Geografia"]
        )

async def  retirar_geografia(geografia: Geografia | None =  None):
    return geografia
    

@app.post(
        "/consultargeografia",
        response_model= Geografia,
        summary="Consultar Geografia",
        description="API para consultar Geografia",
        tags=["Geografia"]
        )

async def  conusltar_geografia(geografia: Geografia | None =  None):
    return geografia


@app.post(
        "/consultarIDgeografia",
        response_model= Geografia,
        summary="Consultar ID Geografia",
        description="API para consultar ID Geografia",
        tags=["Geografia"]
        )

async def  conusltarID_geografia(geografia: Geografia | None =  None):
    return geografia
##############################################################

@app.post(
        "/ingresarempresa",
        response_model= Empresa,
        summary="Ingresar Empresa",
        description="API para ingresar Empresa",
        tags=["Empresa"]
        )

async def  ingresar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/modificarempresa",
        response_model= Empresa,
        summary="Modificar Empresa",
        description="API para modificar Empresa",
        tags=["Empresa"]
        )

async def  retirar_Empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/retirarempresa",
        response_model= Empresa,
        summary="Retirar Empresa",
        description="API para retirar Empresa",
        tags=["Empresa"]
        )

async def  retirar_empresa(empresa: Empresa | None =  None):
    return empresa
    

@app.post(
        "/consultarempresa",
        response_model= Empresa,
        summary="Consultar Empresa",
        description="API para consultar Empresa",
        tags=["Empresa"]
        )

async def  conusltar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/consultarIDempresa",
        response_model= Empresa,
        summary="Consultar ID Empresa",
        description="API para consultar ID Empresa",
        tags=["Empresa"]
        )

async def  conusltarID_empresa(empresa: Empresa | None =  None):
    return empresa
##############################################################
@app.post(
        "/ingresarclientes",
        response_model= Clientes,
        summary="Ingresar Clientes",
        description="API para ingresar Clientes",
        tags=["Clientes"]
        )

async def  clientes(clientes: Clientes | None =  None):
    return clientes


@app.post(
        "/modificarclientes",
        response_model= Clientes,
        summary="Modificar Clientes",
        description="API para modificar Clientes",
        tags=["Clientes"]
        )

async def  retirar_Clientes(clientes: Clientes | None =  None):
    return Clientes


@app.post(
        "/retirarempresa",
        response_model= Empresa,
        summary="Retirar Empresa",
        description="API para retirar Empresa",
        tags=["Empresa"]
        )

async def  retirar_clientes(clientes: Clientes | None =  None):
    return clientes
    

@app.post(
        "/consultarclientes",
        response_model= Clientes,
        summary="Consultar Clientes",
        description="API para consultar Clientes",
        tags=["Empresa"]
        )

async def  conusltar_clientes(clientes: Clientes | None =  None):
    return clientes


@app.post(
        "/consultarIDclientes",
        response_model= Clientes,
        summary="Consultar ID Clientes",
        description="API para consultar ID Clientes",
        tags=["Clientes"]
        )

async def  conusltarID_clientes(clientes: Clientes | None =  None):
    return clientes
##############################################################
@app.post(
        "/ingresarempresa",
        response_model= Empresa,
        summary="Ingresar Empresa",
        description="API para ingresar Empresa",
        tags=["Empresa"]
        )

async def  ingresar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/modificarempresa",
        response_model= Empresa,
        summary="Modificar Empresa",
        description="API para modificar Empresa",
        tags=["Empresa"]
        )

async def  retirar_Empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/retirarempresa",
        response_model= Empresa,
        summary="Retirar Empresa",
        description="API para retirar Empresa",
        tags=["Empresa"]
        )

async def  retirar_empresa(empresa: Empresa | None =  None):
    return empresa
    

@app.post(
        "/consultarempresa",
        response_model= Empresa,
        summary="Consultar Empresa",
        description="API para consultar Empresa",
        tags=["Empresa"]
        )

async def  conusltar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/consultarIDempresa",
        response_model= Empresa,
        summary="Consultar ID Empresa",
        description="API para consultar ID Empresa",
        tags=["Empresa"]
        )

async def  conusltarID_empresa(empresa: Empresa | None =  None):
    return empresa
##############################################################
@app.post(
        "/ingresarproductos",
        response_model= Productos,
        summary="Ingresar Productos",
        description="API para ingresar Productos",
        tags=["Productos"]
        )

async def  producctos(productos: Productos | None =  None):
    return productos


@app.post(
        "/modificarproductos",
        response_model= Productos,
        summary="Modificar Productos",
        description="API para modificar Productos",
        tags=["Productos"]
        )

async def  retirar_Productos(productos: Productos | None =  None):
    return productos


@app.post(
        "/retirarproductos",
        response_model= Productos,
        summary="Retirar Productos",
        description="API para retirar Productos",
        tags=["Productos"]
        )

async def  retirar_productos(productos: Productos | None =  None):
    return productos
    

@app.post(
        "/consultarproductos",
        response_model= Productos,
        summary="Consultar CProductos",
        description="API para consultar Productos",
        tags=["Productos"]
        )

async def  conusltar_productos(productos: Productos | None =  None):
    return productos


@app.post(
        "/consultarIDproductos",
        response_model= Productos,
        summary="Consultar ID Productos",
        description="API para consultar ID Productos",
        tags=["Productos"]
        )

async def  conusltarID_productos(productos: Productos | None =  None):
    return productos
##############################################################
@app.post(
        "/ingresarempresa",
        response_model= Empresa,
        summary="Ingresar Empresa",
        description="API para ingresar Empresa",
        tags=["Empresa"]
        )

async def  ingresar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/modificarempresa",
        response_model= Empresa,
        summary="Modificar Empresa",
        description="API para modificar Empresa",
        tags=["Empresa"]
        )

async def  retirar_Empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/retirarempresa",
        response_model= Empresa,
        summary="Retirar Empresa",
        description="API para retirar Empresa",
        tags=["Empresa"]
        )

async def  retirar_empresa(empresa: Empresa | None =  None):
    return empresa
    

@app.post(
        "/consultarempresa",
        response_model= Empresa,
        summary="Consultar Empresa",
        description="API para consultar Empresa",
        tags=["Empresa"]
        )

async def  conusltar_empresa(empresa: Empresa | None =  None):
    return empresa


@app.post(
        "/consultarIDempresa",
        response_model= Empresa,
        summary="Consultar ID Empresa",
        description="API para consultar ID Empresa",
        tags=["Empresa"]
        )

async def  conusltarID_empresa(empresa: Empresa | None =  None):
    return empresa
##############################################################
@app.post(
        "/ingresartransaccional",
        response_model= Transaccional,
        summary="Ingresar Transaccional",
        description="API para ingresar Transaccional",
        tags=["Transaccional"]
        )

async def  transaccional(transaccional: Transaccional | None =  None):
    return transaccional


@app.post(
        "/modificartransaccional",
        response_model= Transaccional,
        summary="Modificar Transaccional",
        description="API para modificar Transaccional",
        tags=["Transaccional"]
        )

async def  retirar_Transaccional(transaccional: Transaccional | None =  None):
    return Transaccional


@app.post(
        "/retirartransaccional",
        response_model= Transaccional,
        summary="Retirar Transaccional",
        description="API para retirar Transaccional",
        tags=["Transaccional"]
        )

async def  retirar_transaccional(transaccional: Transaccional | None =  None):
    return transaccional
    

@app.post(
        "/consultartransaccional",
        response_model= Transaccional,
        summary="Consultar Transaccional",
        description="API para consultar Transaccional",
        tags=["Transaccional"]
        )

async def  conusltar_transaccional(transaccional: Transaccional | None =  None):
    return transaccional


@app.post(
        "/consultarIDtransaccional",
        response_model= Transaccional,
        summary="Consultar ID Transaccional",
        description="API para consultar ID Transaccional",
        tags=["Transaccional"]
        )

async def  conusltarID_transaccional(transaccional: Transaccional | None =  None):
    return transaccional
##############################################################