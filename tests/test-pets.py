import random

import requests
from faker import Faker

BACKEND_URL: str = "http://127.0.0.1/pets"


class Test:
    def __init__(
            self,
            name: str,
            age: int,
            type: str,
            limit: int,
            ids: list[int],
    ) -> None:
        self.name: str = name
        self.age: int = age
        self.type: str = type
        self.limit: int = limit
        self.ids: list[int] = ids

    def pet_create(self) -> None:
        data: dict = {
            "name": self.name,
            "age": self.age,
            "type": self.type,
        }
        assert requests.post(url=BACKEND_URL, data=data).status_code == 201

    def pet_list(self) -> None:
        data: dict = {
            "limit": self.limit,
        }
        assert requests.get(url=BACKEND_URL, data=data) == 200
    
    def pet_delete(self) -> None:
        data: dict = {
            "ids": self.ids,
        }
        assert requests.delete(url=BACKEND_URL, data=data) == 200


class Randomizer:
    def __init__(self) -> None:
        pass

    def name(self) -> str:
        return Faker.name()

    def age(self) -> int:
        return random.randint(1, 99)

    def type(self) -> str:
        return random.choice(["dog", "cat"])

    def limit(self) -> int:
        return random.randint(1, 1000)

    def ids(self) -> list[int]:
        ...


