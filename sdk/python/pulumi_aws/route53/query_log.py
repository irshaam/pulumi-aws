# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class QueryLog(pulumi.CustomResource):
    cloudwatch_log_group_arn: pulumi.Output[str]
    """
    CloudWatch log group ARN to send query logs.
    """
    zone_id: pulumi.Output[str]
    """
    Route53 hosted zone ID to enable query logs.
    """
    def __init__(__self__, resource_name, opts=None, cloudwatch_log_group_arn=None, zone_id=None, __name__=None, __opts__=None):
        """
        Provides a Route53 query logging configuration resource.
        
        > **NOTE:** There are restrictions on the configuration of query logging. Notably,
        the CloudWatch log group must be in the `us-east-1` region,
        a permissive CloudWatch log resource policy must be in place, and
        the Route53 hosted zone must be public.
        See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: CloudWatch log group ARN to send query logs.
        :param pulumi.Input[str] zone_id: Route53 hosted zone ID to enable query logs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown.
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

        if cloudwatch_log_group_arn is None:
            raise TypeError("Missing required property 'cloudwatch_log_group_arn'")
        __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn

        if zone_id is None:
            raise TypeError("Missing required property 'zone_id'")
        __props__['zone_id'] = zone_id

        super(QueryLog, __self__).__init__(
            'aws:route53/queryLog:QueryLog',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

