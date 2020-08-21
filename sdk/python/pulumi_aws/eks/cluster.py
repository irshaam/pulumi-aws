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

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled_cluster_log_types: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['ClusterVpcConfigArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EKS Cluster.

        ## Example Usage
        ### Example IAM Role for EKS Cluster

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.Role("example", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "eks.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        }
        \"\"\")
        example__amazon_eks_cluster_policy = aws.iam.RolePolicyAttachment("example-AmazonEKSClusterPolicy",
            policy_arn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
            role=example.name)
        example__amazon_eks_service_policy = aws.iam.RolePolicyAttachment("example-AmazonEKSServicePolicy",
            policy_arn="arn:aws:iam::aws:policy/AmazonEKSServicePolicy",
            role=example.name)
        ```
        ### Enabling Control Plane Logging

        [EKS Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) can be enabled via the `enabled_cluster_log_types` argument. To manage the CloudWatch Log Group retention period, the `cloudwatch.LogGroup` resource can be used.

        > The below configuration uses [`dependsOn`](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson) to prevent ordering issues with EKS automatically creating the log group first and a variable for naming consistency. Other ordering and naming methodologies may be more appropriate for your environment.

        ```python
        import pulumi
        import pulumi_aws as aws

        config = pulumi.Config()
        cluster_name = config.get("clusterName")
        if cluster_name is None:
            cluster_name = "example"
        example_log_group = aws.cloudwatch.LogGroup("exampleLogGroup", retention_in_days=7)
        # ... potentially other configuration ...
        example_cluster = aws.eks.Cluster("exampleCluster", enabled_cluster_log_types=[
            "api",
            "audit",
        ],
        opts=ResourceOptions(depends_on=[example_log_group]))
        # ... other configuration ...
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] enabled_cluster_log_types: A list of the desired control plane logging to enable. For more information, see [Amazon EKS Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
        :param pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']] encryption_config: Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.
        :param pulumi.Input[str] name: Name of the cluster.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding [`dependsOn`](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson) if using the `iam.RolePolicy` resource) or `iam.RolePolicyAttachment` resource, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
        :param pulumi.Input[str] version: Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.
        :param pulumi.Input[pulumi.InputType['ClusterVpcConfigArgs']] vpc_config: Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the Amazon EKS User Guide. Configuration detailed below.
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

            __props__['enabled_cluster_log_types'] = enabled_cluster_log_types
            __props__['encryption_config'] = encryption_config
            __props__['name'] = name
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['tags'] = tags
            __props__['version'] = version
            if vpc_config is None:
                raise TypeError("Missing required property 'vpc_config'")
            __props__['vpc_config'] = vpc_config
            __props__['arn'] = None
            __props__['certificate_authority'] = None
            __props__['created_at'] = None
            __props__['endpoint'] = None
            __props__['identities'] = None
            __props__['platform_version'] = None
            __props__['status'] = None
        super(Cluster, __self__).__init__(
            'aws:eks/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            certificate_authority: Optional[pulumi.Input[pulumi.InputType['ClusterCertificateAuthorityArgs']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            enabled_cluster_log_types: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            encryption_config: Optional[pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            identities: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['ClusterIdentityArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            platform_version: Optional[pulumi.Input[str]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None,
            vpc_config: Optional[pulumi.Input[pulumi.InputType['ClusterVpcConfigArgs']]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the cluster.
        :param pulumi.Input[pulumi.InputType['ClusterCertificateAuthorityArgs']] certificate_authority: Nested attribute containing `certificate-authority-data` for your cluster.
        :param pulumi.Input[List[pulumi.Input[str]]] enabled_cluster_log_types: A list of the desired control plane logging to enable. For more information, see [Amazon EKS Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
        :param pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']] encryption_config: Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.
        :param pulumi.Input[str] endpoint: The endpoint for your Kubernetes API server.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['ClusterIdentityArgs']]]] identities: Nested attribute containing identity provider information for your cluster. Only available on Kubernetes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019.
        :param pulumi.Input[str] name: Name of the cluster.
        :param pulumi.Input[str] platform_version: The platform version for the cluster.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding [`dependsOn`](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson) if using the `iam.RolePolicy` resource) or `iam.RolePolicyAttachment` resource, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.
        :param pulumi.Input[str] status: The status of the EKS cluster. One of `CREATING`, `ACTIVE`, `DELETING`, `FAILED`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
        :param pulumi.Input[str] version: Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.
        :param pulumi.Input[pulumi.InputType['ClusterVpcConfigArgs']] vpc_config: Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the Amazon EKS User Guide. Configuration detailed below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["certificate_authority"] = certificate_authority
        __props__["created_at"] = created_at
        __props__["enabled_cluster_log_types"] = enabled_cluster_log_types
        __props__["encryption_config"] = encryption_config
        __props__["endpoint"] = endpoint
        __props__["identities"] = identities
        __props__["name"] = name
        __props__["platform_version"] = platform_version
        __props__["role_arn"] = role_arn
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["version"] = version
        __props__["vpc_config"] = vpc_config
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the cluster.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> 'outputs.ClusterCertificateAuthority':
        """
        Nested attribute containing `certificate-authority-data` for your cluster.
        """
        return pulumi.get(self, "certificate_authority")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> Optional[List[str]]:
        """
        A list of the desired control plane logging to enable. For more information, see [Amazon EKS Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
        """
        return pulumi.get(self, "enabled_cluster_log_types")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional['outputs.ClusterEncryptionConfig']:
        """
        Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The endpoint for your Kubernetes API server.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def identities(self) -> List['outputs.ClusterIdentity']:
        """
        Nested attribute containing identity provider information for your cluster. Only available on Kubernetes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> str:
        """
        The platform version for the cluster.
        """
        return pulumi.get(self, "platform_version")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding [`dependsOn`](https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson) if using the `iam.RolePolicy` resource) or `iam.RolePolicyAttachment` resource, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the EKS cluster. One of `CREATING`, `ACTIVE`, `DELETING`, `FAILED`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value map of resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> 'outputs.ClusterVpcConfig':
        """
        Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the Amazon EKS User Guide. Configuration detailed below.
        """
        return pulumi.get(self, "vpc_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

