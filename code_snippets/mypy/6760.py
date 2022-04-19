from pathlib import Path

@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / 'test.db'
