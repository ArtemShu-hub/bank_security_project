import sqlite3
from decimal import Decimal  # Do precyzyjnych obliczeń finansowych

class TransactionService:
    @staticmethod
    def update_balance(user_id: int, amount: Decimal) -> bool:
        """Aktualizuje saldo + zapisuje transakcję"""
        try:
            with sqlite3.connect('bank.db') as conn:
                cursor = conn.cursor()

                # Weryfikacja użytkownika
                cursor.execute('SELECT 1 FROM users WHERE id = ?', (user_id,))
                if not cursor.fetchone():
                    raise ValueError("Użytkownik nie znaleziony")

                # Dla wypłat: sprawdzenie salda
                if amount < 0:
                    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
                    current_balance = Decimal(cursor.fetchone()[0])
                    if current_balance + amount < 0:
                        raise ValueError("Niewystarczające środki")

                # 1. Aktualizacja salda
                cursor.execute(
                    'UPDATE users SET balance = balance + ? WHERE id = ?',
                    (str(amount), user_id)
                )

                # 2. Zapis transakcji (NOWE)
                cursor.execute('''
                INSERT INTO transactions (user_id, amount, type)
                VALUES (?, ?, ?)
            ''', (
                    user_id,
                    str(amount),
                    'wpłata' if amount > 0 else 'wypłata'
                ))

                conn.commit()
                return True

        except sqlite3.Error as e:
            print(f"Błąd bazy danych: {e}")
            conn.rollback()  # Wycofanie zmian w przypadku błędu
            return False


    def deposit(user_id: int, amount: Decimal) -> bool:
        """Wpłata na konto"""
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia")
        return TransactionService.update_balance(user_id, amount)


    def withdraw(user_id: int, amount: Decimal) -> bool:
        """Wypłata środków"""
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia")
        return TransactionService.update_balance(user_id, -amount)