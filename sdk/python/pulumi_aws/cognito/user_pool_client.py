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

__all__ = ['UserPoolClient']


class UserPoolClient(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_oauth_flows: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[bool]] = None,
                 allowed_oauth_scopes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 analytics_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']]] = None,
                 callback_urls: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 default_redirect_uri: Optional[pulumi.Input[str]] = None,
                 explicit_auth_flows: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 generate_secret: Optional[pulumi.Input[bool]] = None,
                 logout_urls: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prevent_user_existence_errors: Optional[pulumi.Input[str]] = None,
                 read_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 refresh_token_validity: Optional[pulumi.Input[float]] = None,
                 supported_identity_providers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 write_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Cognito User Pool Client resource.

        ## Example Usage
        ### Create a basic user pool client

        ```python
        import pulumi
        import pulumi_aws as aws

        pool = aws.cognito.UserPool("pool")
        client = aws.cognito.UserPoolClient("client", user_pool_id=pool.id)
        ```
        ### Create a user pool client with no SRP authentication

        ```python
        import pulumi
        import pulumi_aws as aws

        pool = aws.cognito.UserPool("pool")
        client = aws.cognito.UserPoolClient("client",
            explicit_auth_flows=["ADMIN_NO_SRP_AUTH"],
            generate_secret=True,
            user_pool_id=pool.id)
        ```
        ### Create a user pool client with pinpoint analytics

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_caller_identity()
        test_user_pool = aws.cognito.UserPool("testUserPool")
        test_app = aws.pinpoint.App("testApp")
        test_role = aws.iam.Role("testRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "cognito-idp.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        test_role_policy = aws.iam.RolePolicy("testRolePolicy",
            policy=test_app.application_id.apply(lambda application_id: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": [
                "mobiletargeting:UpdateEndpoint",
                "mobiletargeting:PutItems"
              ],
              "Effect": "Allow",
              "Resource": "arn:aws:mobiletargeting:*:{current.account_id}:apps/{application_id}*"
            }}
          ]
        }}

        \"\"\"),
            role=test_role.id)
        test_user_pool_client = aws.cognito.UserPoolClient("testUserPoolClient",
            analytics_configuration=aws.cognito.UserPoolClientAnalyticsConfigurationArgs(
                application_id=test_app.application_id,
                external_id="some_id",
                role_arn=test_role.arn,
                user_data_shared=True,
            ),
            user_pool_id=test_user_pool.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] allowed_oauth_flows: List of allowed OAuth flows (code, implicit, client_credentials).
        :param pulumi.Input[bool] allowed_oauth_flows_user_pool_client: Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
        :param pulumi.Input[List[pulumi.Input[str]]] allowed_oauth_scopes: List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
        :param pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']] analytics_configuration: The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.
        :param pulumi.Input[List[pulumi.Input[str]]] callback_urls: List of allowed callback URLs for the identity providers.
        :param pulumi.Input[str] default_redirect_uri: The default redirect URI. Must be in the list of callback URLs.
        :param pulumi.Input[List[pulumi.Input[str]]] explicit_auth_flows: List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
        :param pulumi.Input[bool] generate_secret: Should an application secret be generated.
        :param pulumi.Input[List[pulumi.Input[str]]] logout_urls: List of allowed logout URLs for the identity providers.
        :param pulumi.Input[str] name: The name of the application client.
        :param pulumi.Input[str] prevent_user_existence_errors: Choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to `ENABLED` and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `UserNotFoundException` exception if the user does not exist in the user pool.
        :param pulumi.Input[List[pulumi.Input[str]]] read_attributes: List of user pool attributes the application client can read from.
        :param pulumi.Input[float] refresh_token_validity: The time limit in days refresh tokens are valid for.
        :param pulumi.Input[List[pulumi.Input[str]]] supported_identity_providers: List of provider names for the identity providers that are supported on this client.
        :param pulumi.Input[str] user_pool_id: The user pool the client belongs to.
        :param pulumi.Input[List[pulumi.Input[str]]] write_attributes: List of user pool attributes the application client can write to.
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

            __props__['allowed_oauth_flows'] = allowed_oauth_flows
            __props__['allowed_oauth_flows_user_pool_client'] = allowed_oauth_flows_user_pool_client
            __props__['allowed_oauth_scopes'] = allowed_oauth_scopes
            __props__['analytics_configuration'] = analytics_configuration
            __props__['callback_urls'] = callback_urls
            __props__['default_redirect_uri'] = default_redirect_uri
            __props__['explicit_auth_flows'] = explicit_auth_flows
            __props__['generate_secret'] = generate_secret
            __props__['logout_urls'] = logout_urls
            __props__['name'] = name
            __props__['prevent_user_existence_errors'] = prevent_user_existence_errors
            __props__['read_attributes'] = read_attributes
            __props__['refresh_token_validity'] = refresh_token_validity
            __props__['supported_identity_providers'] = supported_identity_providers
            if user_pool_id is None:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__['user_pool_id'] = user_pool_id
            __props__['write_attributes'] = write_attributes
            __props__['client_secret'] = None
        super(UserPoolClient, __self__).__init__(
            'aws:cognito/userPoolClient:UserPoolClient',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_oauth_flows: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            allowed_oauth_flows_user_pool_client: Optional[pulumi.Input[bool]] = None,
            allowed_oauth_scopes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            analytics_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']]] = None,
            callback_urls: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            client_secret: Optional[pulumi.Input[str]] = None,
            default_redirect_uri: Optional[pulumi.Input[str]] = None,
            explicit_auth_flows: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            generate_secret: Optional[pulumi.Input[bool]] = None,
            logout_urls: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            prevent_user_existence_errors: Optional[pulumi.Input[str]] = None,
            read_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            refresh_token_validity: Optional[pulumi.Input[float]] = None,
            supported_identity_providers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            user_pool_id: Optional[pulumi.Input[str]] = None,
            write_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> 'UserPoolClient':
        """
        Get an existing UserPoolClient resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] allowed_oauth_flows: List of allowed OAuth flows (code, implicit, client_credentials).
        :param pulumi.Input[bool] allowed_oauth_flows_user_pool_client: Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
        :param pulumi.Input[List[pulumi.Input[str]]] allowed_oauth_scopes: List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
        :param pulumi.Input[pulumi.InputType['UserPoolClientAnalyticsConfigurationArgs']] analytics_configuration: The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.
        :param pulumi.Input[List[pulumi.Input[str]]] callback_urls: List of allowed callback URLs for the identity providers.
        :param pulumi.Input[str] client_secret: The client secret of the user pool client.
        :param pulumi.Input[str] default_redirect_uri: The default redirect URI. Must be in the list of callback URLs.
        :param pulumi.Input[List[pulumi.Input[str]]] explicit_auth_flows: List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
        :param pulumi.Input[bool] generate_secret: Should an application secret be generated.
        :param pulumi.Input[List[pulumi.Input[str]]] logout_urls: List of allowed logout URLs for the identity providers.
        :param pulumi.Input[str] name: The name of the application client.
        :param pulumi.Input[str] prevent_user_existence_errors: Choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to `ENABLED` and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `UserNotFoundException` exception if the user does not exist in the user pool.
        :param pulumi.Input[List[pulumi.Input[str]]] read_attributes: List of user pool attributes the application client can read from.
        :param pulumi.Input[float] refresh_token_validity: The time limit in days refresh tokens are valid for.
        :param pulumi.Input[List[pulumi.Input[str]]] supported_identity_providers: List of provider names for the identity providers that are supported on this client.
        :param pulumi.Input[str] user_pool_id: The user pool the client belongs to.
        :param pulumi.Input[List[pulumi.Input[str]]] write_attributes: List of user pool attributes the application client can write to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allowed_oauth_flows"] = allowed_oauth_flows
        __props__["allowed_oauth_flows_user_pool_client"] = allowed_oauth_flows_user_pool_client
        __props__["allowed_oauth_scopes"] = allowed_oauth_scopes
        __props__["analytics_configuration"] = analytics_configuration
        __props__["callback_urls"] = callback_urls
        __props__["client_secret"] = client_secret
        __props__["default_redirect_uri"] = default_redirect_uri
        __props__["explicit_auth_flows"] = explicit_auth_flows
        __props__["generate_secret"] = generate_secret
        __props__["logout_urls"] = logout_urls
        __props__["name"] = name
        __props__["prevent_user_existence_errors"] = prevent_user_existence_errors
        __props__["read_attributes"] = read_attributes
        __props__["refresh_token_validity"] = refresh_token_validity
        __props__["supported_identity_providers"] = supported_identity_providers
        __props__["user_pool_id"] = user_pool_id
        __props__["write_attributes"] = write_attributes
        return UserPoolClient(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> Optional[List[str]]:
        """
        List of allowed OAuth flows (code, implicit, client_credentials).
        """
        return pulumi.get(self, "allowed_oauth_flows")

    @property
    @pulumi.getter(name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(self) -> Optional[bool]:
        """
        Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
        """
        return pulumi.get(self, "allowed_oauth_flows_user_pool_client")

    @property
    @pulumi.getter(name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> Optional[List[str]]:
        """
        List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
        """
        return pulumi.get(self, "allowed_oauth_scopes")

    @property
    @pulumi.getter(name="analyticsConfiguration")
    def analytics_configuration(self) -> Optional['outputs.UserPoolClientAnalyticsConfiguration']:
        """
        The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.
        """
        return pulumi.get(self, "analytics_configuration")

    @property
    @pulumi.getter(name="callbackUrls")
    def callback_urls(self) -> Optional[List[str]]:
        """
        List of allowed callback URLs for the identity providers.
        """
        return pulumi.get(self, "callback_urls")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        The client secret of the user pool client.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="defaultRedirectUri")
    def default_redirect_uri(self) -> Optional[str]:
        """
        The default redirect URI. Must be in the list of callback URLs.
        """
        return pulumi.get(self, "default_redirect_uri")

    @property
    @pulumi.getter(name="explicitAuthFlows")
    def explicit_auth_flows(self) -> Optional[List[str]]:
        """
        List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
        """
        return pulumi.get(self, "explicit_auth_flows")

    @property
    @pulumi.getter(name="generateSecret")
    def generate_secret(self) -> Optional[bool]:
        """
        Should an application secret be generated.
        """
        return pulumi.get(self, "generate_secret")

    @property
    @pulumi.getter(name="logoutUrls")
    def logout_urls(self) -> Optional[List[str]]:
        """
        List of allowed logout URLs for the identity providers.
        """
        return pulumi.get(self, "logout_urls")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the application client.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> str:
        """
        Choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to `ENABLED` and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `UserNotFoundException` exception if the user does not exist in the user pool.
        """
        return pulumi.get(self, "prevent_user_existence_errors")

    @property
    @pulumi.getter(name="readAttributes")
    def read_attributes(self) -> Optional[List[str]]:
        """
        List of user pool attributes the application client can read from.
        """
        return pulumi.get(self, "read_attributes")

    @property
    @pulumi.getter(name="refreshTokenValidity")
    def refresh_token_validity(self) -> Optional[float]:
        """
        The time limit in days refresh tokens are valid for.
        """
        return pulumi.get(self, "refresh_token_validity")

    @property
    @pulumi.getter(name="supportedIdentityProviders")
    def supported_identity_providers(self) -> Optional[List[str]]:
        """
        List of provider names for the identity providers that are supported on this client.
        """
        return pulumi.get(self, "supported_identity_providers")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> str:
        """
        The user pool the client belongs to.
        """
        return pulumi.get(self, "user_pool_id")

    @property
    @pulumi.getter(name="writeAttributes")
    def write_attributes(self) -> Optional[List[str]]:
        """
        List of user pool attributes the application client can write to.
        """
        return pulumi.get(self, "write_attributes")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

