from typing import Optional
import os
import sqlite3
from datetime import datetime
from app.crypto import CryptoService  # Upewnij się, że plik crypto.py istnieje

def init_db():
    conn = sqlite3.connect('bank.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Pozostałe funkcje bez zmian

def get_user(username: str) -> Optional[dict]:
    """Pobiera dane użytkownika"""
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return {'id': user[0], 'username': user[1], 'password_hash': user[2]} if user else None

def create_user(username: str, password_hash: str) -> bool:
    """Tworzy nowego użytkownika"""
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                       (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  # Jeśli użytkownik już istnieje
        return False
    finally:
        conn.close()

def create_backup():
    """Tworzy zaszyfrowaną kopię zapasową bazy danych"""
    try:
        # Tworzy folder na kopie zapasowe, jeśli nie istnieje
        if not os.path.exists('backups'):
            os.makedirs('backups')

        # Generuje nazwę pliku z timestampem
        backup_path = f'backups/backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'

        # Tworzy kopię zapasową
        conn = sqlite3.connect('bank.db')
        with open(backup_path, 'wb') as f:
            for line in conn.iterdump():
                f.write(f'{line}\n'.encode('utf-8'))

        # Szyfruje i usuwa oryginał
        crypto = CryptoService()
        crypto.encrypt_file(backup_path, backup_path + '.enc')
        os.remove(backup_path)

        print(f"Kopia zapasowa utworzona: {backup_path}.enc")
        return True
    except Exception as e:
        print(f"Błąd podczas tworzenia kopii zapasowej: {e}")
        return False

def increment_failed_attempts(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            'UPDATE users SET attempts = attempts + 1 WHERE username = ?',
            (username,)
        )
        conn.commit()
    finally:
        conn.close()

def add_transaction(user_id, amount, description):
    try:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO transactions (user_id, amount, description) 
            VALUES (?, ?, ?)
        ''', (user_id, amount, description))

        conn.commit()

        print("Transakcja dodana pomyślnie")
        return True

    except sqlite3.Error as e:
        print(f"Błąd podczas dodawania transakcji: {e}")
        return False

    finally:
        if conn:
            conn.close()

def init_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
''')
    conn.commit()
    conn.close()