"""
Environment variables tests
"""
import pytest


def test_service_name_is_set(service_ms_name):
    """
    Verifica se o nome do microservice está configurado nas variaveis de ambiente
    """
    assert service_ms_name is not None


def test_service_env_is_set(service_ms_env):
    """
    Verifica se o ambiente do ms está configurado nas variaveis de ambiente
    """
    assert service_ms_env is not None
