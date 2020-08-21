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

__all__ = ['Authorizer']


class Authorizer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 authorizer_credentials_arn: Optional[pulumi.Input[str]] = None,
                 authorizer_type: Optional[pulumi.Input[str]] = None,
                 authorizer_uri: Optional[pulumi.Input[str]] = None,
                 identity_sources: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 jwt_configuration: Optional[pulumi.Input[pulumi.InputType['AuthorizerJwtConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 authorizer.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

        ## Example Usage
        ### Basic WebSocket API

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Authorizer("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            authorizer_type="REQUEST",
            authorizer_uri=aws_lambda_function["example"]["invoke_arn"],
            identity_sources=["route.request.header.Auth"])
        ```
        ### Basic HTTP API

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Authorizer("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            authorizer_type="JWT",
            identity_sources=["$request.header.Authorization"],
            jwt_configuration=aws.apigatewayv2.AuthorizerJwtConfigurationArgs(
                audiences=["example"],
                issuer=f"https://{aws_cognito_user_pool['example']['endpoint']}",
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] authorizer_credentials_arn: The required credentials as an IAM role for API Gateway to invoke the authorizer.
               Supported only for `REQUEST` authorizers.
        :param pulumi.Input[str] authorizer_type: The authorizer type. Valid values: `JWT`, `REQUEST`.
               For WebSocket APIs, specify `REQUEST` for a Lambda function using incoming request parameters.
               For HTTP APIs, specify `JWT` to use JSON Web Tokens.
        :param pulumi.Input[str] authorizer_uri: The authorizer's Uniform Resource Identifier (URI).
               For `REQUEST` authorizers this must be a well-formed Lambda function URI, such as the `invoke_arn` attribute of the `lambda.Function` resource.
               Supported only for `REQUEST` authorizers.
        :param pulumi.Input[List[pulumi.Input[str]]] identity_sources: The identity sources for which authorization is requested.
               For `REQUEST` authorizers the value is a list of one or more mapping expressions of the specified request parameters.
               For `JWT` authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.
        :param pulumi.Input[pulumi.InputType['AuthorizerJwtConfigurationArgs']] jwt_configuration: The configuration of a JWT authorizer. Required for the `JWT` authorizer type.
               Supported only for HTTP APIs.
        :param pulumi.Input[str] name: The name of the authorizer.
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

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['authorizer_credentials_arn'] = authorizer_credentials_arn
            if authorizer_type is None:
                raise TypeError("Missing required property 'authorizer_type'")
            __props__['authorizer_type'] = authorizer_type
            __props__['authorizer_uri'] = authorizer_uri
            if identity_sources is None:
                raise TypeError("Missing required property 'identity_sources'")
            __props__['identity_sources'] = identity_sources
            __props__['jwt_configuration'] = jwt_configuration
            __props__['name'] = name
        super(Authorizer, __self__).__init__(
            'aws:apigatewayv2/authorizer:Authorizer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            authorizer_credentials_arn: Optional[pulumi.Input[str]] = None,
            authorizer_type: Optional[pulumi.Input[str]] = None,
            authorizer_uri: Optional[pulumi.Input[str]] = None,
            identity_sources: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            jwt_configuration: Optional[pulumi.Input[pulumi.InputType['AuthorizerJwtConfigurationArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Authorizer':
        """
        Get an existing Authorizer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] authorizer_credentials_arn: The required credentials as an IAM role for API Gateway to invoke the authorizer.
               Supported only for `REQUEST` authorizers.
        :param pulumi.Input[str] authorizer_type: The authorizer type. Valid values: `JWT`, `REQUEST`.
               For WebSocket APIs, specify `REQUEST` for a Lambda function using incoming request parameters.
               For HTTP APIs, specify `JWT` to use JSON Web Tokens.
        :param pulumi.Input[str] authorizer_uri: The authorizer's Uniform Resource Identifier (URI).
               For `REQUEST` authorizers this must be a well-formed Lambda function URI, such as the `invoke_arn` attribute of the `lambda.Function` resource.
               Supported only for `REQUEST` authorizers.
        :param pulumi.Input[List[pulumi.Input[str]]] identity_sources: The identity sources for which authorization is requested.
               For `REQUEST` authorizers the value is a list of one or more mapping expressions of the specified request parameters.
               For `JWT` authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.
        :param pulumi.Input[pulumi.InputType['AuthorizerJwtConfigurationArgs']] jwt_configuration: The configuration of a JWT authorizer. Required for the `JWT` authorizer type.
               Supported only for HTTP APIs.
        :param pulumi.Input[str] name: The name of the authorizer.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["authorizer_credentials_arn"] = authorizer_credentials_arn
        __props__["authorizer_type"] = authorizer_type
        __props__["authorizer_uri"] = authorizer_uri
        __props__["identity_sources"] = identity_sources
        __props__["jwt_configuration"] = jwt_configuration
        __props__["name"] = name
        return Authorizer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> str:
        """
        The API identifier.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> Optional[str]:
        """
        The required credentials as an IAM role for API Gateway to invoke the authorizer.
        Supported only for `REQUEST` authorizers.
        """
        return pulumi.get(self, "authorizer_credentials_arn")

    @property
    @pulumi.getter(name="authorizerType")
    def authorizer_type(self) -> str:
        """
        The authorizer type. Valid values: `JWT`, `REQUEST`.
        For WebSocket APIs, specify `REQUEST` for a Lambda function using incoming request parameters.
        For HTTP APIs, specify `JWT` to use JSON Web Tokens.
        """
        return pulumi.get(self, "authorizer_type")

    @property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[str]:
        """
        The authorizer's Uniform Resource Identifier (URI).
        For `REQUEST` authorizers this must be a well-formed Lambda function URI, such as the `invoke_arn` attribute of the `lambda.Function` resource.
        Supported only for `REQUEST` authorizers.
        """
        return pulumi.get(self, "authorizer_uri")

    @property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> List[str]:
        """
        The identity sources for which authorization is requested.
        For `REQUEST` authorizers the value is a list of one or more mapping expressions of the specified request parameters.
        For `JWT` authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.
        """
        return pulumi.get(self, "identity_sources")

    @property
    @pulumi.getter(name="jwtConfiguration")
    def jwt_configuration(self) -> Optional['outputs.AuthorizerJwtConfiguration']:
        """
        The configuration of a JWT authorizer. Required for the `JWT` authorizer type.
        Supported only for HTTP APIs.
        """
        return pulumi.get(self, "jwt_configuration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the authorizer.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

