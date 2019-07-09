# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class S3BucketAssociation(pulumi.CustomResource):
    bucket_name: pulumi.Output[str]
    """
    The name of the S3 bucket that you want to associate with Amazon Macie.
    """
    classification_type: pulumi.Output[dict]
    """
    The configuration of how Amazon Macie classifies the S3 objects.
    """
    member_account_id: pulumi.Output[str]
    """
    The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.
    """
    prefix: pulumi.Output[str]
    """
    Object key prefix identifying one or more S3 objects to which the association applies.
    """
    def __init__(__self__, resource_name, opts=None, bucket_name=None, classification_type=None, member_account_id=None, prefix=None, __name__=None, __opts__=None):
        """
        Associates an S3 resource with Amazon Macie for monitoring and data classification.
        
        > **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the S3 bucket that you want to associate with Amazon Macie.
        :param pulumi.Input[dict] classification_type: The configuration of how Amazon Macie classifies the S3 objects.
        :param pulumi.Input[str] member_account_id: The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.
        :param pulumi.Input[str] prefix: Object key prefix identifying one or more S3 objects to which the association applies.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/macie_s3_bucket_association.html.markdown.
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

        if bucket_name is None:
            raise TypeError("Missing required property 'bucket_name'")
        __props__['bucket_name'] = bucket_name

        __props__['classification_type'] = classification_type

        __props__['member_account_id'] = member_account_id

        __props__['prefix'] = prefix

        super(S3BucketAssociation, __self__).__init__(
            'aws:macie/s3BucketAssociation:S3BucketAssociation',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

