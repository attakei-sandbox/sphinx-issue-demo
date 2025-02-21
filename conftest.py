import pytest
from sphinx.testing.path import path

pytest_plugins = ["sphinx.testing.fixtures"]

# Patch
path.is_dir = path.isdir


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "root"
