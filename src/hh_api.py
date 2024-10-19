from typing import Any

import requests

from src.baseapi import BaseAPI


class HhAPI(BaseAPI):

    url = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text": "", "page": 0, "per_page": 100}

    def get_vacancies(self, query: Any = None) -> Any:
        if query:
            self.params["text"] = query
            response = requests.get(url=self.url, params=self.params)  # type: ignore
        else:
            response = requests.get(self.url)

        response.raise_for_status()
        vacancies = response.json()["items"]
        return vacancies
