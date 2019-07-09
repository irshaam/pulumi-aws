# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class TopicSubscription(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the subscription stored as a more user-friendly property
    """
    confirmation_timeout_in_minutes: pulumi.Output[float]
    """
    Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
    """
    delivery_policy: pulumi.Output[str]
    """
    JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
    """
    endpoint: pulumi.Output[str]
    """
    The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
    """
    endpoint_auto_confirms: pulumi.Output[bool]
    """
    Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
    """
    filter_policy: pulumi.Output[str]
    """
    JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
    """
    protocol: pulumi.Output[str]
    """
    The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).
    """
    raw_message_delivery: pulumi.Output[bool]
    """
    Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
    """
    topic: pulumi.Output[str]
    """
    The ARN of the SNS topic to subscribe to
    """
    def __init__(__self__, resource_name, opts=None, confirmation_timeout_in_minutes=None, delivery_policy=None, endpoint=None, endpoint_auto_confirms=None, filter_policy=None, protocol=None, raw_message_delivery=None, topic=None, __name__=None, __opts__=None):
        """
        Create a TopicSubscription resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] confirmation_timeout_in_minutes: Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
        :param pulumi.Input[str] delivery_policy: JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        :param pulumi.Input[str] endpoint: The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
        :param pulumi.Input[bool] endpoint_auto_confirms: Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
        :param pulumi.Input[str] filter_policy: JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        :param pulumi.Input[str] protocol: The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).
        :param pulumi.Input[bool] raw_message_delivery: Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
        :param pulumi.Input[str] topic: The ARN of the SNS topic to subscribe to

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_subscription.html.markdown.
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

        __props__['confirmation_timeout_in_minutes'] = confirmation_timeout_in_minutes

        __props__['delivery_policy'] = delivery_policy

        if endpoint is None:
            raise TypeError("Missing required property 'endpoint'")
        __props__['endpoint'] = endpoint

        __props__['endpoint_auto_confirms'] = endpoint_auto_confirms

        __props__['filter_policy'] = filter_policy

        if protocol is None:
            raise TypeError("Missing required property 'protocol'")
        __props__['protocol'] = protocol

        __props__['raw_message_delivery'] = raw_message_delivery

        if topic is None:
            raise TypeError("Missing required property 'topic'")
        __props__['topic'] = topic

        __props__['arn'] = None

        super(TopicSubscription, __self__).__init__(
            'aws:sns/topicSubscription:TopicSubscription',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

