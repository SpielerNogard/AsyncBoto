from pydantic import BaseModel, constr

from .data_types.allowed_publishers import AllowedPublishers
from .data_types.code_signing_config import CodeSigningConfig
from .data_types.code_signing_policies import CodeSigningPolicies


class CreateCodeSigningConfigRequest(BaseModel):
    """
    Request model for the CreateCodeSigningConfig operation.

    Creates a code signing configuration.

    Attributes
    ----------
    AllowedPublishers : AllowedPublishers
        Signing profiles for this code signing configuration.
    CodeSigningPolicies : Optional[CodeSigningPolicies]
        The code signing policies define the actions to take if the validation
        checks fail.
    Description : Optional[str]
        Descriptive name for this code signing configuration.
    Tags : Optional[Dict[str, str]]
        A list of tags to add to the code signing configuration.
    """

    AllowedPublishers: AllowedPublishers
    CodeSigningPolicies: CodeSigningPolicies | None = None
    Description: constr(min_length=0, max_length=256) | None = None
    Tags: dict[str, str] | None = None


class CreateCodeSigningConfigResponse(BaseModel):
    """
    Response model for the CreateCodeSigningConfig operation.

    Attributes
    ----------
    CodeSigningConfig : CodeSigningConfig
        The code signing configuration.
    """

    CodeSigningConfig: CodeSigningConfig
