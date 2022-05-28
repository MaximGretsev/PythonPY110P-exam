import random
import json

from faker import Faker

from conf import model

fake_ru = Faker("ru_RU")
random_books = {}


def main():
    fields(2)


def fields(count_) -> dict:
    """

    :param count_:
    :return:
    """
    for i in range(count_, 101):
        random_books[i] = {
            "model": model,
            "pk": i,
            "fields": {
                "title": title(),
                "year": years(),
                "pages": pages(),
                "isbn13": isbn(),
                "rating": rating(),
                "price": prices(),
                "author": author()
            }
        }
    with open("result.json", 'w', encoding='utf8') as file:
        json.dump(random_books, file, indent=4, ensure_ascii=False)
    count_ += 1

    return random_books


def title() -> str:
    list_of_the_books = "books.txt"
    with open(list_of_the_books, 'r', encoding='utf8') as f:
        books_list = f.readlines()
        return random.choice(books_list).strip()


def years() -> int:
    year = random.randint(999, 2022)
    return year


def pages() -> int:
    full_pages = random.randint(100, 2000)
    return full_pages


def isbn() -> int:
    """

    :return:
    """
    fake_isbn = fake_ru.isbn13()
    return fake_isbn


def rating() -> str:
    rate = random.uniform(1.0, 5.1)
    return f"{rate:.1f}"


def prices() -> str:
    price = random.uniform(100.0, 10000.0)
    return f"{price:.1f}"


def author() -> list:
    list_of_authors = []
    for i in range(random.randint(1, 3)):
        fake_name = fake_ru.name()
        list_of_authors.append(fake_name)
    return list_of_authors


if __name__ == "__main__":
    main()