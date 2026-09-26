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


def rating_tier(rating: float) -> str:
    """Функция по оценке возвращает категорию."""
    category = None
    if rating < 5:
        category = "слабо"
    elif rating < 7:
        category = "средне"
    elif rating < 9:
        category = "хорошо"
    elif rating >= 9:
        category = "шедевр"
    return category if category is not None else "не возможно определить"


def decade_label(year: int) -> str:
    """Функция возвращает метку по возрасту фильма: "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015)."""
    match year:
        case (year) if year < 2015:
            return "старые"
        case (year) if year >= 2015 and year <= 2020:
            return "недавние"
        case (year) if year > 2020:
            return "новые"
        case _:
            return ""


def print_not_comedy_films(movies: list[dict[str, Any]]) -> None:
    """Функция выводит в консоль названия всех фильмов, не относящихся к жанру 'comedy'."""
    for movie in movies:
        if "comedy" in movie.get("genres", []):
            continue
        else:
            print(movie.get("title"))


def print_first_exelent_movie(movies: list[dict[str, Any]]) -> None:
    """Функция выводит в консоль первого фильма с рейтингом 9.0 или сообщение "Шедевров не найдено"."""
    i = 0
    while i < len(movies):
        if movies[i].get("rating", 0) > 9:
            print(movies[i].get("title", None))
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies: list[dict[str, Any]], treshold: int = 120) -> int:
    """Функция считает количество фильмов с продолжительностью больше, чем `treshold`."""
    long_movies_cnt = 0
    for movie in movies:
        if movie.get("duration_min", 0) > treshold:
            long_movies_cnt += 1

    return long_movies_cnt


def normalize_title(title: str) -> str:
    """Функция нормализует название фильма к формату Title Case."""
    normalize_words = []
    for word in title.split(" "):
        normalize_words.append(word[0].upper() + word[1:].lower())

    return " ".join(normalize_words)


def make_slug(title: str) -> str:
    """Функция преобразует нормализованное название в слаг вида the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie) -> str:
    """Функция возвращает строку с полным описанием фильма."""
    title = normalize_title(movie.get("title", ""))
    year = movie.get("year", 1111)
    rate = movie.get("rating", 0.0)
    time = duration_in_hours(movie.get("duration_min", 0))
    genres = ", ".join(sorted(movie.get("genres", [])))

    return f'"{title}" ({year}) - {rate}/10, {time}, жанры: {genres}'


def titles_sorted_by_rating(movies: list[dict[str, Any]]) -> list[str]:
    """Функция возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    movies_copy = [{"title": m["title"], "rating": m["rating"]} for m in movies]
    movies_copy.sort(key=lambda m: m["rating"], reverse=True)
    result = [movie.get("title", "") for movie in movies_copy]

    return result


def top_n_by_rating(movies: list[dict[str, Any]], n : int = 3) -> list[tuple[str, float]]:
    """Функция возвращает список кортежей (title, rating) - топ по рейтингу."""
    movies_copy = [{"title": m["title"], "rating": m["rating"]} for m in movies]
    movies_copy.sort(key=lambda m: m["rating"], reverse=True)
    result = [(movie.get("title", ""), movie.get("rating", 0.0)) for movie in movies_copy]

    return result[0:n+1]


def count_by_genre(movies: list[dict[str, Any]]) -> dict[str, int]:
    """Функция возвращает словарь {жанр: количество фильмов}."""
    result = {}
    for movie in movies:
        genres = movie["genres"]
        for genre in genres:
            result[genre] = result.get(genre, 0) + 1

    return result


def actor_filmography(movies: list[dict[str, Any]]) -> dict[str, int]:
    """Функция возвращает словарь {актер: [список названий фильмов]}."""
    result = {}
    for movie in movies:
        actors = movie["actors"]
        for actor in actors:
            movies_list = result.get(actor, [])
            movies_list.append(movie["title"])
            result[actor] = movies_list

    return result


def get_rating_movies(movies: list[dict[str, Any]]) -> dict[str, str]:
    """Функция строит словарь {title: rating} для фильмов с рейтингом выше среднего."""
    average_rate = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > average_rate}


def all_genres(movies: list[dict[str, Any]]) -> set[str]:
    """Функция возвращает множество всех уникальных жанров каталога."""
    result = set()
    for movie in movies:
        result = result | set(movie["genres"])

    return result


def common_actors(movie1: dict, movie2: dict) -> set[str]:
    """Функция возвращает актеров, которые снимались в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    """Функция возвращает жанры, которые есть в `movies_a`, но нет в `movies_b`."""
    genres_a = set()
    for movie in movies_a:
        genres_a = genres_a | set(movie["genres"])

    genres_b = set()
    for movie in movies_b:
        genres_b = genres_b | set(movie["genres"])

    return genres_a - genres_b



print(all_genres(movies))
print(common_actors(movies[0], movies[4]))
print(genres_only_in_one(movies[0:2], movies[2:3]))
