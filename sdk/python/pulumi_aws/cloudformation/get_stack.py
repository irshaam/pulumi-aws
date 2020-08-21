# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetStackResult',
    'AwaitableGetStackResult',
    'get_stack',
]

@pulumi.output_type
class GetStackResult:
    """
    A collection of values returned by getStack.
    """
    def __init__(__self__, capabilities=None, description=None, disable_rollback=None, iam_role_arn=None, id=None, name=None, notification_arns=None, outputs=None, parameters=None, tags=None, template_body=None, timeout_in_minutes=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_rollback and not isinstance(disable_rollback, bool):
            raise TypeError("Expected argument 'disable_rollback' to be a bool")
        pulumi.set(__self__, "disable_rollback", disable_rollback)
        if iam_role_arn and not isinstance(iam_role_arn, str):
            raise TypeError("Expected argument 'iam_role_arn' to be a str")
        pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notification_arns and not isinstance(notification_arns, list):
            raise TypeError("Expected argument 'notification_arns' to be a list")
        pulumi.set(__self__, "notification_arns", notification_arns)
        if outputs and not isinstance(outputs, dict):
            raise TypeError("Expected argument 'outputs' to be a dict")
        pulumi.set(__self__, "outputs", outputs)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_body and not isinstance(template_body, str):
            raise TypeError("Expected argument 'template_body' to be a str")
        pulumi.set(__self__, "template_body", template_body)
        if timeout_in_minutes and not isinstance(timeout_in_minutes, float):
            raise TypeError("Expected argument 'timeout_in_minutes' to be a float")
        pulumi.set(__self__, "timeout_in_minutes", timeout_in_minutes)

    @property
    @pulumi.getter
    def capabilities(self) -> List[str]:
        """
        A list of capabilities
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the stack
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableRollback")
    def disable_rollback(self) -> bool:
        """
        Whether the rollback of the stack is disabled when stack creation fails
        """
        return pulumi.get(self, "disable_rollback")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> str:
        """
        The ARN of the IAM role used to create the stack.
        """
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> List[str]:
        """
        A list of SNS topic ARNs to publish stack related events
        """
        return pulumi.get(self, "notification_arns")

    @property
    @pulumi.getter
    def outputs(self) -> Mapping[str, str]:
        """
        A map of outputs from the stack.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def parameters(self) -> Mapping[str, str]:
        """
        A map of parameters that specify input parameters for the stack.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A map of tags associated with this stack.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> str:
        """
        Structure containing the template body.
        """
        return pulumi.get(self, "template_body")

    @property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> float:
        """
        The amount of time that can pass before the stack status becomes `CREATE_FAILED`
        """
        return pulumi.get(self, "timeout_in_minutes")


class AwaitableGetStackResult(GetStackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStackResult(
            capabilities=self.capabilities,
            description=self.description,
            disable_rollback=self.disable_rollback,
            iam_role_arn=self.iam_role_arn,
            id=self.id,
            name=self.name,
            notification_arns=self.notification_arns,
            outputs=self.outputs,
            parameters=self.parameters,
            tags=self.tags,
            template_body=self.template_body,
            timeout_in_minutes=self.timeout_in_minutes)


def get_stack(name: Optional[str] = None,
              tags: Optional[Mapping[str, str]] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStackResult:
    """
    The CloudFormation Stack data source allows access to stack
    outputs and other useful data including the template body.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    network = aws.cloudformation.get_stack(name="my-network-stack")
    web = aws.ec2.Instance("web",
        ami="ami-abb07bcb",
        instance_type="t1.micro",
        subnet_id=network.outputs["SubnetId"],
        tags={
            "Name": "HelloWorld",
        })
    ```


    :param str name: The name of the stack
    :param Mapping[str, str] tags: A map of tags associated with this stack.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:cloudformation/getStack:getStack', __args__, opts=opts, typ=GetStackResult).value

    return AwaitableGetStackResult(
        capabilities=__ret__.capabilities,
        description=__ret__.description,
        disable_rollback=__ret__.disable_rollback,
        iam_role_arn=__ret__.iam_role_arn,
        id=__ret__.id,
        name=__ret__.name,
        notification_arns=__ret__.notification_arns,
        outputs=__ret__.outputs,
        parameters=__ret__.parameters,
        tags=__ret__.tags,
        template_body=__ret__.template_body,
        timeout_in_minutes=__ret__.timeout_in_minutes)
