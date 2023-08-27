"""Remove knoeledge table

Revision ID: 33370fc43253
Revises: 356d1029e182
Create Date: 2023-08-27 17:28:08.613584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33370fc43253'
down_revision: Union[str, None] = '356d1029e182'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
