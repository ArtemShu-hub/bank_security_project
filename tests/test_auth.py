import pytest
from app.database import create_user, get_user
from app.bank_app import hash_password

@pytest.fixture
def test_user():
    
    user = create_user("test_user", hash_password("test123"))
    yield user  # Возвращаем созданного пользователя


def test_user_creation(test_user):  # Фикстура передается как параметр

    user = get_user("test_user")
    assert user is not None
    assert user['username'] == 'test_user'

def test_password_hashing():
    """Testuje poprawność haszowania haseł"""
    hashed = hash_password("test123")
    assert len(hashed) == 60  # Długość hasha bcrypt
    assert hash_password("test123") != hashed  # Unikalna sól

