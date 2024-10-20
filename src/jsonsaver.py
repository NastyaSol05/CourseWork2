import json
import os.path

from dulwich.porcelain import path_to_tree_path

from src.basevacancy import BaseVacancy
from src.vacancies import Vacancy


class JSONSaver(BaseVacancy):

    __path: str = os.path.abspath("data/vacancies.json")

    @classmethod
    def add_vacancy(cls, vacancy: Vacancy) -> None:
        if issubclass(type(vacancy), Vacancy):
            with open(cls.__path, "r") as f:
                result = json.load(f)

            obj = {
                    "name": vacancy.name,
                    "alternate_url": vacancy.alternate_url,
                    "salary": vacancy.salary,
                    "requirement": vacancy.requirement,
                }

            if obj not in result:
                result.append(obj)
                with open(cls.__path, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)

    @classmethod
    def get_vacancy(cls) -> None:
        with open(cls.__path, "r") as f:
            return json.load(f)

    @classmethod
    def save_vacancy(cls) -> None:
        pass

    @classmethod
    def delete_vacancy(cls, vacancy: Vacancy) -> None:
        if issubclass(type(vacancy), Vacancy):
            with open(cls.__path, "r") as f:
                result = json.load(f)

            result.remove(
                {
                    "name": vacancy.name,
                    "alternate_url": vacancy.alternate_url,
                    "salary": vacancy.salary,
                    "requirement": vacancy.requirement,
                }
            )
            with open(cls.__path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

    @property
    def path(self):
        return self.__path
