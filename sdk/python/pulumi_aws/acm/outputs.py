# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'CertificateDomainValidationOption',
    'CertificateOptions',
]

@pulumi.output_type
class CertificateDomainValidationOption(dict):
    def __init__(__self__, *,
                 domain_name: Optional[str] = None,
                 resource_record_name: Optional[str] = None,
                 resource_record_type: Optional[str] = None,
                 resource_record_value: Optional[str] = None):
        """
        :param str domain_name: A domain name for which the certificate should be issued
        :param str resource_record_name: The name of the DNS record to create to validate the certificate
        :param str resource_record_type: The type of DNS record to create
        :param str resource_record_value: The value the DNS record needs to have
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if resource_record_name is not None:
            pulumi.set(__self__, "resource_record_name", resource_record_name)
        if resource_record_type is not None:
            pulumi.set(__self__, "resource_record_type", resource_record_type)
        if resource_record_value is not None:
            pulumi.set(__self__, "resource_record_value", resource_record_value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        A domain name for which the certificate should be issued
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[str]:
        """
        The name of the DNS record to create to validate the certificate
        """
        return pulumi.get(self, "resource_record_name")

    @property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[str]:
        """
        The type of DNS record to create
        """
        return pulumi.get(self, "resource_record_type")

    @property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[str]:
        """
        The value the DNS record needs to have
        """
        return pulumi.get(self, "resource_record_value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CertificateOptions(dict):
    def __init__(__self__, *,
                 certificate_transparency_logging_preference: Optional[str] = None):
        """
        :param str certificate_transparency_logging_preference: Specifies whether certificate details should be added to a certificate transparency log. Valid values are `ENABLED` or `DISABLED`. See https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency for more details.
        """
        if certificate_transparency_logging_preference is not None:
            pulumi.set(__self__, "certificate_transparency_logging_preference", certificate_transparency_logging_preference)

    @property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[str]:
        """
        Specifies whether certificate details should be added to a certificate transparency log. Valid values are `ENABLED` or `DISABLED`. See https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency for more details.
        """
        return pulumi.get(self, "certificate_transparency_logging_preference")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


