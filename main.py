from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def aura():
    return {"message": "Bom dia peoes!"}