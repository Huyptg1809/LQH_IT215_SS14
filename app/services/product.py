from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

def create_product(product: ProductCreate, db: Session):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(product_id: int, product_update: ProductUpdate, db: Session):
    db_product = get_product_by_id(product_id, db)
    
    update_data = product_update.model_dump()
    for key, value in update_data.items():
        setattr(db_product, key, value)
        
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(product_id: int, db: Session):
    db_product = get_product_by_id(product_id, db)
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
