# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetCoipPoolResult',
    'AwaitableGetCoipPoolResult',
    'get_coip_pool',
]

@pulumi.output_type
class GetCoipPoolResult:
    """
    A collection of values returned by getCoipPool.
    """
    def __init__(__self__, filters=None, id=None, local_gateway_route_table_id=None, pool_cidrs=None, pool_id=None, tags=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if local_gateway_route_table_id and not isinstance(local_gateway_route_table_id, str):
            raise TypeError("Expected argument 'local_gateway_route_table_id' to be a str")
        pulumi.set(__self__, "local_gateway_route_table_id", local_gateway_route_table_id)
        if pool_cidrs and not isinstance(pool_cidrs, list):
            raise TypeError("Expected argument 'pool_cidrs' to be a list")
        pulumi.set(__self__, "pool_cidrs", pool_cidrs)
        if pool_id and not isinstance(pool_id, str):
            raise TypeError("Expected argument 'pool_id' to be a str")
        pulumi.set(__self__, "pool_id", pool_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetCoipPoolFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> str:
        return pulumi.get(self, "local_gateway_route_table_id")

    @property
    @pulumi.getter(name="poolCidrs")
    def pool_cidrs(self) -> Sequence[str]:
        """
        Set of CIDR blocks in pool
        """
        return pulumi.get(self, "pool_cidrs")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> str:
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")


class AwaitableGetCoipPoolResult(GetCoipPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCoipPoolResult(
            filters=self.filters,
            id=self.id,
            local_gateway_route_table_id=self.local_gateway_route_table_id,
            pool_cidrs=self.pool_cidrs,
            pool_id=self.pool_id,
            tags=self.tags)


def get_coip_pool(filters: Optional[Sequence[pulumi.InputType['GetCoipPoolFilterArgs']]] = None,
                  local_gateway_route_table_id: Optional[str] = None,
                  pool_id: Optional[str] = None,
                  tags: Optional[Mapping[str, str]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCoipPoolResult:
    """
    Provides details about a specific EC2 Customer-Owned IP Pool.

    This data source can prove useful when a module accepts a coip pool id as
    an input variable and needs to, for example, determine the CIDR block of that
    COIP Pool.

    ## Example Usage

    The following example returns a specific coip pool ID

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    coip_pool_id = config.require_object("coipPoolId")
    selected = aws.ec2.get_coip_pool(id=coip_pool_id)
    ```


    :param str local_gateway_route_table_id: Local Gateway Route Table Id assigned to desired COIP Pool
    :param str pool_id: The id of the specific COIP Pool to retrieve.
    :param Mapping[str, str] tags: A mapping of tags, each pair of which must exactly match
           a pair on the desired COIP Pool.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['localGatewayRouteTableId'] = local_gateway_route_table_id
    __args__['poolId'] = pool_id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getCoipPool:getCoipPool', __args__, opts=opts, typ=GetCoipPoolResult).value

    return AwaitableGetCoipPoolResult(
        filters=__ret__.filters,
        id=__ret__.id,
        local_gateway_route_table_id=__ret__.local_gateway_route_table_id,
        pool_cidrs=__ret__.pool_cidrs,
        pool_id=__ret__.pool_id,
        tags=__ret__.tags)
