import pytest
from snagem.db import session
from snagem.db.model import media as model


@pytest.fixture(autouse=True, scope="package")
def apply_migrations() -> None:
    session.upgrade()


@pytest.fixture(autouse=True, scope="module")
def nuke_assets() -> None:
    with session.get() as db:
        db.query(model.Media).delete()
        db.commit()
