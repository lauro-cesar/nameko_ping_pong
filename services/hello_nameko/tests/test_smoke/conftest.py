"""

Conftest for HelloWorld Smoke Tests

"""
import pytest
import os
import logging


@pytest.fixture(autouse=True, scope="module")
def service_ms_name():
    return os.getenv("MICROSERVICE_NAME", None)


@pytest.fixture(autouse=True, scope="module")
def service_ms_env():
    return os.getenv("MICROSERVICE_ENVIRONMENT", None)
