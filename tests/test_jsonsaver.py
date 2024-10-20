import json
from typing import Any
from unittest.mock import mock_open, patch, call

from src.jsonsaver import JSONSaver
from src.vacancies import Vacancy

@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
def test_add_vacancy(mock_file: Any) -> None:
    vacancy = Vacancy("Software Engineer", "http://example.com", 100000, "Python, Django")

    JSONSaver.add_vacancy(vacancy)

    handle = mock_file()

    write_calls = handle.write.call_args_list
    written_data = "".join(call[0][0] for call in write_calls)

    expected_data = [
        {"name": "Software Engineer", "alternate_url": "http://example.com", "salary": 100000, "requirement": "Python, Django"}
    ]
    expected_json = json.dumps(expected_data, ensure_ascii=False, indent=2)

    assert written_data.strip() == expected_json, f"Expected {expected_json}, but got {written_data.strip()}"
