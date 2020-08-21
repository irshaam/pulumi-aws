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
    'GetTransitGatewayResult',
    'AwaitableGetTransitGatewayResult',
    'get_transit_gateway',
]

@pulumi.output_type
class GetTransitGatewayResult:
    """
    A collection of values returned by getTransitGateway.
    """
    def __init__(__self__, amazon_side_asn=None, arn=None, association_default_route_table_id=None, auto_accept_shared_attachments=None, default_route_table_association=None, default_route_table_propagation=None, description=None, dns_support=None, filters=None, id=None, owner_id=None, propagation_default_route_table_id=None, tags=None, vpn_ecmp_support=None):
        if amazon_side_asn and not isinstance(amazon_side_asn, float):
            raise TypeError("Expected argument 'amazon_side_asn' to be a float")
        pulumi.set(__self__, "amazon_side_asn", amazon_side_asn)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if association_default_route_table_id and not isinstance(association_default_route_table_id, str):
            raise TypeError("Expected argument 'association_default_route_table_id' to be a str")
        pulumi.set(__self__, "association_default_route_table_id", association_default_route_table_id)
        if auto_accept_shared_attachments and not isinstance(auto_accept_shared_attachments, str):
            raise TypeError("Expected argument 'auto_accept_shared_attachments' to be a str")
        pulumi.set(__self__, "auto_accept_shared_attachments", auto_accept_shared_attachments)
        if default_route_table_association and not isinstance(default_route_table_association, str):
            raise TypeError("Expected argument 'default_route_table_association' to be a str")
        pulumi.set(__self__, "default_route_table_association", default_route_table_association)
        if default_route_table_propagation and not isinstance(default_route_table_propagation, str):
            raise TypeError("Expected argument 'default_route_table_propagation' to be a str")
        pulumi.set(__self__, "default_route_table_propagation", default_route_table_propagation)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_support and not isinstance(dns_support, str):
            raise TypeError("Expected argument 'dns_support' to be a str")
        pulumi.set(__self__, "dns_support", dns_support)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        pulumi.set(__self__, "owner_id", owner_id)
        if propagation_default_route_table_id and not isinstance(propagation_default_route_table_id, str):
            raise TypeError("Expected argument 'propagation_default_route_table_id' to be a str")
        pulumi.set(__self__, "propagation_default_route_table_id", propagation_default_route_table_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpn_ecmp_support and not isinstance(vpn_ecmp_support, str):
            raise TypeError("Expected argument 'vpn_ecmp_support' to be a str")
        pulumi.set(__self__, "vpn_ecmp_support", vpn_ecmp_support)

    @property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> float:
        """
        Private Autonomous System Number (ASN) for the Amazon side of a BGP session
        """
        return pulumi.get(self, "amazon_side_asn")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        EC2 Transit Gateway Amazon Resource Name (ARN)
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associationDefaultRouteTableId")
    def association_default_route_table_id(self) -> str:
        """
        Identifier of the default association route table
        """
        return pulumi.get(self, "association_default_route_table_id")

    @property
    @pulumi.getter(name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(self) -> str:
        """
        Whether resource attachment requests are automatically accepted.
        """
        return pulumi.get(self, "auto_accept_shared_attachments")

    @property
    @pulumi.getter(name="defaultRouteTableAssociation")
    def default_route_table_association(self) -> str:
        """
        Whether resource attachments are automatically associated with the default association route table.
        """
        return pulumi.get(self, "default_route_table_association")

    @property
    @pulumi.getter(name="defaultRouteTablePropagation")
    def default_route_table_propagation(self) -> str:
        """
        Whether resource attachments automatically propagate routes to the default propagation route table.
        """
        return pulumi.get(self, "default_route_table_propagation")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the EC2 Transit Gateway
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> str:
        """
        Whether DNS support is enabled.
        """
        return pulumi.get(self, "dns_support")

    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.GetTransitGatewayFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        EC2 Transit Gateway identifier
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> str:
        """
        Identifier of the AWS account that owns the EC2 Transit Gateway
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="propagationDefaultRouteTableId")
    def propagation_default_route_table_id(self) -> str:
        """
        Identifier of the default propagation route table.
        """
        return pulumi.get(self, "propagation_default_route_table_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value tags for the EC2 Transit Gateway
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> str:
        """
        Whether VPN Equal Cost Multipath Protocol support is enabled.
        """
        return pulumi.get(self, "vpn_ecmp_support")


class AwaitableGetTransitGatewayResult(GetTransitGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitGatewayResult(
            amazon_side_asn=self.amazon_side_asn,
            arn=self.arn,
            association_default_route_table_id=self.association_default_route_table_id,
            auto_accept_shared_attachments=self.auto_accept_shared_attachments,
            default_route_table_association=self.default_route_table_association,
            default_route_table_propagation=self.default_route_table_propagation,
            description=self.description,
            dns_support=self.dns_support,
            filters=self.filters,
            id=self.id,
            owner_id=self.owner_id,
            propagation_default_route_table_id=self.propagation_default_route_table_id,
            tags=self.tags,
            vpn_ecmp_support=self.vpn_ecmp_support)


def get_transit_gateway(filters: Optional[List[pulumi.InputType['GetTransitGatewayFilterArgs']]] = None,
                        id: Optional[str] = None,
                        tags: Optional[Mapping[str, str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitGatewayResult:
    """
    Get information on an EC2 Transit Gateway.

    ## Example Usage
    ### By Filter

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_transit_gateway(filters=[aws.ec2transitgateway.GetTransitGatewayFilterArgs(
        name="options.amazon-side-asn",
        values=["64512"],
    )])
    ```
    ### By Identifier

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ec2transitgateway.get_transit_gateway(id="tgw-12345678")
    ```


    :param List[pulumi.InputType['GetTransitGatewayFilterArgs']] filters: One or more configuration blocks containing name-values filters. Detailed below.
    :param str id: Identifier of the EC2 Transit Gateway.
    :param Mapping[str, str] tags: Key-value tags for the EC2 Transit Gateway
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2transitgateway/getTransitGateway:getTransitGateway', __args__, opts=opts, typ=GetTransitGatewayResult).value

    return AwaitableGetTransitGatewayResult(
        amazon_side_asn=__ret__.amazon_side_asn,
        arn=__ret__.arn,
        association_default_route_table_id=__ret__.association_default_route_table_id,
        auto_accept_shared_attachments=__ret__.auto_accept_shared_attachments,
        default_route_table_association=__ret__.default_route_table_association,
        default_route_table_propagation=__ret__.default_route_table_propagation,
        description=__ret__.description,
        dns_support=__ret__.dns_support,
        filters=__ret__.filters,
        id=__ret__.id,
        owner_id=__ret__.owner_id,
        propagation_default_route_table_id=__ret__.propagation_default_route_table_id,
        tags=__ret__.tags,
        vpn_ecmp_support=__ret__.vpn_ecmp_support)
