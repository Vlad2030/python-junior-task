from ormar import Integer, Model, String


class Pets(Model):
    id: int = Integer()
    name: str = String(max_length=50, min_length=1)

