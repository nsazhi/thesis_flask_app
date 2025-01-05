"""initial migrations

Revision ID: ef33ee3d9d07
Revises: 
Create Date: 2025-01-05 15:05:40.777304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef33ee3d9d07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_categories_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_categories_slug'), ['slug'], unique=True)

    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('release', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('director', sa.String(), nullable=False),
    sa.Column('actors', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('is_viewed', sa.Boolean(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_films_category_id'), ['category_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_films_country'), ['country'], unique=False)
        batch_op.create_index(batch_op.f('ix_films_genre'), ['genre'], unique=False)
        batch_op.create_index(batch_op.f('ix_films_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_films_is_viewed'), ['is_viewed'], unique=False)
        batch_op.create_index(batch_op.f('ix_films_slug'), ['slug'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('films', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_films_slug'))
        batch_op.drop_index(batch_op.f('ix_films_is_viewed'))
        batch_op.drop_index(batch_op.f('ix_films_id'))
        batch_op.drop_index(batch_op.f('ix_films_genre'))
        batch_op.drop_index(batch_op.f('ix_films_country'))
        batch_op.drop_index(batch_op.f('ix_films_category_id'))

    op.drop_table('films')
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_categories_slug'))
        batch_op.drop_index(batch_op.f('ix_categories_id'))

    op.drop_table('categories')
    # ### end Alembic commands ###
