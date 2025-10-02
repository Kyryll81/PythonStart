"""Added initial data

Revision ID: 2f5425a94817
Revises: 
Create Date: 2025-10-01 22:27:30.666004

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app import app
from db import Record
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'initial_data'
down_revision = '2f5425a94817'
branch_labels = None
depends_on = None


def upgrade():
    with Session(bind=op.get_bind()) as session:
        bind = op.get_bind()
        session = Session(bind=bind)
        r_1 = Record(subject="Programing", teacher="Toravalds", grade=95, date=datetime.utcnow)
        r_2 = Record(subject="Test second subject", teacher="Teacher f", grade=22, date=datetime.utcnow)
        r_3 = Record(subject="Math", teacher="Skinner!", grade=100, date=datetime.utcnow)
        r_4 = Record(subject="Test", teacher="Test", grade=30, date=datetime.utcnow)
        session.add_all([r_1, r_2, r_3, r_4])
        session.commit()

def downgrade():
    # Тут ви можете додати логіку для видалення даних, якщо це потрібно
    pass