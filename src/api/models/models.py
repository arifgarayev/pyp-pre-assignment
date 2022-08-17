from typing import Union
from pydantic import BaseModel

class Upload(BaseModel):
    # fileName: str
    file: bytes
