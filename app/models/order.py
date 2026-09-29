"""Order models placeholder."""
from pydantic import BaseModel


class Order(BaseModel):
    id: str | None = None
