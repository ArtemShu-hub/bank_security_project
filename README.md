Projekt Bankowy - System Bezpieczeństwa
Aplikacja CLI do zarządzania bezpieczeństwem transakcji bankowych.

🚀 Jak uruchomić projekt?
Wymagania
Python 3.9+

Zainstalowane zależności:

bash
pip install -r requirements.txt
Zalecany sposób (modułowy)
bash
python -m app.bank_app
Alternatywny sposób (bezpośredni)
Dodaj ścieżkę do projektu w zmiennej PYTHONPATH:
Windows (PowerShell):

bash
$env:PYTHONPATH = "B:\projects\bank_security_project"
python app/bank_app.py
Linux/macOS:

bash
export PYTHONPATH="/ścieżka/do/projektu"
python app/bank_app.py
⚠️ Typowe problemy
ModuleNotFoundError: No module named 'app'
→ Użyj uruchomienia modułowego (python -m) lub ustaw PYTHONPATH.

Ostrzeżenie RuntimeWarning
→ Dodaj w bank_app.py:

python
if __name__ == "__main__":
main()
📁 Struktura projektu
bank_security_project/
├── app/
│   ├── __init__.py
│   ├── bank_app.py      # Główny skrypt
│   ├── database.py      # Połączenia z bazą danych
│   └── ...
├── requirements.txt
└── README.md
🔄 Dodatkowe informacje
Środowisko wirtualne:

bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
Dlaczego python -m?
Zapewnia poprawne działanie importów względnych wewnątrz pakietu app.

Uwaga dla developerów:
Wszelkie nowe funkcje powinny być testowane w środowisku wirtualnym.

Problemy z importami najczęściej wynikają z nieprawidłowych ścieżek Pythona.