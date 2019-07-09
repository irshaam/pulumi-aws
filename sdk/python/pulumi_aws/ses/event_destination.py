# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventDestination(pulumi.CustomResource):
    cloudwatch_destinations: pulumi.Output[list]
    """
    CloudWatch destination for the events
    """
    configuration_set_name: pulumi.Output[str]
    """
    The name of the configuration set
    """
    enabled: pulumi.Output[bool]
    """
    If true, the event destination will be enabled
    """
    kinesis_destination: pulumi.Output[dict]
    """
    Send the events to a kinesis firehose destination
    """
    matching_types: pulumi.Output[list]
    """
    A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
    """
    name: pulumi.Output[str]
    """
    The name of the event destination
    """
    sns_destination: pulumi.Output[dict]
    """
    Send the events to an SNS Topic destination
    """
    def __init__(__self__, resource_name, opts=None, cloudwatch_destinations=None, configuration_set_name=None, enabled=None, kinesis_destination=None, matching_types=None, name=None, sns_destination=None, __name__=None, __opts__=None):
        """
        Provides an SES event destination
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] cloudwatch_destinations: CloudWatch destination for the events
        :param pulumi.Input[str] configuration_set_name: The name of the configuration set
        :param pulumi.Input[bool] enabled: If true, the event destination will be enabled
        :param pulumi.Input[dict] kinesis_destination: Send the events to a kinesis firehose destination
        :param pulumi.Input[list] matching_types: A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        :param pulumi.Input[str] name: The name of the event destination
        :param pulumi.Input[dict] sns_destination: Send the events to an SNS Topic destination

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_event_destination.html.markdown.
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

        __props__['cloudwatch_destinations'] = cloudwatch_destinations

        if configuration_set_name is None:
            raise TypeError("Missing required property 'configuration_set_name'")
        __props__['configuration_set_name'] = configuration_set_name

        __props__['enabled'] = enabled

        __props__['kinesis_destination'] = kinesis_destination

        if matching_types is None:
            raise TypeError("Missing required property 'matching_types'")
        __props__['matching_types'] = matching_types

        __props__['name'] = name

        __props__['sns_destination'] = sns_destination

        super(EventDestination, __self__).__init__(
            'aws:ses/eventDestination:EventDestination',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

