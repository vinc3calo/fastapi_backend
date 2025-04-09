import os

# Use environment variable for production DB URL
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://bookuser:bookpass@localhost/bookdb")


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL (recommended for production)
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/dbname")
database_url = os.environ.get("DATABASE_URL")

# Creating the engine to interact with PostgreSQL
engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to create tables
Base = declarative_base()
