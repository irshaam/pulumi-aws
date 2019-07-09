// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package aws

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of a registered AMI for use in other
// resources.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ami.html.markdown.
func LookupAmi(ctx *pulumi.Context, args *GetAmiArgs) (*GetAmiResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["executableUsers"] = args.ExecutableUsers
		inputs["filters"] = args.Filters
		inputs["mostRecent"] = args.MostRecent
		inputs["nameRegex"] = args.NameRegex
		inputs["owners"] = args.Owners
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:index/getAmi:getAmi", inputs)
	if err != nil {
		return nil, err
	}
	return &GetAmiResult{
		Architecture: outputs["architecture"],
		BlockDeviceMappings: outputs["blockDeviceMappings"],
		CreationDate: outputs["creationDate"],
		Description: outputs["description"],
		ExecutableUsers: outputs["executableUsers"],
		Filters: outputs["filters"],
		Hypervisor: outputs["hypervisor"],
		ImageId: outputs["imageId"],
		ImageLocation: outputs["imageLocation"],
		ImageOwnerAlias: outputs["imageOwnerAlias"],
		ImageType: outputs["imageType"],
		KernelId: outputs["kernelId"],
		MostRecent: outputs["mostRecent"],
		Name: outputs["name"],
		NameRegex: outputs["nameRegex"],
		OwnerId: outputs["ownerId"],
		Owners: outputs["owners"],
		Platform: outputs["platform"],
		ProductCodes: outputs["productCodes"],
		Public: outputs["public"],
		RamdiskId: outputs["ramdiskId"],
		RootDeviceName: outputs["rootDeviceName"],
		RootDeviceType: outputs["rootDeviceType"],
		RootSnapshotId: outputs["rootSnapshotId"],
		SriovNetSupport: outputs["sriovNetSupport"],
		State: outputs["state"],
		StateReason: outputs["stateReason"],
		Tags: outputs["tags"],
		VirtualizationType: outputs["virtualizationType"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getAmi.
type GetAmiArgs struct {
	// Limit search to users with *explicit* launch permission on
	// the image. Valid items are the numeric account ID or `self`.
	ExecutableUsers interface{}
	// One or more name/value pairs to filter off of. There are
	// several valid keys, for a full reference, check out
	// [describe-images in the AWS CLI reference][1].
	Filters interface{}
	// If more than one result is returned, use the most
	// recent AMI.
	MostRecent interface{}
	// A regex string to apply to the AMI list returned
	// by AWS. This allows more advanced filtering not supported from the AWS API. This
	// filtering is done locally on what AWS returns, and could have a performance
	// impact if the result is large. It is recommended to combine this with other
	// options to narrow down the list AWS returns.
	NameRegex interface{}
	// List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
	Owners interface{}
	Tags interface{}
}

// A collection of values returned by getAmi.
type GetAmiResult struct {
	// The OS architecture of the AMI (ie: `i386` or `x86_64`).
	Architecture interface{}
	// The block device mappings of the AMI.
	// * `block_device_mappings.#.device_name` - The physical name of the device.
	// * `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
	// will be deleted on termination.
	// * `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
	// is encrypted.
	// * `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
	// not a provisioned IOPS image, otherwise the supported IOPS count.
	// * `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
	// * `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
	// * `block_device_mappings.#.ebs.volume_type` - The volume type.
	// * `block_device_mappings.#.no_device` - Suppresses the specified device
	// included in the block device mapping of the AMI.
	// * `block_device_mappings.#.virtual_name` - The virtual device name (for
	// instance stores).
	BlockDeviceMappings interface{}
	// The date and time the image was created.
	CreationDate interface{}
	// The description of the AMI that was provided during image
	// creation.
	Description interface{}
	ExecutableUsers interface{}
	Filters interface{}
	// The hypervisor type of the image.
	Hypervisor interface{}
	// The ID of the AMI. Should be the same as the resource `id`.
	ImageId interface{}
	// The location of the AMI.
	ImageLocation interface{}
	// The AWS account alias (for example, `amazon`, `self`) or
	// the AWS account ID of the AMI owner.
	ImageOwnerAlias interface{}
	// The type of image.
	ImageType interface{}
	// The kernel associated with the image, if any. Only applicable
	// for machine images.
	KernelId interface{}
	MostRecent interface{}
	// The name of the AMI that was provided during image creation.
	Name interface{}
	NameRegex interface{}
	// The AWS account ID of the image owner.
	OwnerId interface{}
	Owners interface{}
	// The value is Windows for `Windows` AMIs; otherwise blank.
	Platform interface{}
	// Any product codes associated with the AMI.
	// * `product_codes.#.product_code_id` - The product code.
	// * `product_codes.#.product_code_type` - The type of product code.
	ProductCodes interface{}
	// `true` if the image has public launch permissions.
	Public interface{}
	// The RAM disk associated with the image, if any. Only applicable
	// for machine images.
	RamdiskId interface{}
	// The device name of the root device.
	RootDeviceName interface{}
	// The type of root device (ie: `ebs` or `instance-store`).
	RootDeviceType interface{}
	// The snapshot id associated with the root device, if any
	// (only applies to `ebs` root devices).
	RootSnapshotId interface{}
	// Specifies whether enhanced networking is enabled.
	SriovNetSupport interface{}
	// The current state of the AMI. If the state is `available`, the image
	// is successfully registered and can be used to launch an instance.
	State interface{}
	// Describes a state change. Fields are `UNSET` if not available.
	// * `state_reason.code` - The reason code for the state change.
	// * `state_reason.message` - The message for the state change.
	StateReason interface{}
	// Any tags assigned to the image.
	// * `tags.#.key` - The key name of the tag.
	// * `tags.#.value` - The value of the tag.
	Tags interface{}
	// The type of virtualization of the AMI (ie: `hvm` or
	// `paravirtual`).
	VirtualizationType interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
