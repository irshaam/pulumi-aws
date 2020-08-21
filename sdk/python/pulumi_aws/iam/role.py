# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Role']


class Role(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assume_role_policy: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_detach_policies: Optional[pulumi.Input[bool]] = None,
                 max_session_duration: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions_boundary: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an IAM role.

        > *NOTE:* If policies are attached to the role via the `iam.PolicyAttachment` resource and you are modifying the role `name` or `path`, the `force_detach_policies` argument must be set to `true` and applied before attempting the operation otherwise you will encounter a `DeleteConflict` error. The `iam.RolePolicyAttachment` resource (recommended) does not have this requirement.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_role = aws.iam.Role("testRole",
            assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "ec2.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\",
            tags={
                "tag-key": "tag-value",
            })
        ```
        ## Example of Using Data Source for Assume Role Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        instance_assume_role_policy = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="Service",
                identifiers=["ec2.amazonaws.com"],
            )],
        )])
        instance = aws.iam.Role("instance",
            path="/system/",
            assume_role_policy=instance_assume_role_policy.json)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assume_role_policy: The policy that grants an entity permission to assume the role.
        :param pulumi.Input[str] description: The description of the role.
        :param pulumi.Input[bool] force_detach_policies: Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
        :param pulumi.Input[float] max_session_duration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
        :param pulumi.Input[str] name: The name of the role. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] path: The path to the role.
               See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
        :param pulumi.Input[str] permissions_boundary: The ARN of the policy that is used to set the permissions boundary for the role.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the IAM role
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

            if assume_role_policy is None:
                raise TypeError("Missing required property 'assume_role_policy'")
            __props__['assume_role_policy'] = assume_role_policy
            __props__['description'] = description
            __props__['force_detach_policies'] = force_detach_policies
            __props__['max_session_duration'] = max_session_duration
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['path'] = path
            __props__['permissions_boundary'] = permissions_boundary
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['create_date'] = None
            __props__['unique_id'] = None
        super(Role, __self__).__init__(
            'aws:iam/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            assume_role_policy: Optional[pulumi.Input[str]] = None,
            create_date: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            force_detach_policies: Optional[pulumi.Input[bool]] = None,
            max_session_duration: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            permissions_boundary: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            unique_id: Optional[pulumi.Input[str]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) specifying the role.
        :param pulumi.Input[str] assume_role_policy: The policy that grants an entity permission to assume the role.
        :param pulumi.Input[str] create_date: The creation date of the IAM role.
        :param pulumi.Input[str] description: The description of the role.
        :param pulumi.Input[bool] force_detach_policies: Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
        :param pulumi.Input[float] max_session_duration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
        :param pulumi.Input[str] name: The name of the role. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] path: The path to the role.
               See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
        :param pulumi.Input[str] permissions_boundary: The ARN of the policy that is used to set the permissions boundary for the role.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags for the IAM role
        :param pulumi.Input[str] unique_id: The stable and unique string identifying the role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["assume_role_policy"] = assume_role_policy
        __props__["create_date"] = create_date
        __props__["description"] = description
        __props__["force_detach_policies"] = force_detach_policies
        __props__["max_session_duration"] = max_session_duration
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["path"] = path
        __props__["permissions_boundary"] = permissions_boundary
        __props__["tags"] = tags
        __props__["unique_id"] = unique_id
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) specifying the role.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> str:
        """
        The policy that grants an entity permission to assume the role.
        """
        return pulumi.get(self, "assume_role_policy")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> str:
        """
        The creation date of the IAM role.
        """
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="forceDetachPolicies")
    def force_detach_policies(self) -> Optional[bool]:
        """
        Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
        """
        return pulumi.get(self, "force_detach_policies")

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> Optional[float]:
        """
        The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
        """
        return pulumi.get(self, "max_session_duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the role. If omitted, this provider will assign a random, unique name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[str]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The path to the role.
        See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> Optional[str]:
        """
        The ARN of the policy that is used to set the permissions boundary for the role.
        """
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value map of tags for the IAM role
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        The stable and unique string identifying the role.
        """
        return pulumi.get(self, "unique_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

