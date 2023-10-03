# main;

###############################

import uvicorn

###############################

def webapi_gestioncafeterialosposada():
    uvicorn.run(
        "aplication.WebAPIGestionCafeteriaLosPosada:app",
        host="127.0.0.1",
        port=8060,
        reload=True
    )
        
###############################

if __name__=='__main__':
    webapi_gestioncafeterialosposada()
    
###############################