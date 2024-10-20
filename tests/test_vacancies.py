import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancy_one() -> Vacancy:
    vacancy1 = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )
    return vacancy1


@pytest.fixture
def vacancy_two() -> Vacancy:
    vacancy2 = Vacancy(
        "Java Developer",
        "<https://hh.ru/vacancy/123456>",
        "70 000-80 000 руб.",
        "Требования: БЕЗ ОПЫТА",
    )
    return vacancy2


def test_vacancy_one(vacancy_one: Vacancy) -> None:
    assert vacancy_one.name == "Python Developer"
    assert vacancy_one.alternate_url == "<https://hh.ru/vacancy/123456>"
    assert vacancy_one.salary == 100_000
    assert vacancy_one.requirement == "Требования: опыт работы от 3 лет..."


def test_compare_salary(vacancy_one: Vacancy, vacancy_two: Vacancy) -> None:
    result = vacancy_one > vacancy_two
    assert result


def test_cast_to_object_list(vacancy_one: Vacancy) -> None:
    hh_vacancies = [
        {
            "name": "Python Developer",
            "alternate_url": "https://example.com/vacancy/1",
            "salary": {"from": 1000, "to": 2000},
            "snippet": {"requirement": "Знание Python"},
        },
        {
            "name": "Java Developer",
            "alternate_url": "https://example.com/vacancy/2",
            "salary": {"from": 1500, "to": 2500},
            "snippet": {"requirement": "Знание Java"},
        },
    ]
    expected_vacancies = [
        Vacancy("Python Developer", "https://example.com/vacancy/1", {"from": 1000, "to": 2000}, "Знание Python"),
        Vacancy("Java Developer", "https://example.com/vacancy/2", {"from": 1500, "to": 2500}, "Знание Java"),
    ]

    result = Vacancy.cast_to_object_list(hh_vacancies)  # type: ignore
    for r, e in zip(result, expected_vacancies):
        assert r.name == e.name
        assert r.alternate_url == e.alternate_url
        assert r.salary == e.salary
        assert r.requirement == e.requirement
