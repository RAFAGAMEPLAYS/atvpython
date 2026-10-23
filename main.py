import logging

from fastapi import FastAPI,HTTPException,Path,Query,Request,Response
from fastapi.responses import JSONResponse
from mysql.connector import Error as MySQLError

from database import executar_sql

app = FastAPI(title="FAST API 2INFO2")

@app.exception_handler(MySQLError)
def erro_de_banco(request: Request, exc: MySQLError):
    logging.getLogger("uvicorn.error").error(f"Erro de banco de dados: %s", exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro de banco de dados"},
    )

def representar_produto(produto):
    return {
        "id":produto["id"],
        "nome":produto["nome"],
        "preco":format(produto["preco"], "2f"),
        "categoria":produto["categoria"],
    }

@app.get("/produtos")
def listar_produtos():
    sql="SELECT * FROM produtos"
    produtos=executar_sql(sql)
    return {"dados":[representar_produto(produto) for produto in produtos],"sintaxe":{"sql":sql,"parametros":[]},}