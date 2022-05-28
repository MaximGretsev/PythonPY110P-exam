import itertools
import random
import json

from faker import Faker

from conf import model

fake_ru = Faker("ru_RU")
random_books = {}

# start = int(input("Enter start number: "))
# finish = int(input("Enter finish number: "))
start = 1
finish = 100


def main():
    iter_ = fields(start)
    for _ in range(start, finish + 1):
        try:
            next(iter_)
        except:
            TypeError("Я кончился")


def fields(count_):
    """

    :param count_:
    :return:
    """
    while count_ < finish:
        random_books[count_] = {
            "model": model,
            "pk": count_,
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
        with open("result_gen.json", 'w+', encoding='utf8') as file:
            json.dump(random_books, file, indent=4, ensure_ascii=False)

        yield random_books
        count_ += 1


def title() -> str:
    """

    :return:
    """
    list_of_the_books = "books.txt"
    with open(list_of_the_books, 'r', encoding='utf8') as f:
        books_list = f.readlines()
        return random.choice(books_list).strip()


def years() -> int:
    """

    :return:
    """
    year = random.randint(999, 2022)
    return year


def pages() -> int:
    """

    :return:
    """
    full_pages = random.randint(100, 2000)
    return full_pages


def isbn() -> int:
    """

    :return:
    """
    fake_isbn = fake_ru.isbn13()
    return fake_isbn


def rating() -> str:
    """

    :return:
    """
    rate = random.uniform(1.0, 5.1)
    return f"{rate:.1f}"


def prices() -> str:
    """

    :return:
    """
    price = random.uniform(100.0, 10000.0)
    return f"{price:.1f}"


def author() -> list:
    """

    :return:
    """
    list_of_authors = []
    for i in range(random.randint(1, 3)):
        fake_name = fake_ru.name()
        list_of_authors.append(fake_name)
    return list_of_authors


if __name__ == "__main__":
    main()
