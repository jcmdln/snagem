# SPDX-License-Identifier: AGPL-3.0-or-later

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
branch_labels = None
create_date = "2022-03-28 03:22:15.005856+00:00"
depends_on = None
down_revision = None
revision = "8cc1e0b83c3b"


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "media",
        sa.Column("uuid", sa.String(), nullable=False),
        sa.Column("categories", sa.String(), nullable=True),
        sa.Column("date_created", sa.DateTime(), nullable=False),
        sa.Column("date_updated", sa.DateTime(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("source_url", sa.String(), nullable=False),
        sa.Column("subtitles", sa.String(), nullable=True),
        sa.Column("tags", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("views", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("media")
    # ### end Alembic commands ###
