import pytest

import snagem.db.model.media as model
from snagem.db import session


@pytest.fixture(autouse=True, scope="package")
def apply_migrations() -> None:
    session.upgrade()


@pytest.fixture(autouse=True, scope="module")
def nuke_assets() -> None:
    with session.session() as db:
        db.query(model.Media).delete()
        db.commit()