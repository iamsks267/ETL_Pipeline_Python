from sqlalchemy import create_engine
db_uri = "postgresql://postgres:Bsk123@localhost:5433/Learn"

engine = create_engine(db_uri)
connection = engine.connect()
print("Connected Successfully!")
connection.close()
