import pytest
import os
import tempfile
import shutil


@pytest.fixture
def tempdir(scope="module"):
    # contextmanager to generate and delete a temporary directory
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)


@pytest.fixture
def testdata_fixture(scope="module"):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdata")
