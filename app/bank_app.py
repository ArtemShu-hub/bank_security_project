from app.database import init_db, get_user, create_user
import bcrypt
import getpass  # Do ukrytego wprowadzania hasła
from app.database import init_db

def main():
    init_db()
    print("Baza danych zainicjalizowana!")

if __name__ == "__main__":
    from app.database import init_db
    init_db()

def hash_password(password: str) -> str:
    """Haszowanie hasła"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def register():
    username = input("Wprowadź nazwę użytkownika: ")
    password = getpass.getpass("Wprowadź hasło: ")

    if get_user(username):
        print("Błąd: użytkownik już istnieje")
        return

    if create_user(username, hash_password(password)):
        print("Użytkownik zarejestrowany pomyślnie!")
    else:
        print("Błąd podczas rejestracji")

def login():
    username = input("Nazwa użytkownika: ")
    password = getpass.getpass("Hasło: ")

    user = get_user(username)
    if not user:
        print("Błąd: użytkownik nie znaleziony")
        return

    if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        print("Logowanie udane!")
    else:
        print("Nieprawidłowe hasło")

if __name__ == "__main__":
    init_db()

    while True:
        print("\n1. Rejestracja\n2. Logowanie\n3. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break