from http import HTTPStatus
from typing import Optional

from starlette.status import (HTTP_200_OK, HTTP_201_CREATED,
                              HTTP_400_BAD_REQUEST)


PETS_TYPE_DOESNT_EXIST="Pet type doesn't exists."
PETS_NO_WERE_DELETED="No pets were deleted."
PETS_ID_NOT_FOUND="Pet with the matching ID was not found."


class PetsException(Exception):
    def __init__(
        self,
        status_code: int,
        detail: Optional[str] = None,
        headers: Optional[dict] = None,
    ) -> None:
        if detail is None:
            detail = HTTPStatus(status_code).phrase
        self.status_code = status_code
        self.detail = detail
        self.headers = headers

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"


class PetsTypeException(
    PetsException(
        status_code=HTTP_400_BAD_REQUEST,
        detail=PETS_TYPE_DOESNT_EXIST,
    )
):
    pass


class PetsNullDeleteException(
    PetsException(
        status_code=HTTP_200_OK,
        detail=PETS_NO_WERE_DELETED,
    )
):
    pass