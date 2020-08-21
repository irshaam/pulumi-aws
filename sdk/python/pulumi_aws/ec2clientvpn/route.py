# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Route']


class Route(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides additional routes for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_endpoint = aws.ec2clientvpn.Endpoint("exampleEndpoint",
            description="Example Client VPN endpoint",
            server_certificate_arn=aws_acm_certificate["example"]["arn"],
            client_cidr_block="10.0.0.0/16",
            authentication_options=[aws.ec2clientvpn.EndpointAuthenticationOptionArgs(
                type="certificate-authentication",
                root_certificate_chain_arn=aws_acm_certificate["example"]["arn"],
            )],
            connection_log_options=aws.ec2clientvpn.EndpointConnectionLogOptionsArgs(
                enabled=False,
            ))
        example_network_association = aws.ec2clientvpn.NetworkAssociation("exampleNetworkAssociation",
            client_vpn_endpoint_id=example_endpoint.id,
            subnet_id=aws_subnet["example"]["id"])
        example_route = aws.ec2clientvpn.Route("exampleRoute",
            client_vpn_endpoint_id=example_endpoint.id,
            destination_cidr_block="0.0.0.0/0",
            target_vpc_subnet_id=example_network_association.subnet_id)
        ```
        ## Attribute Reference

        In addition to all arguments above, the following attributes are exported:

        * `id` - The ID of the Client VPN endpoint.
        * `origin` - Indicates how the Client VPN route was added. Will be `add-route` for routes created by this resource.
        * `type` - The type of the route.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] description: A brief description of the authorization rule.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if client_vpn_endpoint_id is None:
                raise TypeError("Missing required property 'client_vpn_endpoint_id'")
            __props__['client_vpn_endpoint_id'] = client_vpn_endpoint_id
            __props__['description'] = description
            if destination_cidr_block is None:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__['destination_cidr_block'] = destination_cidr_block
            if target_vpc_subnet_id is None:
                raise TypeError("Missing required property 'target_vpc_subnet_id'")
            __props__['target_vpc_subnet_id'] = target_vpc_subnet_id
            __props__['origin'] = None
            __props__['type'] = None
        super(Route, __self__).__init__(
            'aws:ec2clientvpn/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            origin: Optional[pulumi.Input[str]] = None,
            target_vpc_subnet_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[str] description: A brief description of the authorization rule.
        :param pulumi.Input[str] destination_cidr_block: The IPv4 address range, in CIDR notation, of the route destination.
        :param pulumi.Input[str] target_vpc_subnet_id: The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        __props__["description"] = description
        __props__["destination_cidr_block"] = destination_cidr_block
        __props__["origin"] = origin
        __props__["target_vpc_subnet_id"] = target_vpc_subnet_id
        __props__["type"] = type
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> str:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A brief description of the authorization rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> str:
        """
        The IPv4 address range, in CIDR notation, of the route destination.
        """
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter
    def origin(self) -> str:
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="targetVpcSubnetId")
    def target_vpc_subnet_id(self) -> str:
        """
        The ID of the Subnet to route the traffic through. It must already be attached to the Client VPN.
        """
        return pulumi.get(self, "target_vpc_subnet_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

