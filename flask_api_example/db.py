from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker,declarative_base
# 1. Load the .env file
load_dotenv()

# 2. Get the FULL URL directly from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if it loaded correctly (optional debug print)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found. Make sure .env is in the same folder.")
# Update the DATABASE_URL with your actual username and password
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}/{dbname}"

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
    
    
    
