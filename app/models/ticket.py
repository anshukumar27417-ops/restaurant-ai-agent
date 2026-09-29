"""Ticket models placeholder."""
from pydantic import BaseModel


class Ticket(BaseModel):
    id: str | None = None
