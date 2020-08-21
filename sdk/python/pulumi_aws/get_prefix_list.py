# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetPrefixListResult',
    'AwaitableGetPrefixListResult',
    'get_prefix_list',
]

@pulumi.output_type
class GetPrefixListResult:
    """
    A collection of values returned by getPrefixList.
    """
    def __init__(__self__, cidr_blocks=None, filters=None, id=None, name=None, prefix_list_id=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError("Expected argument 'cidr_blocks' to be a list")
        pulumi.set(__self__, "cidr_blocks", cidr_blocks)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prefix_list_id and not isinstance(prefix_list_id, str):
            raise TypeError("Expected argument 'prefix_list_id' to be a str")
        pulumi.set(__self__, "prefix_list_id", prefix_list_id)

    @property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> List[str]:
        """
        The list of CIDR blocks for the AWS service associated with the prefix list.
        """
        return pulumi.get(self, "cidr_blocks")

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetPrefixListFilterResult']]:
        return pulumi.get(self, "filters")

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
        """
        The name of the selected prefix list.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[str]:
        return pulumi.get(self, "prefix_list_id")


class AwaitableGetPrefixListResult(GetPrefixListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrefixListResult(
            cidr_blocks=self.cidr_blocks,
            filters=self.filters,
            id=self.id,
            name=self.name,
            prefix_list_id=self.prefix_list_id)


def get_prefix_list(filters: Optional[List[pulumi.InputType['GetPrefixListFilterArgs']]] = None,
                    name: Optional[str] = None,
                    prefix_list_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrefixListResult:
    """
    `getPrefixList` provides details about a specific prefix list (PL)
    in the current region.

    This can be used both to validate a prefix list given in a variable
    and to obtain the CIDR blocks (IP address ranges) for the associated
    AWS service. The latter may be useful e.g. for adding network ACL
    rules.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    private_s3_vpc_endpoint = aws.ec2.VpcEndpoint("privateS3VpcEndpoint",
        vpc_id=aws_vpc["foo"]["id"],
        service_name="com.amazonaws.us-west-2.s3")
    private_s3_prefix_list = private_s3_vpc_endpoint.prefix_list_id.apply(lambda prefix_list_id: aws.get_prefix_list(prefix_list_id=prefix_list_id))
    bar = aws.ec2.NetworkAcl("bar", vpc_id=aws_vpc["foo"]["id"])
    private_s3_network_acl_rule = aws.ec2.NetworkAclRule("privateS3NetworkAclRule",
        network_acl_id=bar.id,
        rule_number=200,
        egress=False,
        protocol="tcp",
        rule_action="allow",
        cidr_block=private_s3_prefix_list.cidr_blocks[0],
        from_port=443,
        to_port=443)
    ```
    ### Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.get_prefix_list(filters=[aws.GetPrefixListFilterArgs(
        name="prefix-list-id",
        values=["pl-68a54001"],
    )])
    ```


    :param List[pulumi.InputType['GetPrefixListFilterArgs']] filters: Configuration block(s) for filtering. Detailed below.
    :param str name: The name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
    :param str prefix_list_id: The ID of the prefix list to select.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['prefixListId'] = prefix_list_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getPrefixList:getPrefixList', __args__, opts=opts, typ=GetPrefixListResult).value

    return AwaitableGetPrefixListResult(
        cidr_blocks=__ret__.cidr_blocks,
        filters=__ret__.filters,
        id=__ret__.id,
        name=__ret__.name,
        prefix_list_id=__ret__.prefix_list_id)
