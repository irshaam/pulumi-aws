# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GroupResourceQueryArgs',
]

@pulumi.input_type
class GroupResourceQueryArgs:
    def __init__(__self__, *,
                 query: pulumi.Input[str],
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] query: The resource query as a JSON string.
        :param pulumi.Input[str] type: The type of the resource query. Defaults to `TAG_FILTERS_1_0`.
        """
        pulumi.set(__self__, "query", query)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def query(self) -> pulumi.Input[str]:
        """
        The resource query as a JSON string.
        """
        ...

    @query.setter
    def query(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the resource query. Defaults to `TAG_FILTERS_1_0`.
        """
        ...

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        ...

