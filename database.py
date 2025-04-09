import os

# Use environment variable for production DB URL
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://bookuser:bookpass@localhost/bookdb")
database_url = os.environ.get("DATABASE_URL")