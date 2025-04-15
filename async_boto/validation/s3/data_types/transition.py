from datetime import datetime
from typing import Literal

from pydantic import BaseModel, root_validator


class Transition(BaseModel):
    """
    Specifies when an object transitions to a specified storage class.

    Attributes
    ----------
    Date : Optional[datetime]
        Indicates when objects are transitioned to the specified storage class.
    Days : Optional[int]
        Indicates the number of days after creation when objects are transitioned to
        the specified storage class.
    StorageClass : Optional[Literal["GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE", "GLACIER_IR"]]
        The storage class to which you want the object to transition.
    """  # noqa: E501

    Date: datetime | None
    Days: int | None
    StorageClass: (
        Literal[
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
            "GLACIER_IR",
        ]
        | None
    )

    @root_validator
    def validate_days(cls, values):
        days = values.get("Days")
        storage_class = values.get("StorageClass")
        if days is not None and storage_class is not None:
            if storage_class in {"STANDARD_IA", "ONEZONE_IA"} and days <= 30:
                raise ValueError(
                    "Days must be greater than 30 for STANDARD_IA or ONEZONE_IA "
                    "storage classes."
                )
            if (
                storage_class
                in {"INTELLIGENT_TIERING", "GLACIER_IR", "GLACIER", "DEEP_ARCHIVE"}
                and days < 0
            ):
                raise ValueError(
                    "Days must be 0 or a positive integer for INTELLIGENT_TIERING, "
                    "GLACIER_IR, GLACIER, or DEEP_ARCHIVE storage classes."
                )
        return values
