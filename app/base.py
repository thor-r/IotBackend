from sqlalchemy.orm import declarative_base

# I am doiing this here so there is a global point of reference for the base class before database.py and models.py need it. 
Base = declarative_base()