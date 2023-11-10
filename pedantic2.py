# Написать вложенную схему валидации переменных окружения (настройки приложения), получить ошибки валидации

from pydantic import BaseSettings


class Settings(BaseSettings):
    name: str
    password: str
    DEBUG: bool
    SECRET_KEY: str
    ALLOWED_HOSTS: list[str] = []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


try:
    settings = Settings()

    print("Переменные окружения валидны:", settings.json())
except Exception as e:
    print("Произошла ошибка валидации переменных окружения:", e)

