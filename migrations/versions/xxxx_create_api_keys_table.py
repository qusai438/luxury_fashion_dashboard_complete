"""create api_keys table"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxx_create_api_keys_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'api_keys',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('service_name', sa.String(length=50), nullable=False, unique=True),
        sa.Column('key_value', sa.Text(), nullable=False)
    )


def downgrade():
    op.drop_table('api_keys')
