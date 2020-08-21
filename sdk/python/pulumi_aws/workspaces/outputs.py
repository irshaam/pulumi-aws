# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'DirectorySelfServicePermissions',
    'IpGroupRule',
    'WorkspaceWorkspaceProperties',
    'GetBundleComputeTypeResult',
    'GetBundleRootStorageResult',
    'GetBundleUserStorageResult',
    'GetDirectorySelfServicePermissionResult',
]

@pulumi.output_type
class DirectorySelfServicePermissions(dict):
    def __init__(__self__, *,
                 change_compute_type: Optional[bool] = None,
                 increase_volume_size: Optional[bool] = None,
                 rebuild_workspace: Optional[bool] = None,
                 restart_workspace: Optional[bool] = None,
                 switch_running_mode: Optional[bool] = None):
        """
        :param bool change_compute_type: Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default `false`.
        :param bool increase_volume_size: Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default `false`.
        :param bool rebuild_workspace: Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default `false`.
        :param bool restart_workspace: Whether WorkSpaces directory users can restart their workspace. Default `true`.
        :param bool switch_running_mode: Whether WorkSpaces directory users can switch the running mode of their workspace. Default `false`.
        """
        if change_compute_type is not None:
            pulumi.set(__self__, "change_compute_type", change_compute_type)
        if increase_volume_size is not None:
            pulumi.set(__self__, "increase_volume_size", increase_volume_size)
        if rebuild_workspace is not None:
            pulumi.set(__self__, "rebuild_workspace", rebuild_workspace)
        if restart_workspace is not None:
            pulumi.set(__self__, "restart_workspace", restart_workspace)
        if switch_running_mode is not None:
            pulumi.set(__self__, "switch_running_mode", switch_running_mode)

    @property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> Optional[bool]:
        """
        Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default `false`.
        """
        return pulumi.get(self, "change_compute_type")

    @property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> Optional[bool]:
        """
        Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default `false`.
        """
        return pulumi.get(self, "increase_volume_size")

    @property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> Optional[bool]:
        """
        Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default `false`.
        """
        return pulumi.get(self, "rebuild_workspace")

    @property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> Optional[bool]:
        """
        Whether WorkSpaces directory users can restart their workspace. Default `true`.
        """
        return pulumi.get(self, "restart_workspace")

    @property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> Optional[bool]:
        """
        Whether WorkSpaces directory users can switch the running mode of their workspace. Default `false`.
        """
        return pulumi.get(self, "switch_running_mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IpGroupRule(dict):
    def __init__(__self__, *,
                 source: str,
                 description: Optional[str] = None):
        """
        :param str source: The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        :param str description: The description.
        """
        pulumi.set(__self__, "source", source)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WorkspaceWorkspaceProperties(dict):
    def __init__(__self__, *,
                 compute_type_name: Optional[str] = None,
                 root_volume_size_gib: Optional[float] = None,
                 running_mode: Optional[str] = None,
                 running_mode_auto_stop_timeout_in_minutes: Optional[float] = None,
                 user_volume_size_gib: Optional[float] = None):
        """
        :param str compute_type_name: The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
        :param float root_volume_size_gib: The size of the root volume.
        :param str running_mode: The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
        :param float running_mode_auto_stop_timeout_in_minutes: The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
        :param float user_volume_size_gib: The size of the user storage.
        """
        if compute_type_name is not None:
            pulumi.set(__self__, "compute_type_name", compute_type_name)
        if root_volume_size_gib is not None:
            pulumi.set(__self__, "root_volume_size_gib", root_volume_size_gib)
        if running_mode is not None:
            pulumi.set(__self__, "running_mode", running_mode)
        if running_mode_auto_stop_timeout_in_minutes is not None:
            pulumi.set(__self__, "running_mode_auto_stop_timeout_in_minutes", running_mode_auto_stop_timeout_in_minutes)
        if user_volume_size_gib is not None:
            pulumi.set(__self__, "user_volume_size_gib", user_volume_size_gib)

    @property
    @pulumi.getter(name="computeTypeName")
    def compute_type_name(self) -> Optional[str]:
        """
        The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
        """
        return pulumi.get(self, "compute_type_name")

    @property
    @pulumi.getter(name="rootVolumeSizeGib")
    def root_volume_size_gib(self) -> Optional[float]:
        """
        The size of the root volume.
        """
        return pulumi.get(self, "root_volume_size_gib")

    @property
    @pulumi.getter(name="runningMode")
    def running_mode(self) -> Optional[str]:
        """
        The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
        """
        return pulumi.get(self, "running_mode")

    @property
    @pulumi.getter(name="runningModeAutoStopTimeoutInMinutes")
    def running_mode_auto_stop_timeout_in_minutes(self) -> Optional[float]:
        """
        The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
        """
        return pulumi.get(self, "running_mode_auto_stop_timeout_in_minutes")

    @property
    @pulumi.getter(name="userVolumeSizeGib")
    def user_volume_size_gib(self) -> Optional[float]:
        """
        The size of the user storage.
        """
        return pulumi.get(self, "user_volume_size_gib")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetBundleComputeTypeResult(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: The name of the bundle. You cannot combine this parameter with `bundle_id`.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the bundle. You cannot combine this parameter with `bundle_id`.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetBundleRootStorageResult(dict):
    def __init__(__self__, *,
                 capacity: str):
        """
        :param str capacity: The size of the user storage.
        """
        pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def capacity(self) -> str:
        """
        The size of the user storage.
        """
        return pulumi.get(self, "capacity")


@pulumi.output_type
class GetBundleUserStorageResult(dict):
    def __init__(__self__, *,
                 capacity: str):
        """
        :param str capacity: The size of the user storage.
        """
        pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def capacity(self) -> str:
        """
        The size of the user storage.
        """
        return pulumi.get(self, "capacity")


@pulumi.output_type
class GetDirectorySelfServicePermissionResult(dict):
    def __init__(__self__, *,
                 change_compute_type: bool,
                 increase_volume_size: bool,
                 rebuild_workspace: bool,
                 restart_workspace: bool,
                 switch_running_mode: bool):
        """
        :param bool change_compute_type: Whether WorkSpaces directory users can change the compute type (bundle) for their workspace.
        :param bool increase_volume_size: Whether WorkSpaces directory users can increase the volume size of the drives on their workspace.
        :param bool rebuild_workspace: Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state.
        :param bool restart_workspace: Whether WorkSpaces directory users can restart their workspace.
        :param bool switch_running_mode: Whether WorkSpaces directory users can switch the running mode of their workspace.
        """
        pulumi.set(__self__, "change_compute_type", change_compute_type)
        pulumi.set(__self__, "increase_volume_size", increase_volume_size)
        pulumi.set(__self__, "rebuild_workspace", rebuild_workspace)
        pulumi.set(__self__, "restart_workspace", restart_workspace)
        pulumi.set(__self__, "switch_running_mode", switch_running_mode)

    @property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> bool:
        """
        Whether WorkSpaces directory users can change the compute type (bundle) for their workspace.
        """
        return pulumi.get(self, "change_compute_type")

    @property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> bool:
        """
        Whether WorkSpaces directory users can increase the volume size of the drives on their workspace.
        """
        return pulumi.get(self, "increase_volume_size")

    @property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> bool:
        """
        Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state.
        """
        return pulumi.get(self, "rebuild_workspace")

    @property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> bool:
        """
        Whether WorkSpaces directory users can restart their workspace.
        """
        return pulumi.get(self, "restart_workspace")

    @property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> bool:
        """
        Whether WorkSpaces directory users can switch the running mode of their workspace.
        """
        return pulumi.get(self, "switch_running_mode")


