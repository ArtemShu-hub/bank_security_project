import pytest
from app import hash_password, get_user, create_user  # Usunięto duplikat importu

@pytest.fixture
def test_user():
    create_user("test_user", hash_password("test123"))  # Poprawiona składnia
    yield
    # Czyszczenie zostanie dodane później

def test_password_hashing():
    """Testuje poprawność haszowania haseł"""
    hashed = hash_password("test123")
    assert len(hashed) == 60  # Długość hasha bcrypt
    assert hash_password("test123") != hashed  # Unikalna sól

def test_user_creation(test_user):
    """Testuje tworzenie użytkownika"""
    user = get_user("test_user")
    assert user is not None
    assert user['username'] == 'test_user'