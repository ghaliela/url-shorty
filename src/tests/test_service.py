import pytest

from ..app import service

@pytest
def test_shouldd_create_short_hash_with_6_characters():
    long_url = "https://www.example.com"
    short_hash = service.create_short_hash(long_url) 
    assert short_hash == "123456"

@pytest
def test_should_create_short_hash_with_7_characters_if_collision():
    long_url = "https://www.example.com"
    short_hash = service.create_short_hash(long_url) 
    assert short_hash == "1234567"

@pytest
def test_should_create_short_hash_with_8_characters_if_2_collisions():
    long_url = "https://www.example.com"
    short_hash = service.create_short_hash(long_url) 
    assert short_hash == "12345678"

@pytest
def test_should_return_same_short_hash_if_long_url_exists():
    long_url = "https://www.example.com"
    short_hash = service.create_short_hash(long_url) 
    assert short_hash == "123456"
