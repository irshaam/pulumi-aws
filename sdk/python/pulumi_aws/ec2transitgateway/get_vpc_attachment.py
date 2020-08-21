# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetVpcAttachmentResult',
    'AwaitableGetVpcAttachmentResult',
    'get_vpc_attachment',
]

@pulumi.output_type
class GetVpcAttachmentResult:
    """
    A collection of values returned by getVpcAttachment.
    """
    def __init__(__self__, dns_support=None, filters=None, id=None, ipv6_support=None, subnet_ids=None, tags=None, transit_gateway_id=None, vpc_id=None, vpc_owner_id=None):
        if dns_support and not isinstance(dns_support, str):
            raise TypeError("Expected argument 'dns_support' to be a str")
        pulumi.set(__self__, "dns_support", dns_support)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_support and not isinstance(ipv6_support, str):
            raise TypeError("Expected argument 'ipv6_support' to be a str")
        pulumi.set(__self__, "ipv6_support", ipv6_support)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_owner_id and not isinstance(vpc_owner_id, str):
            raise TypeError("Expected argument 'vpc_owner_id' to be a str")
        pulumi.set(__self__, "vpc_owner_id", vpc_owner_id)

    @property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> str:
        """
        Whether DNS support is enabled.
        """
        return pulumi.get(self, "dns_support")

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetVpcAttachmentFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        EC2 Transit Gateway VPC Attachment identifier
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> str:
        """
        Whether IPv6 support is enabled.
        """
        return pulumi.get(self, "ipv6_support")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        """
        Identifiers of EC2 Subnets.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value tags for the EC2 Transit Gateway VPC Attachment
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """
        EC2 Transit Gateway identifier
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Identifier of EC2 VPC.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcOwnerId")
    def vpc_owner_id(self) -> str:
        """
        Identifier of the AWS account that owns the EC2 VPC.
        """
        return pulumi.get(self, "vpc_owner_id")


class AwaitableGetVpcAttachmentResult(GetVpcAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcAttachmentResult(
            dns_support=self.dns_support,
            filters=self.filters,
            id=self.id,
            ipv6_support=self.ipv6_support,
            subnet_ids=self.subnet_ids,
            tags=self.tags,
            transit_gateway_id=self.transit_gateway_id,
            vpc_id=self.vpc_id,
            vpc_owner_id=self.vpc_owner_id)


def get_vpc_attachment(filters: Optional[List[pulumi.InputType['GetVpcAttachmentFilterArgs']]] = None,
                       id: Optional[str] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcAttachmentResult:
    """
    Get information on an EC2 Transit Gateway VPC Attachment.

    ## Example Usage
    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(filters=[aws.ec2transitgateway.GetVpcAttachmentFilterArgs(
        name="vpc-id",
        values=["vpc-12345678"],
    )])
    ```
    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_vpc_attachment(id="tgw-attach-12345678")
    ```


    :param List[pulumi.InputType['GetVpcAttachmentFilterArgs']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway VPC Attachment.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway VPC Attachment
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2transitgateway/getVpcAttachment:getVpcAttachment', __args__, opts=opts, typ=GetVpcAttachmentResult).value

    return AwaitableGetVpcAttachmentResult(
        dns_support=__ret__.dns_support,
        filters=__ret__.filters,
        id=__ret__.id,
        ipv6_support=__ret__.ipv6_support,
        subnet_ids=__ret__.subnet_ids,
        tags=__ret__.tags,
        transit_gateway_id=__ret__.transit_gateway_id,
        vpc_id=__ret__.vpc_id,
        vpc_owner_id=__ret__.vpc_owner_id)
