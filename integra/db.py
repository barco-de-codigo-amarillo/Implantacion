from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://usuario:P455w0rd@localhost:5432/Ada"
engine = create_engine(DATABASE_URL, echo=True)

# la clase base para los modelos
Base = declarative_base()

# modelo (tabla)
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', email='{self.email}')>"

# tablas en la base de datos
Base.metadata.create_all(engine)

# una sesión para hacer consultas
Session = sessionmaker(bind=engine)
session = Session()