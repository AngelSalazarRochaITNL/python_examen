"""empty message

Revision ID: e62d7dc2f99f
Revises: 
Create Date: 2023-04-21 07:39:27.547487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e62d7dc2f99f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('camino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_camino', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mision',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_mision', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('npc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_npc', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_personaje', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ruta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_ruta', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ruta')
    op.drop_table('personaje')
    op.drop_table('npc')
    op.drop_table('mision')
    op.drop_table('camino')
    # ### end Alembic commands ###
