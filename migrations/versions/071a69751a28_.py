"""empty message

Revision ID: 071a69751a28
Revises: 2fc1d1c5f9e4
Create Date: 2018-12-15 22:04:06.823563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '071a69751a28'
down_revision = '2fc1d1c5f9e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('event_dates_event_id_fkey', 'event_dates', type_='foreignkey')
    op.drop_column('event_dates', 'event_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event_dates', sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('event_dates_event_id_fkey', 'event_dates', 'events', ['event_id'], ['id'])
    # ### end Alembic commands ###
