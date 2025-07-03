import pytest
from app.services.cache import cache

def test_cache_set_and_get():
    cache.set("key123", {"result": "ok"})
    assert cache.get("key123") == {"result": "ok"}

def test_cache_miss_returns_none():
    assert cache.get("nao_existe") is None
