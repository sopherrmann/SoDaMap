"""change routing relations

Revision ID: 75611c5b2dd4
Revises: 86697f03e85b
Create Date: 2019-11-29 18:06:25.152144

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '75611c5b2dd4'
down_revision = '86697f03e85b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mapped_session', 'session_type',
                    existing_type=postgresql.ENUM('mapped', 'web', name='sessiontype'),
                    nullable=False)
    op.drop_constraint('routing_destination_text_with_sug_id_fkey', 'routing_destination', type_='foreignkey')
    op.drop_column('routing_destination', 'text_with_suggestion_id')
    op.drop_constraint('routing_origin_text_with_sug_id_fkey', 'routing_origin', type_='foreignkey')
    op.drop_column('routing_origin', 'text_with_suggestion_id')
    op.add_column('text_with_suggestion', sa.Column('routing_destination_id', sa.Integer(), nullable=True))
    op.add_column('text_with_suggestion', sa.Column('routing_origin_id', sa.Integer(), nullable=True))
    op.create_foreign_key('text_with_sug_routing_destination_id_fkey', 'text_with_suggestion', 'routing_destination', ['routing_destination_id'], ['id'])
    op.create_foreign_key('text_with_sug_routing_origin_id_fkey', 'text_with_suggestion', 'routing_origin', ['routing_origin_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('text_with_sug_routing_origin_id_fkey', 'text_with_suggestion', type_='foreignkey')
    op.drop_constraint('text_with_sug_routing_destination_id_fkey', 'text_with_suggestion', type_='foreignkey')
    op.drop_column('text_with_suggestion', 'routing_origin_id')
    op.drop_column('text_with_suggestion', 'routing_destination_id')
    op.add_column('routing_origin', sa.Column('text_with_suggestion_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('routing_origin_text_with_sug_id_fkey', 'routing_origin', 'text_with_suggestion', ['text_with_suggestion_id'], ['id'])
    op.add_column('routing_destination', sa.Column('text_with_suggestion_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('routing_destination_text_with_sug_id_fkey', 'routing_destination', 'text_with_suggestion', ['text_with_suggestion_id'], ['id'])
    op.alter_column('mapped_session', 'session_type',
                    existing_type=postgresql.ENUM('mapped', 'web', name='sessiontype'),
                    nullable=True)
    # ### end Alembic commands ###
