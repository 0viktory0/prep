# Написать вложенную схему валидации данных, получить ошибки валидации
# Экспортировать данные в формат JSON с помощью Pydantic
# Прочитать данные из JSON с помощью Pydantic

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    year_published: int

class Author(BaseModel):
    name: str
    last_name: str
    books: list[Book]


if __name__ == '__main__':
    data = {
        "name": "Михаил",
        "last_name": "Булгаков",
        "books": [
            {
                "title": "Мастер и Маргарита",
                "year_published": 1966
            },
            {
                "title": "Собачье сердце",
                         "year_published": 1987
             }
        ]
    }


    try:
        author = Author(**data)
        print("Данные валидны")
        #print("Выводим данные в json", author.json(ensure_ascii=False))
    except Exception as e:
        print("Произошла ошибка валидации данных:", e)

   # Экспортировать данные в формат JSON с помощью Pydantic
    json_data = author.json()

    # Прочитать данные из JSON с помощью Pydantic
    author_object = Author.parse_raw(json_data)

    print("Имя автора:", author_object.name)
    print("Фамилия автора:", author_object.last_name)
    print("Книги:", author_object.books)




