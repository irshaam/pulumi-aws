# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ReplicationInstance']


class ReplicationInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocated_storage: Optional[pulumi.Input[float]] = None,
                 apply_immediately: Optional[pulumi.Input[bool]] = None,
                 auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 multi_az: Optional[pulumi.Input[bool]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 replication_instance_class: Optional[pulumi.Input[str]] = None,
                 replication_instance_id: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_security_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        dms_assume_role = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                identifiers=["dms.amazonaws.com"],
                type="Service",
            )],
        )])
        dms_access_for_endpoint = aws.iam.Role("dms-access-for-endpoint", assume_role_policy=dms_assume_role.json)
        dms_access_for_endpoint__amazon_dms_redshift_s3_role = aws.iam.RolePolicyAttachment("dms-access-for-endpoint-AmazonDMSRedshiftS3Role",
            policy_arn="arn:aws:iam::aws:policy/service-role/AmazonDMSRedshiftS3Role",
            role=dms_access_for_endpoint.name)
        dms_cloudwatch_logs_role = aws.iam.Role("dms-cloudwatch-logs-role", assume_role_policy=dms_assume_role.json)
        dms_cloudwatch_logs_role__amazon_dms_cloud_watch_logs_role = aws.iam.RolePolicyAttachment("dms-cloudwatch-logs-role-AmazonDMSCloudWatchLogsRole",
            policy_arn="arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole",
            role=dms_cloudwatch_logs_role.name)
        dms_vpc_role = aws.iam.Role("dms-vpc-role", assume_role_policy=dms_assume_role.json)
        dms_vpc_role__amazon_dmsvpc_management_role = aws.iam.RolePolicyAttachment("dms-vpc-role-AmazonDMSVPCManagementRole",
            policy_arn="arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole",
            role=dms_vpc_role.name)
        # Create a new replication instance
        test = aws.dms.ReplicationInstance("test",
            allocated_storage=20,
            apply_immediately=True,
            auto_minor_version_upgrade=True,
            availability_zone="us-west-2c",
            engine_version="3.1.4",
            kms_key_arn="arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
            multi_az=False,
            preferred_maintenance_window="sun:10:30-sun:14:30",
            publicly_accessible=True,
            replication_instance_class="dms.t2.micro",
            replication_instance_id="test-dms-replication-instance-tf",
            replication_subnet_group_id=aws_dms_replication_subnet_group["test-dms-replication-subnet-group-tf"]["id"],
            tags={
                "Name": "test",
            },
            vpc_security_group_ids=["sg-12345678"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param pulumi.Input[bool] apply_immediately: Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.
        :param pulumi.Input[bool] auto_minor_version_upgrade: Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
        :param pulumi.Input[str] availability_zone: The EC2 Availability Zone that the replication instance will be created in.
        :param pulumi.Input[str] engine_version: The engine version number of the replication instance.
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        :param pulumi.Input[bool] multi_az: Specifies if the replication instance is a multi-az deployment. You cannot set the `availability_zone` parameter if the `multi_az` parameter is set to `true`.
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param pulumi.Input[bool] publicly_accessible: Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.
        :param pulumi.Input[str] replication_instance_class: The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge`
        :param pulumi.Input[str] replication_instance_id: The replication instance identifier. This parameter is stored as a lowercase string.
        :param pulumi.Input[str] replication_subnet_group_id: A subnet group to associate with the replication instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] vpc_security_group_ids: A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.
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

            __props__['allocated_storage'] = allocated_storage
            __props__['apply_immediately'] = apply_immediately
            __props__['auto_minor_version_upgrade'] = auto_minor_version_upgrade
            __props__['availability_zone'] = availability_zone
            __props__['engine_version'] = engine_version
            __props__['kms_key_arn'] = kms_key_arn
            __props__['multi_az'] = multi_az
            __props__['preferred_maintenance_window'] = preferred_maintenance_window
            __props__['publicly_accessible'] = publicly_accessible
            if replication_instance_class is None:
                raise TypeError("Missing required property 'replication_instance_class'")
            __props__['replication_instance_class'] = replication_instance_class
            if replication_instance_id is None:
                raise TypeError("Missing required property 'replication_instance_id'")
            __props__['replication_instance_id'] = replication_instance_id
            __props__['replication_subnet_group_id'] = replication_subnet_group_id
            __props__['tags'] = tags
            __props__['vpc_security_group_ids'] = vpc_security_group_ids
            __props__['replication_instance_arn'] = None
            __props__['replication_instance_private_ips'] = None
            __props__['replication_instance_public_ips'] = None
        super(ReplicationInstance, __self__).__init__(
            'aws:dms/replicationInstance:ReplicationInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocated_storage: Optional[pulumi.Input[float]] = None,
            apply_immediately: Optional[pulumi.Input[bool]] = None,
            auto_minor_version_upgrade: Optional[pulumi.Input[bool]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            kms_key_arn: Optional[pulumi.Input[str]] = None,
            multi_az: Optional[pulumi.Input[bool]] = None,
            preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
            publicly_accessible: Optional[pulumi.Input[bool]] = None,
            replication_instance_arn: Optional[pulumi.Input[str]] = None,
            replication_instance_class: Optional[pulumi.Input[str]] = None,
            replication_instance_id: Optional[pulumi.Input[str]] = None,
            replication_instance_private_ips: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            replication_instance_public_ips: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_security_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> 'ReplicationInstance':
        """
        Get an existing ReplicationInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param pulumi.Input[bool] apply_immediately: Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.
        :param pulumi.Input[bool] auto_minor_version_upgrade: Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
        :param pulumi.Input[str] availability_zone: The EC2 Availability Zone that the replication instance will be created in.
        :param pulumi.Input[str] engine_version: The engine version number of the replication instance.
        :param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        :param pulumi.Input[bool] multi_az: Specifies if the replication instance is a multi-az deployment. You cannot set the `availability_zone` parameter if the `multi_az` parameter is set to `true`.
        :param pulumi.Input[str] preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        :param pulumi.Input[bool] publicly_accessible: Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.
        :param pulumi.Input[str] replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param pulumi.Input[str] replication_instance_class: The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge`
        :param pulumi.Input[str] replication_instance_id: The replication instance identifier. This parameter is stored as a lowercase string.
        :param pulumi.Input[List[pulumi.Input[str]]] replication_instance_private_ips: A list of the private IP addresses of the replication instance.
        :param pulumi.Input[List[pulumi.Input[str]]] replication_instance_public_ips: A list of the public IP addresses of the replication instance.
        :param pulumi.Input[str] replication_subnet_group_id: A subnet group to associate with the replication instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] vpc_security_group_ids: A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allocated_storage"] = allocated_storage
        __props__["apply_immediately"] = apply_immediately
        __props__["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        __props__["availability_zone"] = availability_zone
        __props__["engine_version"] = engine_version
        __props__["kms_key_arn"] = kms_key_arn
        __props__["multi_az"] = multi_az
        __props__["preferred_maintenance_window"] = preferred_maintenance_window
        __props__["publicly_accessible"] = publicly_accessible
        __props__["replication_instance_arn"] = replication_instance_arn
        __props__["replication_instance_class"] = replication_instance_class
        __props__["replication_instance_id"] = replication_instance_id
        __props__["replication_instance_private_ips"] = replication_instance_private_ips
        __props__["replication_instance_public_ips"] = replication_instance_public_ips
        __props__["replication_subnet_group_id"] = replication_subnet_group_id
        __props__["tags"] = tags
        __props__["vpc_security_group_ids"] = vpc_security_group_ids
        return ReplicationInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> float:
        """
        The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[bool]:
        """
        Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.
        """
        return pulumi.get(self, "apply_immediately")

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> bool:
        """
        Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
        """
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        The EC2 Availability Zone that the replication instance will be created in.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        The engine version number of the replication instance.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> bool:
        """
        Specifies if the replication instance is a multi-az deployment. You cannot set the `availability_zone` parameter if the `multi_az` parameter is set to `true`.
        """
        return pulumi.get(self, "multi_az")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> str:
        """
        The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> bool:
        """
        Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the replication instance.
        """
        return pulumi.get(self, "replication_instance_arn")

    @property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> str:
        """
        The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge`
        """
        return pulumi.get(self, "replication_instance_class")

    @property
    @pulumi.getter(name="replicationInstanceId")
    def replication_instance_id(self) -> str:
        """
        The replication instance identifier. This parameter is stored as a lowercase string.
        """
        return pulumi.get(self, "replication_instance_id")

    @property
    @pulumi.getter(name="replicationInstancePrivateIps")
    def replication_instance_private_ips(self) -> List[str]:
        """
        A list of the private IP addresses of the replication instance.
        """
        return pulumi.get(self, "replication_instance_private_ips")

    @property
    @pulumi.getter(name="replicationInstancePublicIps")
    def replication_instance_public_ips(self) -> List[str]:
        """
        A list of the public IP addresses of the replication instance.
        """
        return pulumi.get(self, "replication_instance_public_ips")

    @property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> str:
        """
        A subnet group to associate with the replication instance.
        """
        return pulumi.get(self, "replication_subnet_group_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> List[str]:
        """
        A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.
        """
        return pulumi.get(self, "vpc_security_group_ids")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

