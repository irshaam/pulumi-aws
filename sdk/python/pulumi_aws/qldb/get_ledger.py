# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetLedgerResult',
    'AwaitableGetLedgerResult',
    'get_ledger',
]

@pulumi.output_type
class GetLedgerResult:
    """
    A collection of values returned by getLedger.
    """
    def __init__(__self__, arn=None, deletion_protection=None, id=None, name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the ledger.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> bool:
        """
        Deletion protection on the QLDB Ledger instance. Set to `true` by default.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetLedgerResult(GetLedgerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLedgerResult(
            arn=self.arn,
            deletion_protection=self.deletion_protection,
            id=self.id,
            name=self.name)


def get_ledger(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLedgerResult:
    """
    Use this data source to fetch information about a Quantum Ledger Database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.qldb.get_ledger(name="an_example_ledger")
    ```


    :param str name: The friendly name of the ledger to match.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:qldb/getLedger:getLedger', __args__, opts=opts, typ=GetLedgerResult).value

    return AwaitableGetLedgerResult(
        arn=__ret__.arn,
        deletion_protection=__ret__.deletion_protection,
        id=__ret__.id,
        name=__ret__.name)
