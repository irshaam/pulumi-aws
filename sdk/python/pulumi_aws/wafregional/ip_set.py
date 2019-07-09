# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class IpSet(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the WAF IPSet.
    """
    ip_set_descriptors: pulumi.Output[list]
    """
    One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.
    """
    name: pulumi.Output[str]
    """
    The name or description of the IPSet.
    """
    def __init__(__self__, resource_name, opts=None, ip_set_descriptors=None, name=None, __name__=None, __opts__=None):
        """
        Provides a WAF Regional IPSet Resource for use with Application Load Balancer.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] ip_set_descriptors: One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR notation) from which web requests originate.
        :param pulumi.Input[str] name: The name or description of the IPSet.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_ipset.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['ip_set_descriptors'] = ip_set_descriptors

        __props__['name'] = name

        __props__['arn'] = None

        super(IpSet, __self__).__init__(
            'aws:wafregional/ipSet:IpSet',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

