from fastapi import FastAPI
from app.database import engine, Base
from app.routers import product

# Tự động tạo bảng trong CSDL
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Management API")

# Gắn router
app.include_router(product.router)
