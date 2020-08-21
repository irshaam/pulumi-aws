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

__all__ = ['NotificationRule']


class NotificationRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detail_type: Optional[pulumi.Input[str]] = None,
                 event_type_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 targets: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NotificationRuleTargetArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CodeStar Notifications Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        code = aws.codecommit.Repository("code", repository_name="example-code-repo")
        notif = aws.sns.Topic("notif")
        notif_access = notif.arn.apply(lambda arn: aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sns:Publish"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="Service",
                identifiers=["codestar-notifications.amazonaws.com"],
            )],
            resources=[arn],
        )]))
        default = aws.sns.TopicPolicy("default",
            arn=notif.arn,
            policy=notif_access.json)
        commits = aws.codestarnotifications.NotificationRule("commits",
            detail_type="BASIC",
            event_type_ids=["codecommit-repository-comments-on-commits"],
            resource=code.arn,
            targets=[aws.codestarnotifications.NotificationRuleTargetArgs(
                address=notif.arn,
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detail_type: The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
        :param pulumi.Input[List[pulumi.Input[str]]] event_type_ids: A list of event types associated with this notification rule.
               For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
        :param pulumi.Input[str] name: The name of notification rule.
        :param pulumi.Input[str] resource: The ARN of the resource to associate with the notification rule.
        :param pulumi.Input[str] status: The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NotificationRuleTargetArgs']]]] targets: Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.
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

            if detail_type is None:
                raise TypeError("Missing required property 'detail_type'")
            __props__['detail_type'] = detail_type
            if event_type_ids is None:
                raise TypeError("Missing required property 'event_type_ids'")
            __props__['event_type_ids'] = event_type_ids
            __props__['name'] = name
            if resource is None:
                raise TypeError("Missing required property 'resource'")
            __props__['resource'] = resource
            __props__['status'] = status
            __props__['tags'] = tags
            __props__['targets'] = targets
            __props__['arn'] = None
        super(NotificationRule, __self__).__init__(
            'aws:codestarnotifications/notificationRule:NotificationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            detail_type: Optional[pulumi.Input[str]] = None,
            event_type_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            targets: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['NotificationRuleTargetArgs']]]]] = None) -> 'NotificationRule':
        """
        Get an existing NotificationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The codestar notification rule ARN.
        :param pulumi.Input[str] detail_type: The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
        :param pulumi.Input[List[pulumi.Input[str]]] event_type_ids: A list of event types associated with this notification rule.
               For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
        :param pulumi.Input[str] name: The name of notification rule.
        :param pulumi.Input[str] resource: The ARN of the resource to associate with the notification rule.
        :param pulumi.Input[str] status: The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['NotificationRuleTargetArgs']]]] targets: Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["detail_type"] = detail_type
        __props__["event_type_ids"] = event_type_ids
        __props__["name"] = name
        __props__["resource"] = resource
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["targets"] = targets
        return NotificationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The codestar notification rule ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> str:
        """
        The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
        """
        return pulumi.get(self, "detail_type")

    @property
    @pulumi.getter(name="eventTypeIds")
    def event_type_ids(self) -> List[str]:
        """
        A list of event types associated with this notification rule.
        For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
        """
        return pulumi.get(self, "event_type_ids")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of notification rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        The ARN of the resource to associate with the notification rule.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def targets(self) -> Optional[List['outputs.NotificationRuleTarget']]:
        """
        Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.
        """
        return pulumi.get(self, "targets")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

