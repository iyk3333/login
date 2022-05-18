from pydantic import BaseModel


class loginInfoModel(BaseModel):
    kind: str
    loginId: str
    loginPassword: str
