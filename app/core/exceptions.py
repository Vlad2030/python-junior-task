PETS_TYPE_DOESNT_EXIST = "Pet type doesn't exists."
PET_ID_DOESNT_EXIST = "Pet ID doesn't exists."
PETS_NO_WERE_DELETED = "No pets were deleted."
PET_ID_NOT_FOUND = "Pet with the matching ID was not found."
LIMIT_LESS_THAN_ZERO = "Limit can't be less than zero"


class PetsException(Exception):
    pass


class PetsTypeException(PetsException):
    pass


class PetsNullDeleteException(PetsException):
    pass
