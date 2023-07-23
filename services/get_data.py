import requests
import json


class GetData:

    """Класс - интерфейс получения данных по API"""

    DATA_URL = 'https://file.notion.so/f/s/0f8850ad-e46f-4f37-99ea-0e4e2a6af5b6/trial_task.json?' \
               'id=2583a04b-4256-4c1f-939e-6eac0f749ceb&table=block&' \
               'spaceId=41165294-a784-489a-a401-1a916d020564&' \
               'expirationTimestamp=1690207200000&' \
               'signature=rdi8YtQNjmpGJQZ5oX2J7Z79BTuEIWmUWNzdlziL4A0&downloadName=trial_task.json'

    @classmethod
    def get_data(cls) -> dict:
        """ Метод получения данных по API"""
        response = requests.get(cls.DATA_URL)
        data = json.loads(response.content)

        return data
