from typing import Literal

from pydantic import BaseModel, root_validator


class DefaultRetention(BaseModel):
    """
    The container element for optionally specifying the default Object Lock retention
    settings
    for new objects placed in the specified bucket.

    Attributes
    ----------
    Days : Optional[int]
        The number of days for the default retention period. Must be used with Mode.
    Mode : Optional[Literal["GOVERNANCE", "COMPLIANCE"]]
        The default Object Lock retention mode. Must be used with either Days or Years.
    Years : Optional[int]
        The number of years for the default retention period. Must be used with Mode.
    """

    Days: int | None = None
    Mode: Literal["GOVERNANCE", "COMPLIANCE"] | None = None
    Years: int | None = None

    @root_validator
    def validate_retention(cls, values):
        days = values.get("Days")
        years = values.get("Years")
        mode = values.get("Mode")

        if not mode and (days or years):
            raise ValueError("Mode must be specified when Days or Years is provided.")
        if mode and not (days or years):
            raise ValueError(
                "Either Days or Years must be specified when Mode is provided."
            )
        if days and years:
            raise ValueError("You cannot specify both Days and Years at the same time.")

        return values
