from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db = SQLAlchemy()

class Contact(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    
    
    def __str__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, phone={self.phone}, email={self.email})"
