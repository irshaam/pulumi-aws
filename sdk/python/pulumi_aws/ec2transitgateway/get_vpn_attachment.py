# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetVpnAttachmentResult:
    """
    A collection of values returned by getVpnAttachment.
    """
    def __init__(__self__, tags=None, transit_gateway_id=None, vpn_connection_id=None, id=None):
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Key-value tags for the EC2 Transit Gateway VPN Attachment
        """
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        __self__.transit_gateway_id = transit_gateway_id
        if vpn_connection_id and not isinstance(vpn_connection_id, str):
            raise TypeError("Expected argument 'vpn_connection_id' to be a str")
        __self__.vpn_connection_id = vpn_connection_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_vpn_attachment(tags=None,transit_gateway_id=None,vpn_connection_id=None,opts=None):
    """
    Get information on an EC2 Transit Gateway VPN Attachment.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ec2_transit_gateway_vpn_attachment.html.markdown.
    """
    __args__ = dict()

    __args__['tags'] = tags
    __args__['transitGatewayId'] = transit_gateway_id
    __args__['vpnConnectionId'] = vpn_connection_id
    __ret__ = await pulumi.runtime.invoke('aws:ec2transitgateway/getVpnAttachment:getVpnAttachment', __args__, opts=opts)

    return GetVpnAttachmentResult(
        tags=__ret__.get('tags'),
        transit_gateway_id=__ret__.get('transitGatewayId'),
        vpn_connection_id=__ret__.get('vpnConnectionId'),
        id=__ret__.get('id'))
