"""
ORM
"""

from typing import Optional
from pydantic import BaseModel


class loginInfoModel(BaseModel):
    loginId: str
    loginPassword: str
