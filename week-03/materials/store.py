
from typing import Protocol


class MaterialsUnavailable(Exception):
    """The materials storage is temporarily unavailable."""
    pass


class MaterialNotFound(Exception):
    """The requested material does not exist."""
    pass


class MaterialStore(Protocol):
    def list(self, course_id: int) -> list[str]:
        """Return file names. Raises MaterialsUnavailable if unavailable."""
        ...

    def read(self, course_id: int, name: str) -> bytes:
        """Read a file. Raises MaterialNotFound or MaterialsUnavailable."""
        ...

    def write(self, course_id: int, name: str, data: bytes) -> None:
        """Write a file. Raises MaterialsUnavailable if unavailable."""
        ...
