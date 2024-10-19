import json
import os.path

from src.basevacancy import BaseVacancy
from src.vacancies import Vacancy


class JSONSaver(BaseVacancy):

    path: str = os.path.abspath("data/vacancies.json")

    @classmethod
    def add_vacancy(cls, vacancy: Vacancy) -> None:
        if issubclass(type(vacancy), Vacancy):
            with open(cls.path, "r") as f:
                result = json.load(f)

            result.append(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": vacancy.salary,
                    "requirement": vacancy.requirement,
                }
            )
            with open(cls.path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

    @classmethod
    def get_vacancy(cls) -> None:
        pass

    @classmethod
    def save_vacancy(cls) -> None:
        pass

    @classmethod
    def delete_vacancy(cls, vacancy: Vacancy) -> None:
        if issubclass(type(vacancy), Vacancy):
            with open(cls.path, "r") as f:
                result = json.load(f)

            result.remove(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": vacancy.salary,
                    "requirement": vacancy.requirement,
                }
            )
            with open(cls.path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
