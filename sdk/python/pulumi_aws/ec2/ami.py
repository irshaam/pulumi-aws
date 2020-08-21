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

__all__ = ['Ami']


class Ami(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ebs_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEbsBlockDeviceArgs']]]]] = None,
                 ena_support: Optional[pulumi.Input[bool]] = None,
                 ephemeral_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEphemeralBlockDeviceArgs']]]]] = None,
                 image_location: Optional[pulumi.Input[str]] = None,
                 kernel_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ramdisk_id: Optional[pulumi.Input[str]] = None,
                 root_device_name: Optional[pulumi.Input[str]] = None,
                 sriov_net_support: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtualization_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The AMI resource allows the creation and management of a completely-custom
        *Amazon Machine Image* (AMI).

        If you just want to duplicate an existing AMI, possibly copying it to another
        region, it's better to use `ec2.AmiCopy` instead.

        If you just want to share an existing AMI with another AWS account,
        it's better to use `ec2.AmiLaunchPermission` instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create an AMI that will start a machine whose root device is backed by
        # an EBS volume populated from a snapshot. It is assumed that such a snapshot
        # already exists with the id "snap-xxxxxxxx".
        example = aws.ec2.Ami("example",
            ebs_block_devices=[aws.ec2.AmiEbsBlockDeviceArgs(
                device_name="/dev/xvda",
                snapshot_id="snap-xxxxxxxx",
                volume_size=8,
            )],
            root_device_name="/dev/xvda",
            virtualization_type="hvm")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: Machine architecture for created instances. Defaults to "x86_64".
        :param pulumi.Input[str] description: A longer, human-readable description for the AMI.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEbsBlockDeviceArgs']]]] ebs_block_devices: Nested block describing an EBS block device that should be
               attached to created instances. The structure of this block is described below.
        :param pulumi.Input[bool] ena_support: Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Nested block describing an ephemeral block device that
               should be attached to created instances. The structure of this block is described below.
        :param pulumi.Input[str] image_location: Path to an S3 object containing an image manifest, e.g. created
               by the `ec2-upload-bundle` command in the EC2 command line tools.
        :param pulumi.Input[str] kernel_id: The id of the kernel image (AKI) that will be used as the paravirtual
               kernel in created instances.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[str] ramdisk_id: The id of an initrd image (ARI) that will be used when booting the
               created instances.
        :param pulumi.Input[str] root_device_name: The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        :param pulumi.Input[str] sriov_net_support: When set to "simple" (the default), enables enhanced networking
               for created instances. No other value is supported at this time.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances
               will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
               changes the set of further arguments that are required, as described below.
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

            __props__['architecture'] = architecture
            __props__['description'] = description
            __props__['ebs_block_devices'] = ebs_block_devices
            __props__['ena_support'] = ena_support
            __props__['ephemeral_block_devices'] = ephemeral_block_devices
            __props__['image_location'] = image_location
            __props__['kernel_id'] = kernel_id
            __props__['name'] = name
            __props__['ramdisk_id'] = ramdisk_id
            __props__['root_device_name'] = root_device_name
            __props__['sriov_net_support'] = sriov_net_support
            __props__['tags'] = tags
            __props__['virtualization_type'] = virtualization_type
            __props__['arn'] = None
            __props__['manage_ebs_snapshots'] = None
            __props__['root_snapshot_id'] = None
        super(Ami, __self__).__init__(
            'aws:ec2/ami:Ami',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ebs_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEbsBlockDeviceArgs']]]]] = None,
            ena_support: Optional[pulumi.Input[bool]] = None,
            ephemeral_block_devices: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEphemeralBlockDeviceArgs']]]]] = None,
            image_location: Optional[pulumi.Input[str]] = None,
            kernel_id: Optional[pulumi.Input[str]] = None,
            manage_ebs_snapshots: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ramdisk_id: Optional[pulumi.Input[str]] = None,
            root_device_name: Optional[pulumi.Input[str]] = None,
            root_snapshot_id: Optional[pulumi.Input[str]] = None,
            sriov_net_support: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtualization_type: Optional[pulumi.Input[str]] = None) -> 'Ami':
        """
        Get an existing Ami resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: Machine architecture for created instances. Defaults to "x86_64".
        :param pulumi.Input[str] arn: The ARN of the AMI.
        :param pulumi.Input[str] description: A longer, human-readable description for the AMI.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEbsBlockDeviceArgs']]]] ebs_block_devices: Nested block describing an EBS block device that should be
               attached to created instances. The structure of this block is described below.
        :param pulumi.Input[bool] ena_support: Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AmiEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Nested block describing an ephemeral block device that
               should be attached to created instances. The structure of this block is described below.
        :param pulumi.Input[str] image_location: Path to an S3 object containing an image manifest, e.g. created
               by the `ec2-upload-bundle` command in the EC2 command line tools.
        :param pulumi.Input[str] kernel_id: The id of the kernel image (AKI) that will be used as the paravirtual
               kernel in created instances.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[str] ramdisk_id: The id of an initrd image (ARI) that will be used when booting the
               created instances.
        :param pulumi.Input[str] root_device_name: The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        :param pulumi.Input[str] root_snapshot_id: The Snapshot ID for the root volume (for EBS-backed AMIs)
        :param pulumi.Input[str] sriov_net_support: When set to "simple" (the default), enables enhanced networking
               for created instances. No other value is supported at this time.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances
               will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
               changes the set of further arguments that are required, as described below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["architecture"] = architecture
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["ebs_block_devices"] = ebs_block_devices
        __props__["ena_support"] = ena_support
        __props__["ephemeral_block_devices"] = ephemeral_block_devices
        __props__["image_location"] = image_location
        __props__["kernel_id"] = kernel_id
        __props__["manage_ebs_snapshots"] = manage_ebs_snapshots
        __props__["name"] = name
        __props__["ramdisk_id"] = ramdisk_id
        __props__["root_device_name"] = root_device_name
        __props__["root_snapshot_id"] = root_snapshot_id
        __props__["sriov_net_support"] = sriov_net_support
        __props__["tags"] = tags
        __props__["virtualization_type"] = virtualization_type
        return Ami(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[str]:
        """
        Machine architecture for created instances. Defaults to "x86_64".
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the AMI.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A longer, human-readable description for the AMI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> List['outputs.AmiEbsBlockDevice']:
        """
        Nested block describing an EBS block device that should be
        attached to created instances. The structure of this block is described below.
        """
        return pulumi.get(self, "ebs_block_devices")

    @property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> Optional[bool]:
        """
        Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        """
        return pulumi.get(self, "ena_support")

    @property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> List['outputs.AmiEphemeralBlockDevice']:
        """
        Nested block describing an ephemeral block device that
        should be attached to created instances. The structure of this block is described below.
        """
        return pulumi.get(self, "ephemeral_block_devices")

    @property
    @pulumi.getter(name="imageLocation")
    def image_location(self) -> str:
        """
        Path to an S3 object containing an image manifest, e.g. created
        by the `ec2-upload-bundle` command in the EC2 command line tools.
        """
        return pulumi.get(self, "image_location")

    @property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> Optional[str]:
        """
        The id of the kernel image (AKI) that will be used as the paravirtual
        kernel in created instances.
        """
        return pulumi.get(self, "kernel_id")

    @property
    @pulumi.getter(name="manageEbsSnapshots")
    def manage_ebs_snapshots(self) -> bool:
        return pulumi.get(self, "manage_ebs_snapshots")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A region-unique name for the AMI.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ramdiskId")
    def ramdisk_id(self) -> Optional[str]:
        """
        The id of an initrd image (ARI) that will be used when booting the
        created instances.
        """
        return pulumi.get(self, "ramdisk_id")

    @property
    @pulumi.getter(name="rootDeviceName")
    def root_device_name(self) -> Optional[str]:
        """
        The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        """
        return pulumi.get(self, "root_device_name")

    @property
    @pulumi.getter(name="rootSnapshotId")
    def root_snapshot_id(self) -> str:
        """
        The Snapshot ID for the root volume (for EBS-backed AMIs)
        """
        return pulumi.get(self, "root_snapshot_id")

    @property
    @pulumi.getter(name="sriovNetSupport")
    def sriov_net_support(self) -> Optional[str]:
        """
        When set to "simple" (the default), enables enhanced networking
        for created instances. No other value is supported at this time.
        """
        return pulumi.get(self, "sriov_net_support")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> Optional[str]:
        """
        Keyword to choose what virtualization mode created instances
        will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
        changes the set of further arguments that are required, as described below.
        """
        return pulumi.get(self, "virtualization_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

