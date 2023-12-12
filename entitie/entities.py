from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey

Base = declarative_base()

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(120), nullable=False)
    value = Column(Float, nullable=False)

class ProductVariants(Base):
    __tablename__ = 'products_variants'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    model = Column(String(40), nullable=False)
    color = Column(String(20), nullable=False)
    size = Column(String(40), nullable=False)