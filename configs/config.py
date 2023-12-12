from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:mysql@172.188.0.3:3306/estagio")
Session = sessionmaker(bind=engine)
session = Session()