"""new fields in user model

Revision ID: e2eaf9e6ec65
Revises: ee3db523fdf5
Create Date: 2020-05-14 04:55:49.518446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2eaf9e6ec65'
down_revision = 'ee3db523fdf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
