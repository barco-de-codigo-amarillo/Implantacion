from fastapi import FastAPI

# Importa tus routers desde la carpeta routers
# from app.routers import users, items  (Ajusta según tus módulos reales)

app = FastAPI(
    title="Mi API con FastAPI",
    description="API estructurada con core, models, schemas y routers",
    version="1.0.0",
)


@app.get("/")
def read_root():
  return {"message": "¡La API está funcionando correctamente!"}


# Incluye tus routers aquí
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(items.router, prefix="/items", tags=["Items"])