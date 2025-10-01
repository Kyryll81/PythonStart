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
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with Session(bind=op.get_bind()) as session:
        with app.app_context():
            # Додавання початкових даних
            r_1 = Record(subject="Programing", teacher="Toravalds", grade=95, date=datetime.now())
            r_2 = Record(subject="Test second subject", teacher="Teacher f", grade=22, date=datetime.now())
            r_3 = Record(subject="Math", teacher="Skinner!", grade=100, date=datetime.now())
            r_4 = Record(subject="Test", teacher="Test", grade=30, date=datetime.now())
            session.add_all([r_1, r_2, r_3, r_4])
            session.commit()

def downgrade():
    # Тут ви можете додати логіку для видалення даних, якщо це потрібно
    pass