from typing import List, Optional
from pydantic import BaseModel


class Method(BaseModel):
    device: str
    method: str
    payload: str
