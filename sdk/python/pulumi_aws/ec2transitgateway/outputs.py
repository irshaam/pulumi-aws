# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetDirectConnectGatewayAttachmentFilterResult',
    'GetPeeringAttachmentFilterResult',
    'GetRouteTableFilterResult',
    'GetTransitGatewayFilterResult',
    'GetVpcAttachmentFilterResult',
    'GetVpnAttachmentFilterResult',
]

@pulumi.output_type
class GetDirectConnectGatewayAttachmentFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the filter field. Valid values can be found in the [EC2 DescribeTransitGatewayAttachments API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html).
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        ...


@pulumi.output_type
class GetPeeringAttachmentFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the field to filter by, as defined by
        [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayPeeringAttachments.html).
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        Set of values that are accepted for the given field.
        An EC2 Transit Gateway Peering Attachment be selected if any one of the given values matches.
        """
        ...


@pulumi.output_type
class GetRouteTableFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter.
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        List of one or more values for the filter.
        """
        ...


@pulumi.output_type
class GetTransitGatewayFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter.
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        List of one or more values for the filter.
        """
        ...


@pulumi.output_type
class GetVpcAttachmentFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the filter.
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        List of one or more values for the filter.
        """
        ...


@pulumi.output_type
class GetVpnAttachmentFilterResult(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the filter field. Valid values can be found in the [EC2 DescribeTransitGatewayAttachments API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html).
        """
        ...

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        ...

