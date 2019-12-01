"""add where_clicked col

Revision ID: 4b8cdd0b7f42
Revises: 75611c5b2dd4
Create Date: 2019-12-01 22:48:05.897537

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geometry


# revision identifiers, used by Alembic.
revision = '4b8cdd0b7f42'
down_revision = '75611c5b2dd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('map_interaction', sa.Column('where_clicked_geom', Geometry(geometry_type='POINT', srid=4326), nullable=True))
    op.add_column('map_interaction', sa.Column('where_clicked_time_stamp', sa.DateTime(), nullable=True))
    op.alter_column('question', 'answer',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'answer',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('map_interaction', 'where_clicked_time_stamp')
    op.drop_column('map_interaction', 'where_clicked_geom')
    # ### end Alembic commands ###
