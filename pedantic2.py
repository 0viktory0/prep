# Написать вложенную схему валидации переменных окружения (настройки приложения), получить ошибки валидации

from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    name: str
    password: str

class DjangoSettings(BaseModel):
    DEBUG: bool
    SECRET_KEY: str
    DATABASE: DatabaseSettings
    ALLOWED_HOSTS: list[str] = []


data = {
    "DEBUG": "True",
    "SECRET_KEY": "mysecretkey",
    "DB_NAME": "mydb",
    "DB_PASSWORD": "mypassword",
    "ALLOWED_HOSTS": "localhost,127.0.0.1",
}


try:
    django_settings = DjangoSettings(
        DEBUG=bool(data["DEBUG"]),
        SECRET_KEY=data["SECRET_KEY"],
        DATABASE=DatabaseSettings(
            name=data["DB_NAME"],
            password=data["DB_PASSWORD"],
        ),
        ALLOWED_HOSTS=data["ALLOWED_HOSTS"].split(",")
    )
    print("Переменные окружения валидны:", django_settings.json())
except Exception as e:
    print("Произошла ошибка валидации переменных окружения:", e)

