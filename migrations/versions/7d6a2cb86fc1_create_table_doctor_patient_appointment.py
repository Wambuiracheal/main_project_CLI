"""create table doctor,patient,appointment

Revision ID: 7d6a2cb86fc1
Revises: 762bf343ac7d
Create Date: 2024-12-18 10:07:08.983729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d6a2cb86fc1'
down_revision: Union[str, None] = '762bf343ac7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('age', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'age')
    # ### end Alembic commands ###
