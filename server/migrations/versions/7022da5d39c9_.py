"""empty message

Revision ID: 7022da5d39c9
Revises: 
Create Date: 2024-04-09 14:34:20.569642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7022da5d39c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('developer', sa.String(), nullable=False),
    sa.Column('publisher', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('game_platform',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('game_id', sa.String(), nullable=True),
    sa.Column('platform_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name=op.f('fk_game_platform_game_id_game')),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], name=op.f('fk_game_platform_platform_id_platform')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name=op.f('fk_game_profile_game_id_game')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_game_profile_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_profile')
    op.drop_table('game_platform')
    op.drop_table('user')
    op.drop_table('platform')
    op.drop_table('game')
    # ### end Alembic commands ###
