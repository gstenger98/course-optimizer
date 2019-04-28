"""adding title column to courses

Revision ID: adabd9a4d224
Revises: 027734e17f7a
Create Date: 2019-04-28 00:04:56.521498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adabd9a4d224'
down_revision = '027734e17f7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('title', sa.String(length=100)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'title')
    # ### end Alembic commands ###