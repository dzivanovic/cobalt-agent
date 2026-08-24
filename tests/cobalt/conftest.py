"""Override the repo-root autouse psycopg mock for the new-core tests.

The root conftest patches psycopg.connect globally (module attribute), so
without this override the store 'integration' test would run against a
MagicMock and pass/fail meaninglessly. cobalt/ tests use the real
cobalt_dev database (integration-marked) or no DB at all.
"""

import pytest


@pytest.fixture(autouse=True)
def mock_postgres_memory():
    yield
