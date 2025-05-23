from cryptography.fernet import Fernet
import os

class CryptoService:
    def __init__(self):
        self.key = self._load_or_generate_key()

    def _load_or_generate_key(self):
        """Wczytuje lub generuje klucz szyfrowania"""
        key_file = 'encryption.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key

    def encrypt_file(self, input_path, output_path):
        """Szyfruje plik"""
        cipher = Fernet(self.key)
        with open(input_path, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(output_path, 'wb') as f:
            f.write(encrypted)

    def decrypt_file(self, input_path, output_path):
        """Deszyfruje plik"""
        cipher = Fernet(self.key)
        with open(input_path, 'rb') as f:
            encrypted = f.read()
        decrypted = cipher.decrypt(encrypted)
        with open(output_path, 'wb') as f:
            f.write(decrypted)