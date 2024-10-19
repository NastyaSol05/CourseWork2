from typing import Any

from src.hh_api import HhAPI
from src.jsonsaver import JSONSaver
from src.vacancies import Vacancy


def user_interaction() -> Any:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    json_saver = JSONSaver()
    hh_api = HhAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancy_list = Vacancy.cast_to_object_list(hh_vacancies)
    sorted_vacancies = sorted(vacancy_list, key=lambda vacancy_: vacancy_.salary, reverse=True)
    print("Топ n")
    for i in range(0, top_n):
        print(sorted_vacancies[i])
        json_saver.add_vacancy(sorted_vacancies[i])

    print("\nФильтр по ключевому слову:")
    for vacancy in vacancy_list:
        for word in filter_words:
            if word in vacancy.requirement:
                print(vacancy)
                continue


if __name__ == "__main__":
    user_interaction()
