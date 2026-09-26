import math
from typing import Any


movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies: list[dict[str, Any]]) -> float:
    """
    Функция возвращает среднюю оценку по каталогу фильмов.

    Args:
        movies (list[dict]): Список фильмов, каждый фильм представляет собой словарь аттрибутов 
            словарь должен содержать ключ "rating" - по нему считается средняя оценка

    Returns:
        float: Средняя оценка, округленная до одного знака после запятой
    """
    rate_sum = 0.0
    for movie in movies:
        rate_sum += movie.get("rating", 0.0)

    movies_count = len(movies)
    if movies_count > 0:
        average = rate_sum / movies_count
    else:
        average = 0

    return round(average, 1)


def catalog_age_stats(movies: list[dict[str, Any]], current_year:int=2026) -> tuple[int, int, int]:
    """
    Функция возвращает кортеж: (самый старый фильм в годах, самый новый фильм в годах, среднее)

    Args:
        movies (list[dict]): Список фильмов, каждый фильм представляет собой словарь аттрибутов 
            словарь должен содержать ключ "year" - по нему считается возраст фильма

    Returns:
        tuple[int, int, int]: кортеж: (самый старый фильм в годах, самый новый фильм в годах, среднее), где среднее округлено вверх до целого."""
    years = []
    years_sum = 0
    for movie in movies:
        movie_year = movie.get("year")
        if movie_year is not None:
            diff = current_year - movie_year
            years.append(diff)
            years_sum += diff

    movies_count = len(movies)
    if movies_count > 0:
        average = years_sum / movies_count
    else:
        average = 0

    return (max(years), min(years), math.ceil(average))


def duration_in_hours(minutes: int) -> str:
    """Функция переводит количество минут в строку формата "2ч 35м"."""
    hours = minutes // 60
    minutes_rest = minutes - hours*60
    return f"{hours}ч {minutes_rest}м"


print(average_rating(movies))
print(catalog_age_stats(movies))
print(duration_in_hours(movies[0]["duration_min"]))
