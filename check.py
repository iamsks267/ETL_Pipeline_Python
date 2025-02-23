from sqlalchemy import create_engine
db_uri = "postgresql://postgres:yourpassword@localhost:5433/yourdatabase"

engine = create_engine(db_uri)
connection = engine.connect()
print("Connected Successfully!")
connection.close()
