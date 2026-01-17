import os


def log_message(message: str):
    os.write(1, f"{message}\n".encode())
