# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetCustomerGatewayResult:
    """
    A collection of values returned by getCustomerGateway.
    """
    def __init__(__self__, bgp_asn=None, filters=None, id=None, ip_address=None, tags=None, type=None):
        if bgp_asn and not isinstance(bgp_asn, float):
            raise TypeError("Expected argument 'bgp_asn' to be a float")
        __self__.bgp_asn = bgp_asn
        """
        (Optional) The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        __self__.ip_address = ip_address
        """
        (Optional) The IP address of the gateway's Internet-routable external interface.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Map of key-value pairs assigned to the gateway.
        """
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        """
        (Optional) The type of customer gateway. The only type AWS supports at this time is "ipsec.1".
        """

async def get_customer_gateway(filters=None,id=None,tags=None,opts=None):
    """
    Get an existing AWS Customer Gateway.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/customer_gateway.html.markdown.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['id'] = id
    __args__['tags'] = tags
    __ret__ = await pulumi.runtime.invoke('aws:ec2/getCustomerGateway:getCustomerGateway', __args__, opts=opts)

    return GetCustomerGatewayResult(
        bgp_asn=__ret__.get('bgpAsn'),
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        ip_address=__ret__.get('ipAddress'),
        tags=__ret__.get('tags'),
        type=__ret__.get('type'))
