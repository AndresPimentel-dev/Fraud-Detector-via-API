from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    hashed_password : str

@dataclass
class Transaccion:
    tsn_description: Optional[dict]

