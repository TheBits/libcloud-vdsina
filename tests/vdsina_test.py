import os

import pytest
import vcr

from vdsinadriver import VdsinaDriver


@pytest.fixture()
def vdsina_key() -> str:
    key = os.getenv("VDSINA_TOKEN")
    if key is None:
        pytest.exit("set up VDSINA_TOKEN environment variable")
    return str(key)


@pytest.fixture()
def compute_conn(vdsina_key):
    conn = VdsinaDriver(key=vdsina_key)
    return conn


@vcr.use_cassette("./tests/fixtures/list_key_pairs.yaml", filter_headers=["Authorization"])
def test_list_key_pairs(compute_conn):
    keys = compute_conn.list_key_pairs()
    key = keys.pop()
    assert key.name == "x200s"
    assert key.fingerprint == "ca:28:dc:6e:9e:72:48:d3:bc:73:76:19:d2:5f:c3:e8"
    assert isinstance(key.driver, VdsinaDriver)
    assert key.extra["id"] == 46329
