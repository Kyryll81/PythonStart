from datetime import datetime

from sqlalchemy import Float, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Record(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    subject: Mapped[str] = mapped_column(String(50), nullable=False)
    teacher: Mapped[str] = mapped_column(String(50), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    date: Mapped[datetime] = mapped_column(Date, nullable=False, default=datetime.now())


