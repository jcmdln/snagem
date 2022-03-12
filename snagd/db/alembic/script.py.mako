# SPDX-License-Identifier: AGPL-3.0-or-later

import sqlalchemy as sa

from alembic import op

${imports if imports else ""}

# revision identifiers, used by Alembic.
branch_labels = ${repr(branch_labels)}
create_date = "${create_date}"
depends_on = ${repr(depends_on)}
down_revision = ${repr(down_revision)}
revision = ${repr(up_revision)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
