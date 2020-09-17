# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['LoadBalancerBackendServerPolicy']

warnings.warn("aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy", DeprecationWarning)


class LoadBalancerBackendServerPolicy(pulumi.CustomResource):
    warnings.warn("aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_port: Optional[pulumi.Input[int]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches a load balancer policy to an ELB backend server.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        wu_tang = aws.elb.LoadBalancer("wu-tang",
            availability_zones=["us-east-1a"],
            listeners=[aws.elb.LoadBalancerListenerArgs(
                instance_port=443,
                instance_protocol="http",
                lb_port=443,
                lb_protocol="https",
                ssl_certificate_id="arn:aws:iam::000000000000:server-certificate/wu-tang.net",
            )],
            tags={
                "Name": "wu-tang",
            })
        wu_tang_ca_pubkey_policy = aws.elb.LoadBalancerPolicy("wu-tang-ca-pubkey-policy",
            load_balancer_name=wu_tang.name,
            policy_name="wu-tang-ca-pubkey-policy",
            policy_type_name="PublicKeyPolicyType",
            policy_attributes=[aws.elb.LoadBalancerPolicyPolicyAttributeArgs(
                name="PublicKey",
                value=(lambda path: open(path).read())("wu-tang-pubkey"),
            )])
        wu_tang_root_ca_backend_auth_policy = aws.elb.LoadBalancerPolicy("wu-tang-root-ca-backend-auth-policy",
            load_balancer_name=wu_tang.name,
            policy_name="wu-tang-root-ca-backend-auth-policy",
            policy_type_name="BackendServerAuthenticationPolicyType",
            policy_attributes=[aws.elb.LoadBalancerPolicyPolicyAttributeArgs(
                name="PublicKeyPolicyName",
                value=aws_load_balancer_policy["wu-tang-root-ca-pubkey-policy"]["policy_name"],
            )])
        wu_tang_backend_auth_policies_443 = aws.elb.LoadBalancerBackendServerPolicy("wu-tang-backend-auth-policies-443",
            load_balancer_name=wu_tang.name,
            instance_port=443,
            policy_names=[wu_tang_root_ca_backend_auth_policy.policy_name])
        ```

        Where the file `pubkey` in the current directory contains only the _public key_ of the certificate.

        ```python
        import pulumi
        ```

        This example shows how to enable backend authentication for an ELB as well as customize the TLS settings.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] instance_port: The instance port to apply the policy to.
        :param pulumi.Input[str] load_balancer_name: The load balancer to attach the policy to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: List of Policy Names to apply to the backend server.
        """
        pulumi.log.warn("LoadBalancerBackendServerPolicy is deprecated: aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy")
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

            if instance_port is None:
                raise TypeError("Missing required property 'instance_port'")
            __props__['instance_port'] = instance_port
            if load_balancer_name is None:
                raise TypeError("Missing required property 'load_balancer_name'")
            __props__['load_balancer_name'] = load_balancer_name
            __props__['policy_names'] = policy_names
        super(LoadBalancerBackendServerPolicy, __self__).__init__(
            'aws:elasticloadbalancing/loadBalancerBackendServerPolicy:LoadBalancerBackendServerPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_port: Optional[pulumi.Input[int]] = None,
            load_balancer_name: Optional[pulumi.Input[str]] = None,
            policy_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'LoadBalancerBackendServerPolicy':
        """
        Get an existing LoadBalancerBackendServerPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] instance_port: The instance port to apply the policy to.
        :param pulumi.Input[str] load_balancer_name: The load balancer to attach the policy to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_names: List of Policy Names to apply to the backend server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_port"] = instance_port
        __props__["load_balancer_name"] = load_balancer_name
        __props__["policy_names"] = policy_names
        return LoadBalancerBackendServerPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> pulumi.Output[int]:
        """
        The instance port to apply the policy to.
        """
        return pulumi.get(self, "instance_port")

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Output[str]:
        """
        The load balancer to attach the policy to.
        """
        return pulumi.get(self, "load_balancer_name")

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Policy Names to apply to the backend server.
        """
        return pulumi.get(self, "policy_names")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

