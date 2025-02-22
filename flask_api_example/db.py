from fastapi import FastAPI

from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker,declarative_base

# Update the DATABASE_URL with your actual username and password
DATABASE_URL = "mysql://fastserver:Kishore123$@localhost/products"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print(SessionLocal)
Base = declarative_base()

# Define the Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Updated length to match your table
    category = Column(String(40))            # New field for category
    price = Column(Numeric(10, 2))          # Updated to use Numeric for decimal
    tag = Column(String(30))                 # New field for tag

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/products/")
def read_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

@app.post("/products/")
def create_product(name: str, category: str, price: float, tag: str):
    db = SessionLocal()
    new_product = Product(name=name, category=category, price=price, tag=tag)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()
    return new_product
    
    
    
