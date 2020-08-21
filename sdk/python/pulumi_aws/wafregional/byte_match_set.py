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

__all__ = ['ByteMatchSet']


class ByteMatchSet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 byte_match_tuples: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['ByteMatchSetByteMatchTupleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a WAF Regional Byte Match Set Resource for use with Application Load Balancer.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        byte_set = aws.wafregional.ByteMatchSet("byteSet", byte_match_tuples=[aws.wafregional.ByteMatchSetByteMatchTupleArgs(
            field_to_match=aws.wafregional.ByteMatchSetByteMatchTupleFieldToMatchArgs(
                data="referer",
                type="HEADER",
            ),
            positional_constraint="CONTAINS",
            target_string="badrefer1",
            text_transformation="NONE",
        )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['ByteMatchSetByteMatchTupleArgs']]]] byte_match_tuples: Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        :param pulumi.Input[str] name: The name or description of the ByteMatchSet.
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

            __props__['byte_match_tuples'] = byte_match_tuples
            __props__['name'] = name
        super(ByteMatchSet, __self__).__init__(
            'aws:wafregional/byteMatchSet:ByteMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            byte_match_tuples: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['ByteMatchSetByteMatchTupleArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ByteMatchSet':
        """
        Get an existing ByteMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['ByteMatchSetByteMatchTupleArgs']]]] byte_match_tuples: Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        :param pulumi.Input[str] name: The name or description of the ByteMatchSet.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["byte_match_tuples"] = byte_match_tuples
        __props__["name"] = name
        return ByteMatchSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="byteMatchTuples")
    def byte_match_tuples(self) -> Optional[List['outputs.ByteMatchSetByteMatchTuple']]:
        """
        Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        """
        return pulumi.get(self, "byte_match_tuples")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name or description of the ByteMatchSet.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

