import pytest
from app.database import create_user, get_user
from app.bank_app import hash_password
import sqlite3

@pytest.fixture
def test_user():
    """Фикстура создает и удаляет тестового пользователя"""
    # Генерируем хеш пароля
    hashed_password = hash_password("test123")

    # Создаем пользователя
    user = create_user("test_user", hashed_password)

    yield user  # Возвращаем пользователя для теста

    # Очистка после теста
    with sqlite3.connect('bank.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE username = ?', ('test_user',))
        conn.commit()

def test_user_creation(test_user):
    user = get_user("test_user")
    assert user is not None
    assert user['username'] == 'test_user'

def test_password_hashing():
    """Testuje poprawność haszowania haseł"""
    hashed = hash_password("test123")
    assert len(hashed) == 60  # Długość hasha bcrypt
    assert hash_password("test123") != hashed  # Unikalna sól
