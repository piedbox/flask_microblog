"""new field in user model

Revision ID: 50f396a706c4
Revises: 4b03bd4dddb0
Create Date: 2019-04-05 15:33:53.473522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f396a706c4'
down_revision = '4b03bd4dddb0'
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