# mypy: disable-error-code="arg-type,return-value"

from core.depends import auth_required
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.responses import JSONResponse, Response
from fastapi_jwt_auth import AuthJWT
from schemas import ApplicationResponse
from starlette import status

router = APIRouter()


def unset_jwt_cookies(response: Response, authorize: AuthJWT) -> None:
    authorize.unset_jwt_cookies(response=response)


@router.delete(
    path="/",
    dependencies=[Depends(auth_required)],
    summary="WORKS (need X-CSRF-TOKEN in headers): " "User logout (token removal).",
    response_model=ApplicationResponse[bool],
    status_code=status.HTTP_200_OK,
)
async def logout_user(
    response: JSONResponse, authorize: AuthJWT = Depends()
) -> ApplicationResponse[bool]:
    unset_jwt_cookies(response=response, authorize=authorize)

    return {
        "ok": True,
        "result": True,
    }
