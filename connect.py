from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker 

# location of where our database is going to be
engine = create_engine(
    "sqlite:///site.db", echo=True    
)

Session = sessionmaker(bind=engine)

db = Session()


# with engine.connect() as conn:
#     result = conn.execute(
#         text("select 'hello'")
#     )
#     print(result.all())