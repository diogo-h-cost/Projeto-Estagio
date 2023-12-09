from config import session
from entities import Products, ProductVariants
from fastapi import FastAPI
from models_pyd import ProdPyd, ProdVarPyd
from sqlalchemy import delete, update
from tables import banco, table1, table2

session.execute(banco)

session.execute(table1)

session.execute(table2)

projeto = FastAPI()

@projeto.get("/products/{prod_id}")
def read_prod(prod_id: int):
    prods_join = session.query(Products, ProductVariants.model, ProductVariants.color, ProductVariants.size).join(ProductVariants, Products.id == ProductVariants.product_id)
    prods = prods_join.filter(Products.id == prod_id).first()

    if prods is None:
        return {"msg": "Product not found"}

    return {
            "id": prods.Products.id,
            "name": prods.Products.name,
            "description": prods.Products.description,
            "value": prods.Products.value,
            "model": prods.model,
            "color": prods.color,
            "size": prods.size
            }

@projeto.get("/products")
def read_prod_all():
    prod_with_var = session.query(Products, ProductVariants.id, ProductVariants.product_id, ProductVariants.model, ProductVariants.color, ProductVariants.size).join(ProductVariants, Products.id == ProductVariants.product_id)
    all_prod = prod_with_var.all()

    products_dict = []
    for product, variant_id, variant_product_id, variant_model, variant_color, variant_size in all_prod:
        products_dict.append({
            "Product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "value": product.value
            },
            "variants": [
                {
                    "id": variant_id,
                    "product_id": variant_product_id,
                    "model": variant_model,
                    "color": variant_color,
                    "size": variant_size,
                }
            ]
        })
    return products_dict

@projeto.post("/products")
def create_prod(prod:ProdPyd, prod_var:ProdVarPyd):
    products = Products(
        name = prod.name,
        description = prod.description,
        value = prod.value
    )
    session.add(products)
    session.flush()

    products_var = ProductVariants(
        product_id = products.id,
        model = prod_var.model,
        color = prod_var.color,
        size = prod_var.size
    )
    session.add(products_var)

    session.commit()
    return {"Message": "Product created "}

@projeto.put("/products/{prod_id}")
def update_prod(prod_id: int, prod:ProdPyd, prod_var:ProdVarPyd):
    upd_prod = update(Products).where(Products.id == prod_id).values(
        name = prod.name,
        description = prod.description,
        value = prod.value
    )
    session.execute(upd_prod)

    upd_var = update(ProductVariants).where(ProductVariants.product_id == prod_id).values(
        model = prod_var.model,
        color = prod_var.color,
        size = prod_var.size
    )
    session.execute(upd_var)

    session.commit()
    return {"Message": "Updated product"}

@projeto.delete("/products/{prod_id}")
def delet_prod(prod_id: int):
    session.execute(delete(ProductVariants).where(ProductVariants.product_id == prod_id))
    session.execute(delete(Products).where(Products.id == prod_id))
    session.commit()
    return {"Message": "Deleted product"}