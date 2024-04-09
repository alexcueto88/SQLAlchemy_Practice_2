from connect import engine
from models import Base, Program, Course

# print(f"getting metadata ....")
Base.metadata.create_all(bind=engine)


# once you run createdb.py, this will create tables