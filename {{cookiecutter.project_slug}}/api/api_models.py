"""
Declare models for incoming request, these models will evaluate
"""

from fastapi import Form
from pydantic import BaseModel


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            if not hasattr(arg, "default")
            else arg.replace(default=Form(arg.default))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


class JsonRequestModel(BaseModel):
    """
    Declare model for json body (recommended)
    """

    input: str
    another_param: str = "Default value"


@form_body
class FormRequestModel(BaseModel):
    """
    To use pydantic Model for Form body, there must be @form_body decorator
    """

    input: str
    another_param: str = "Default value"
